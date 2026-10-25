"""Regression for US-013/US-015 when two requests race on the same client email."""
from sqlalchemy import select

from app.models import Audit, Client
from app.repositories import clients as repo


def test_database_prevents_duplicate_email_even_if_precheck_is_stale(context, monkeypatch):
    http, headers = context["client"], context["operator"]
    first = http.post("/api/v1/clientes", json={
        "nombre": "Primero", "email": "Comercial@Empresa.test",
    }, headers=headers)
    assert first.status_code == 201, first.text

    # Simulates a concurrent pre-check which saw no conflicting row.
    monkeypatch.setattr(repo, "email_exists", lambda *args, **kwargs: False)
    duplicate = http.post("/api/v1/clientes", json={
        "nombre": "Segundo", "email": "COMERCIAL@EMPRESA.TEST",
    }, headers=headers)
    assert duplicate.status_code == 409, duplicate.text

    with context["factory"]() as db:
        matching = list(db.scalars(select(Client).where(
            Client.email == "comercial@empresa.test",
        )))
        assert len(matching) == 1
        events = list(db.scalars(select(Audit).where(
            Audit.entidad == "CLIENTE",
        )))
        assert sorted(event.resultado for event in events) == ["EXITOSO", "FALLIDO"]


def test_client_email_can_be_absent_for_multiple_clients(context):
    http, headers = context["client"], context["operator"]
    for name in ("Sin correo A", "Sin correo B"):
        response = http.post("/api/v1/clientes", json={"nombre": name}, headers=headers)
        assert response.status_code == 201, response.text

    with context["factory"]() as db:
        assert len(list(db.scalars(select(Client).where(Client.email.is_(None))))) >= 2
