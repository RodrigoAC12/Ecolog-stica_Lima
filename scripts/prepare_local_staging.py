import os
import secrets
from pathlib import Path


def prepare() -> None:
    directory = Path(os.environ["LOCALAPPDATA"]) / "EcoLogistica"
    directory.mkdir(parents=True, exist_ok=True)
    destination = directory / "staging.env"
    if destination.exists():
        print(f"Se conserva la configuración existente: {destination}")
        return
    database_password = secrets.token_hex(24)
    values = {
        "STAGING_DOMAIN": "localhost",
        "STAGING_HTTP_PORT": "8080",
        "STAGING_HTTPS_PORT": "8443",
        "POSTGRES_DB": "ecologistica_staging_local",
        "POSTGRES_USER": "ecologistica_local",
        "POSTGRES_PASSWORD": database_password,
        "DATABASE_URL": f"postgresql+psycopg://ecologistica_local:{database_password}@db:5432/ecologistica_staging_local",
        "JWT_SECRET": secrets.token_hex(48),
        "BOOTSTRAP_OPERATOR_EMAIL": "operador.local@example.test",
        "BOOTSTRAP_OPERATOR_PASSWORD": secrets.token_urlsafe(24),
    }
    with destination.open("x", encoding="utf-8") as configuration:
        configuration.write("\n".join(f"{name}={value}" for name, value in values.items()) + "\n")
    print(f"Configuración privada creada: {destination}")


if __name__ == "__main__":
    prepare()
