"""Export public analysis evidence, without persisting the analysis credential."""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

PROJECT = "RodrigoAC12_Ecolog-stica_Lima"
BASE_URL = "https://sonarcloud.io"


def read_api(endpoint: str, parameters: dict):
    headers = {"Accept": "application/json", "User-Agent": "Ecologistica-SonarCloud-Evidence"}
    token = os.environ.get("SONAR_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    request = Request(BASE_URL + endpoint + "?" + urlencode(parameters), headers=headers)
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def export_report():
    analyses = read_api("/api/project_analyses/search", {"project": PROJECT, "branch": "main", "ps": 10})
    expected = os.environ.get("GITHUB_SHA")
    analysis = next((item for item in analyses["analyses"] if not expected or item.get("revision") == expected), None)
    if analysis is None:
        raise RuntimeError("El análisis disponible no corresponde a la revisión de esta ejecución.")
    report = {
        "executedAt": datetime.now(timezone.utc).isoformat(),
        "project": PROJECT,
        "branch": "main",
        "analysis": analysis,
        "qualityGate": read_api("/api/qualitygates/project_status", {"analysisId": analysis["key"]}),
        "measures": read_api("/api/measures/component", {
            "component": PROJECT, "branch": "main",
            "metricKeys": "coverage,line_coverage,branch_coverage,duplicated_lines_density,ncloc,bugs,vulnerabilities,code_smells,security_hotspots",
        }),
        "issues": read_api("/api/issues/search", {"componentKeys": PROJECT, "branch": "main", "resolved": "false", "ps": 100}),
        "scope": "Código de aplicación, scripts, Dockerfiles y workflows; cobertura backend, frontend y comprobador de enlaces.",
    }
    destination = Path("sonarcloud-report.json")
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"revision": analysis.get("revision"), "qualityGate": report["qualityGate"]["projectStatus"]["status"], "openIssues": report["issues"]["paging"]["total"]}))


if __name__ == "__main__":
    export_report()
