import hashlib
import json
import os
import socket
import ssl
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from local_staging_settings import load_settings


def verify() -> None:
    repository = Path(__file__).resolve().parents[1]
    directory = Path(os.environ["LOCALAPPDATA"]) / "EcoLogistica"
    settings = load_settings(directory)
    authority = directory / "localhost-root.crt"
    context = ssl.create_default_context(cafile=str(authority))
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    port = int(settings["STAGING_HTTPS_PORT"])
    base_url = f"https://localhost:{port}"

    def request(path: str, body: dict | None = None, token: str | None = None):
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        data = json.dumps(body).encode() if body is not None else None
        with urlopen(Request(base_url + path, data=data, headers=headers), context=context, timeout=15) as response:
            return response.status, response.headers, response.read()

    health_status, _, health_data = request("/health")
    assert health_status == 200 and json.loads(health_data)["status"] == "ok"
    frontend_status, frontend_headers, frontend_data = request("/")
    assert frontend_status == 200 and 'id="root"' in frontend_data.decode("utf-8")
    assert frontend_headers["X-Content-Type-Options"] == "nosniff"
    assert frontend_headers["X-Frame-Options"] == "DENY"
    assert frontend_headers["Referrer-Policy"] == "no-referrer"
    http_url = f"http://localhost:{settings.get('STAGING_HTTP_PORT', '8080')}"
    with urlopen(http_url, timeout=15) as local_http:
        assert local_http.status == 200 and 'id="root"' in local_http.read().decode("utf-8")
    try:
        request("/api/v1/vehiculos")
        raise AssertionError("La API permitió una consulta sin autenticación")
    except HTTPError as error:
        assert error.code == 401
    login_status, _, login_data = request("/api/v1/auth/login", {
        "email": settings["BOOTSTRAP_OPERATOR_EMAIL"],
        "password": settings["BOOTSTRAP_OPERATOR_PASSWORD"],
    })
    assert login_status == 200
    token = json.loads(login_data)["access_token"]
    resources = {}
    for resource in ("vehiculos", "pedidos", "conductores", "clientes"):
        status, _, content = request(f"/api/v1/{resource}", token=token)
        entities = json.loads(content)
        assert status == 200 and isinstance(entities, list)
        resources[resource] = {"status": status, "count": len(entities)}
    with socket.create_connection(("localhost", port), timeout=15) as connection:
        with context.wrap_socket(connection, server_hostname="localhost") as encrypted:
            certificate = encrypted.getpeercert()
            tls_version = encrypted.version()
    report = {
        "executed_at": datetime.now(timezone.utc).isoformat(),
        "scope": "localhost",
        "url": base_url,
        "http_url": http_url,
        "tls_version": tls_version,
        "certificate_hostname_verified": True,
        "certificate_chain_verified": True,
        "authority_sha256": hashlib.sha256(authority.read_bytes()).hexdigest(),
        "certificate_subject": certificate["subject"],
        "health_status": health_status,
        "frontend_status": frontend_status,
        "unauthenticated_access_status": 401,
        "login_status": login_status,
        "security_headers_verified": True,
        "resources": resources,
        "credentials_included": False,
        "operating_system_trust_store_modified": False,
        "limits": ["Validación local; no se evalúa acceso remoto.", "La confianza del navegador en la CA local se administra por separado."],
    }
    destination = repository / "docs" / "03 Implementación" / "Sprint 03" / "evidencias" / "staging-local.json"
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"url": base_url, "status": "PASSED", "tls": tls_version, "evidence": str(destination)}, ensure_ascii=False))


if __name__ == "__main__":
    verify()
