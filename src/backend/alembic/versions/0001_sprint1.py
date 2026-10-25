"""Immutable initial PostgreSQL schema (Sprint 1 and Sprint 2 baseline).

This revision intentionally contains explicit DDL instead of reading current
Base.metadata. Otherwise future model changes would change the meaning of 0001.
Existing databases already at 0001 are not rebuilt by this replacement.
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "0001_sprint1"
down_revision = None
branch_labels = None
depends_on = None

UUID = sa.Uuid(as_uuid=True)
STAMP = sa.DateTime(timezone=True)
NOW = sa.text("CURRENT_TIMESTAMP")
NEW_UUID = sa.text("gen_random_uuid()")


def upgrade() -> None:
    bind = op.get_bind()
    if bind.dialect.name == "postgresql":
        op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")

    op.create_table(
        "roles",
        sa.Column("rol_id", sa.SmallInteger(), primary_key=True, autoincrement=True),
        sa.Column("nombre", sa.String(50), nullable=False, unique=True),
        sa.Column("descripcion", sa.String(255)),
    )
    op.create_table(
        "usuarios",
        sa.Column("usuario_id", UUID, primary_key=True, server_default=NEW_UUID),
        sa.Column("nombre", sa.String(150), nullable=False),
        sa.Column("email", sa.String(255), nullable=False, unique=True),
        sa.Column("password_hash", sa.String(255), nullable=False),
        sa.Column("estado", sa.String(20), nullable=False, server_default=sa.text("'ACTIVO'")),
        sa.Column("creado_en", STAMP, nullable=False, server_default=NOW),
        sa.Column("actualizado_en", STAMP, nullable=False, server_default=NOW),
        sa.CheckConstraint("estado IN ('ACTIVO','INACTIVO','BLOQUEADO')"),
    )
    op.create_index("idx_usuarios_estado", "usuarios", ["estado"])
    op.create_table(
        "usuario_roles",
        sa.Column("usuario_id", UUID, sa.ForeignKey("usuarios.usuario_id"), primary_key=True),
        sa.Column("rol_id", sa.SmallInteger(), sa.ForeignKey("roles.rol_id"), primary_key=True),
        sa.Column("asignado_en", STAMP, nullable=False, server_default=NOW),
    )
    op.create_table(
        "vehiculos",
        sa.Column("vehiculo_id", UUID, primary_key=True, server_default=NEW_UUID),
        sa.Column("placa", sa.String(15), nullable=False, unique=True),
        sa.Column("marca", sa.String(80), nullable=False),
        sa.Column("modelo", sa.String(80), nullable=False),
        sa.Column("capacidad_kg", sa.Numeric(10, 2), nullable=False),
        sa.Column("capacidad_m3", sa.Numeric(10, 2), nullable=False),
        sa.Column("consumo_km_l", sa.Numeric(10, 4)),
        sa.Column("factor_emision_kg_co2_km", sa.Numeric(10, 6)),
        sa.Column("estado", sa.String(20), nullable=False, server_default=sa.text("'DISPONIBLE'")),
        sa.Column("creado_en", STAMP, nullable=False, server_default=NOW),
        sa.Column("actualizado_en", STAMP, nullable=False, server_default=NOW),
        sa.CheckConstraint("capacidad_kg > 0"),
        sa.CheckConstraint("capacidad_m3 > 0"),
        sa.CheckConstraint("consumo_km_l IS NULL OR consumo_km_l > 0"),
        sa.CheckConstraint("factor_emision_kg_co2_km IS NULL OR factor_emision_kg_co2_km >= 0"),
        sa.CheckConstraint("estado IN ('DISPONIBLE','EN_RUTA','MANTENIMIENTO','INACTIVO')"),
    )
    op.create_index("idx_vehiculos_estado", "vehiculos", ["estado"])
    op.create_table(
        "conductores",
        sa.Column("conductor_id", UUID, primary_key=True, server_default=NEW_UUID),
        sa.Column("nombres", sa.String(120), nullable=False),
        sa.Column("apellidos", sa.String(120), nullable=False),
        sa.Column("numero_licencia", sa.String(30), nullable=False, unique=True),
        sa.Column("categoria_licencia", sa.String(20), nullable=False),
        sa.Column("telefono", sa.String(30)),
        sa.Column("experiencia_anios", sa.SmallInteger()),
        sa.Column("estado", sa.String(20), nullable=False, server_default=sa.text("'DISPONIBLE'")),
        sa.Column("creado_en", STAMP, nullable=False, server_default=NOW),
        sa.Column("actualizado_en", STAMP, nullable=False, server_default=NOW),
        sa.CheckConstraint("experiencia_anios IS NULL OR experiencia_anios >= 0"),
        sa.CheckConstraint("estado IN ('DISPONIBLE','ASIGNADO','DESCANSO','INACTIVO')"),
    )
    op.create_index("idx_conductores_estado", "conductores", ["estado"])
    op.create_table(
        "clientes",
        sa.Column("cliente_id", UUID, primary_key=True, server_default=NEW_UUID),
        sa.Column("nombre", sa.String(180), nullable=False),
        sa.Column("telefono", sa.String(30)),
        sa.Column("email", sa.String(255)),
        sa.Column("preferencia_entrega", sa.Text()),
        sa.Column("restriccion_acceso", sa.Text()),
        sa.Column("estado", sa.String(20), nullable=False, server_default=sa.text("'ACTIVO'")),
        sa.Column("creado_en", STAMP, nullable=False, server_default=NOW),
        sa.CheckConstraint("estado IN ('ACTIVO','INACTIVO')"),
    )
    op.create_index("idx_clientes_estado", "clientes", ["estado"])
    op.create_table(
        "pedidos",
        sa.Column("pedido_id", UUID, primary_key=True, server_default=NEW_UUID),
        sa.Column("cliente_id", UUID, sa.ForeignKey("clientes.cliente_id"), nullable=False),
        sa.Column("codigo_pedido", sa.String(40), nullable=False, unique=True),
        sa.Column("direccion_entrega", sa.String(255), nullable=False),
        sa.Column("referencia_entrega", sa.String(255)),
        sa.Column("latitud", sa.Numeric(9, 6), nullable=False),
        sa.Column("longitud", sa.Numeric(9, 6), nullable=False),
        sa.Column("peso_kg", sa.Numeric(10, 2), nullable=False),
        sa.Column("volumen_m3", sa.Numeric(10, 3), nullable=False),
        sa.Column("ventana_inicio", STAMP, nullable=False),
        sa.Column("ventana_fin", STAMP, nullable=False),
        sa.Column("prioridad", sa.String(20), nullable=False, server_default=sa.text("'MEDIA'")),
        sa.Column("tipo_producto", sa.String(80)),
        sa.Column("estado", sa.String(20), nullable=False, server_default=sa.text("'PENDIENTE'")),
        sa.Column("creado_en", STAMP, nullable=False, server_default=NOW),
        sa.Column("actualizado_en", STAMP, nullable=False, server_default=NOW),
        sa.CheckConstraint("latitud BETWEEN -90 AND 90"),
        sa.CheckConstraint("longitud BETWEEN -180 AND 180"),
        sa.CheckConstraint("peso_kg > 0"),
        sa.CheckConstraint("volumen_m3 > 0"),
        sa.CheckConstraint("ventana_inicio < ventana_fin"),
        sa.CheckConstraint("prioridad IN ('ALTA','MEDIA','BAJA')"),
        sa.CheckConstraint("estado IN ('PENDIENTE','PLANIFICADO','EN_RUTA','ENTREGADO','CANCELADO','NO_ASIGNADO')"),
    )
    for name, columns in (
        ("idx_pedidos_cliente", ["cliente_id"]),
        ("idx_pedidos_estado", ["estado"]),
        ("idx_pedidos_prioridad", ["prioridad"]),
        ("idx_pedidos_ventana", ["ventana_inicio", "ventana_fin"]),
        ("idx_pedidos_coordenadas", ["latitud", "longitud"]),
    ):
        op.create_index(name, "pedidos", columns)
    op.create_table(
        "auditoria",
        sa.Column("auditoria_id", UUID, primary_key=True, server_default=NEW_UUID),
        sa.Column("usuario_id", UUID, sa.ForeignKey("usuarios.usuario_id")),
        sa.Column("entidad", sa.String(80), nullable=False),
        sa.Column("entidad_id", UUID),
        sa.Column("accion", sa.String(50), nullable=False),
        sa.Column("resultado", sa.String(20), nullable=False),
        sa.Column("detalle", sa.JSON().with_variant(JSONB(), "postgresql")),
        sa.Column("fecha_evento", STAMP, nullable=False, server_default=NOW),
        sa.CheckConstraint("resultado IN ('EXITOSO','FALLIDO')"),
    )
    op.create_index("idx_auditoria_usuario", "auditoria", ["usuario_id"])
    op.create_index("idx_auditoria_entidad", "auditoria", ["entidad", "entidad_id"])
    op.create_index("idx_auditoria_fecha", "auditoria", ["fecha_evento"])


def downgrade() -> None:
    # DESTRUCTIVE: only for a disposable environment after explicit backup.
    for table in (
        "auditoria",
        "pedidos",
        "usuario_roles",
        "clientes",
        "conductores",
        "vehiculos",
        "usuarios",
        "roles",
    ):
        op.drop_table(table)
