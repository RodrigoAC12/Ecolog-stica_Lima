import secrets

from local_staging_settings import load_settings, save_settings, settings_directory


def prepare() -> None:
    directory = settings_directory()
    directory.mkdir(parents=True, exist_ok=True)
    if (directory / "staging.settings.dpapi").exists() or (directory / "staging.env").exists():
        load_settings(directory)
        print("Se conserva la configuración existente, protegida con DPAPI de Windows")
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
    save_settings(values, directory)
    print("Configuración privada creada y protegida con DPAPI de Windows")


if __name__ == "__main__":
    prepare()
