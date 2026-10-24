"""Enforce case-insensitive uniqueness of client email without removing existing records.

Applies to existing databases; the initial metadata-backed bootstrap may already
include the new index on a pristine database. Check presence before creating it.
"""

from alembic import op
import sqlalchemy as sa

revision = "0002_clients_email_unique"
down_revision = "0001_sprint1"
branch_labels = None
depends_on = None

INDEX_NAME = "uq_clientes_email_normalized"


def upgrade() -> None:
    bind = op.get_bind()
    duplicates = bind.execute(sa.text("""
        SELECT lower(email) AS email_key, count(*) AS total
        FROM clientes
        WHERE email IS NOT NULL
        GROUP BY lower(email)
        HAVING count(*) > 1
    """)).fetchall()
    if duplicates:
        raise RuntimeError(
            "Existing duplicate client emails must be reconciled by the team "
            "before applying 0002; no records were deleted automatically."
        )
    existing = {index["name"] for index in sa.inspect(bind).get_indexes("clientes")}
    if INDEX_NAME not in existing:
        op.create_index(
            INDEX_NAME,
            "clientes",
            [sa.text("lower(email)")],
            unique=True,
        )


def downgrade() -> None:
    bind = op.get_bind()
    existing = {index["name"] for index in sa.inspect(bind).get_indexes("clientes")}
    if INDEX_NAME in existing:
        op.drop_index(INDEX_NAME, table_name="clientes")
