[← Volver al README](../../README.md)

# Guía de staging local — EcoLogística Lima

**Versión documental:** 1.0.1 · **Actualizado:** 25/10/2026 (Lima).

El entorno se ejecuta exclusivamente en localhost. Docker Compose levanta PostgreSQL, API y frontend compilado detrás de Caddy. Solo el gateway publica puertos, enlazados a 127.0.0.1; la API y la base permanecen en la red interna. No se necesita dominio público ni servidor adicional.

## Preparación

Desde la raíz del repositorio, con Docker Desktop activo:

```powershell
& .venv/Scripts/python.exe scripts/prepare_local_staging.py
$localEnvironment = Join-Path $env:LOCALAPPDATA 'EcoLogistica/staging.env'
docker compose --project-name ecologistica-staging-local --env-file $localEnvironment -f docker-compose.staging.yml config --quiet
docker compose --project-name ecologistica-staging-local --env-file $localEnvironment -f docker-compose.staging.yml up -d --build --wait
```

El preparador genera una configuración privada fuera del repositorio y no sobrescribe una existente. Allí se encuentran la cuenta local y sus credenciales. No publicar ese archivo ni imprimir la configuración Compose expandida. La plantilla versionada contiene únicamente valores de ejemplo.

## Acceso

- Aplicación local: [http://localhost:8080](http://localhost:8080).
- Aplicación con TLS local: [https://localhost:8443](https://localhost:8443).
- Salud de API por TLS: [https://localhost:8443/health](https://localhost:8443/health).

Caddy utiliza una CA interna para localhost. La confianza del navegador se administra por separado; no se modifica automáticamente el almacén de certificados de Windows. El acceso HTTP está limitado a la interfaz local. La comprobación TLS valida la cadena y el nombre del certificado mediante la CA seleccionada, sin desactivar la verificación.

## Verificación

Copiar únicamente el certificado público y ejecutar el comprobador:

```powershell
$localEnvironment = Join-Path $env:LOCALAPPDATA 'EcoLogistica/staging.env'
$localAuthority = Join-Path $env:LOCALAPPDATA 'EcoLogistica/localhost-root.crt'
docker compose --project-name ecologistica-staging-local --env-file $localEnvironment -f docker-compose.staging.yml cp gateway:/data/caddy/pki/authorities/local/root.crt $localAuthority
& .venv/Scripts/python.exe scripts/verify_local_staging.py
```

Se verifica frontend HTTP/HTTPS, salud, cabeceras, rechazo sin autenticación, login y lectura de cuatro recursos protegidos. Los resultados sin tokens ni contraseñas se conservan en [staging-local.json](<../03 Implementación/Sprint 03/evidencias/staging-local.json>). Las migraciones deben indicar la revisión 0002_clients_email_unique al consultar Alembic dentro del backend.

## Operación

Los volúmenes persistentes pertenecen al proyecto Compose ecologistica-staging-local. Para detenerlo conservando datos:

```powershell
docker compose --project-name ecologistica-staging-local --env-file $localEnvironment -f docker-compose.staging.yml down
```

No utilizar down -v para una parada normal. Antes de migrar datos existentes, respaldarlos y revisar duplicados de correo. La validación local no acredita operación remota ni aprobación funcional de interesados.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 24/10/2026 | Configuración inicial de staging. |
| 1.0.1 | 25/10/2026 | Alcance localhost, acceso loopback y verificación TLS con CA local. |
