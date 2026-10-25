"""Inspect CodeQL SARIF exported by CI; do not infer zero alerts from workflow status.

Usage: python scripts/check_codeql_sarif.py codeql-sarif
"""
import json
import sys
from pathlib import Path


def check_reports(directory: Path) -> int:
    paths = sorted(directory.glob("*.sarif"))
    if not paths:
        print("ERROR: no CodeQL SARIF report found.")
        return 1

    total = high = critical = unclassified = 0
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        for run in data.get("runs", []):
            rules = run.get("tool", {}).get("driver", {}).get("rules", [])
            for result in run.get("results", []):
                total += 1
                index = result.get("ruleIndex")
                meta = rules[index] if isinstance(index, int) and 0 <= index < len(rules) else {}
                props = dict(meta.get("properties", {}))
                props.update(result.get("properties", {}))
                rating = props.get("security-severity")
                try:
                    severity = float(rating)
                except (ValueError, TypeError):
                    unclassified += 1
                    print(f"UNCLASSIFIED: {result.get('ruleId', '?')}")
                    continue
                if severity >= 9.0:
                    critical += 1
                elif severity >= 7.0:
                    high += 1
                print(f"rule={result.get('ruleId', '?')} severity={severity}")
    print(f"CodeQL SARIF: results={total}, critical={critical}, high={high}, unclassified={unclassified}")
    if critical:
        print("FAILED: CodeQL reports a critical security finding.")
        return 1
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: check_codeql_sarif.py DIRECTORY")
        sys.exit(2)
    sys.exit(check_reports(Path(sys.argv[1])))
