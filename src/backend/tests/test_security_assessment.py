from datetime import datetime, timedelta, timezone

import jwt
import pytest
from sqlalchemy import select

from app.core.config import settings
from app.core.security import hash_password, verify_password
from app.models import User


@pytest.mark.parametrize("resource", ["vehiculos", "pedidos", "conductores", "clientes"])
def test_resource_permissions_reject_unauthenticated_and_read_only_writes(context, resource):
    client = context["client"]
    endpoint = f"/api/v1/{resource}"
    assert client.get(endpoint).status_code == 401
    assert client.get(endpoint, headers=context["auditor"]).status_code == 200
    assert client.post(endpoint, json={}, headers=context["auditor"]).status_code == 403


@pytest.mark.parametrize("token_case", ["missing_expiration", "expired", "unsigned"])
def test_rejects_tokens_without_valid_expiration_and_signature(context, token_case):
    with context["factory"]() as database:
        operator = database.scalar(select(User).where(User.email == "op@example.test"))
        subject = str(operator.usuario_id)
    payload = {"sub": subject}
    if token_case == "expired":
        payload["exp"] = datetime.now(timezone.utc) - timedelta(seconds=1)
    if token_case == "unsigned":
        payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=1)
        token = jwt.encode(payload, key=None, algorithm="none")
    else:
        token = jwt.encode(payload, settings.jwt_secret, algorithm="HS256")
    response = context["client"].get(
        "/api/v1/vehiculos", headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 401


def test_login_does_not_interpret_sql_in_input(context):
    response = context["client"].post(
        "/api/v1/auth/login",
        json={"email": "' OR 1=1 --", "password": "invalid-password"},
    )
    assert response.status_code == 401
    assert "access_token" not in response.json()


def test_password_hashes_use_random_salts_and_reject_invalid_credentials():
    password = "password-for-isolated-security-test"
    first_hash = hash_password(password)
    second_hash = hash_password(password)
    assert first_hash != second_hash
    assert password not in first_hash
    assert verify_password(password, first_hash)
    assert not verify_password("different-password", first_hash)
    assert not verify_password(password, "invalid-encoded-value")
