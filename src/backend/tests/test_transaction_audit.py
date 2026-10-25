"""Evidence for DoD-09: entity and successful audit must commit atomically.

These tests execute with SQLite by default and with the isolated PostgreSQL
service in GitHub Actions.  No production database is ever used.
"""
from decimal import Decimal
from uuid import uuid4

import pytest
from sqlalchemy import event, select

from app.models import Audit, User, Vehicle
from app.services.common import commit_change


def _vehicle(plate: str) -> Vehicle:
    return Vehicle(
        vehiculo_id=uuid4(),
        placa=plate,
        marca="Toyota",
        modelo="Hiace",
        capacidad_kg=Decimal("1200.00"),
        capacidad_m3=Decimal("8.00"),
        estado="DISPONIBLE",
    )


def _reject_successful_audit(mapper, connection, target) -> None:
    if target.resultado == "EXITOSO":
        raise RuntimeError("Fallo simulado al persistir la auditoría")


def test_new_entity_is_rolled_back_if_success_audit_fails(context):
    factory = context["factory"]
    with factory() as db:
        operator = db.scalar(select(User).where(User.email == "op@example.test"))
        vehicle = _vehicle("TXN-001")
        event.listen(Audit, "before_insert", _reject_successful_audit)
        try:
            with pytest.raises(RuntimeError, match="Fallo simulado"):
                commit_change(
                    db, operator, vehicle, "VEHICULO", "REGISTRAR",
                    vehicle.vehiculo_id,
                )
        finally:
            event.remove(Audit, "before_insert", _reject_successful_audit)

    with factory() as db:
        assert db.scalar(select(Vehicle).where(Vehicle.placa == "TXN-001")) is None
        assert list(db.scalars(select(Audit).where(Audit.entidad == "VEHICULO"))) == []


def test_update_is_rolled_back_if_success_audit_fails(context):
    factory = context["factory"]
    existing = _vehicle("TXN-002")
    with factory() as db:
        db.add(existing)
        db.commit()
        vehicle_id = existing.vehiculo_id

    with factory() as db:
        operator = db.scalar(select(User).where(User.email == "op@example.test"))
        vehicle = db.get(Vehicle, vehicle_id)
        vehicle.estado = "MANTENIMIENTO"
        event.listen(Audit, "before_insert", _reject_successful_audit)
        try:
            with pytest.raises(RuntimeError, match="Fallo simulado"):
                commit_change(
                    db, operator, vehicle, "VEHICULO", "ACTUALIZAR",
                    vehicle_id,
                )
        finally:
            event.remove(Audit, "before_insert", _reject_successful_audit)

    with factory() as db:
        assert db.get(Vehicle, vehicle_id).estado == "DISPONIBLE"
        assert list(db.scalars(select(Audit).where(Audit.entidad == "VEHICULO"))) == []


def test_rejected_api_write_is_logged_separately_without_domain_change(context, vehicle_data):
    client = context["client"]
    operator = context["operator"]
    auditor = context["auditor"]

    assert client.post("/api/v1/vehiculos", json=vehicle_data, headers=auditor).status_code == 403
    assert client.post(
        "/api/v1/vehiculos",
        json={**vehicle_data, "capacidad_kg": "0"},
        headers=operator,
    ).status_code == 422

    with context["factory"]() as db:
        assert list(db.scalars(select(Vehicle))) == []
        failed = list(db.scalars(select(Audit).where(
            Audit.entidad == "VEHICULO", Audit.resultado == "FALLIDO",
        )))
        assert sorted(a.detalle["status"] for a in failed) == [403, 422]
        assert all(a.accion == "POST" and a.usuario_id is not None for a in failed)
