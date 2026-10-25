[← Volver al README](../../README.md)

# Guía de staging local — EcoLogística Lima

**Versión documental:** 1.0.2 · **Actualizado:** 25/10/2026 (Lima).

El entorno se ejecuta exclusivamente en localhost. Docker Compose levanta PostgreSQL, API y frontend compilado detrás de Caddy. Solo el gateway publica puertos, enlazados a 127.0.0.1; la API y la base permanecen en la red interna. No se necesita dominio público ni servidor adicional.

## Preparación

Desde la raíz del repositorio, con Docker Desktop activo:

```powershell
& .venv/Scripts/python.exe scripts/prepare_local_staging.py
& .venv/Scripts/python.exe scripts/manage_local_staging.py config --quiet
& .venv/Scripts/python.exe scripts/manage_local_staging.py up -d --build --wait
```

El preparador conserva las credenciales existentes y almacena la configuración cifrada con DPAPI en `%LOCALAPPDATA%/EcoLogistica/staging.settings.dpapi`, fuera del repositorio. Si encuentra el archivo anterior `staging.env`, cifra sus valores, verifica que pueden recuperarse sin cambios y retira únicamente ese archivo de texto después de comprobar la migración.

El administrador descifra los valores en memoria y los entrega al proceso Compose mediante su entorno; no genera otro archivo de contraseñas. `config` exige `--quiet` para evitar mostrar la configuración operativa. La plantilla versionada contiene únicamente valores de ejemplo. La protección corresponde al usuario de Windows: copiar el archivo a otra cuenta no constituye un procedimiento de recuperación; conservar el perfil y planificar la recuperación de credenciales con el responsable técnico. [Referencia de Microsoft](https://learn.microsoft.com/en-us/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata).

## Acceso

- Aplicación local: [http://localhost:8080](http://localhost:8080).
- Aplicación con TLS local: [https://localhost:8443](https://localhost:8443).
- Salud de API por TLS: [https://localhost:8443/health](https://localhost:8443/health).

Caddy utiliza una CA interna para localhost. La confianza del navegador se administra por separado; no se modifica automáticamente el almacén de certificados de Windows. El acceso HTTP está limitado a la interfaz local. La comprobación TLS valida la cadena y el nombre del certificado mediante la CA seleccionada, exige como mínimo TLS 1.2 y comprueba la versión realmente negociada, sin desactivar la verificación.

## Verificación

Copiar únicamente el certificado público y ejecutar el comprobador:

```powershell
$localAuthority = Join-Path $env:LOCALAPPDATA 'EcoLogistica/localhost-root.crt'
& .venv/Scripts/python.exe scripts/manage_local_staging.py cp gateway:/data/caddy/pki/authorities/local/root.crt $localAuthority
& .venv/Scripts/python.exe scripts/verify_local_staging.py
```

Se verifica frontend HTTP/HTTPS, salud, cabeceras, rechazo sin autenticación, login y lectura de cuatro recursos protegidos. Los resultados sin tokens ni contraseñas se conservan en [staging-local.json](<../03 Implementación/Sprint 03/evidencias/staging-local.json>). Las migraciones deben indicar la revisión 0002_clients_email_unique al consultar Alembic dentro del backend.

## Operación

Los volúmenes persistentes pertenecen al proyecto Compose ecologistica-staging-local. Para detenerlo conservando datos:

```powershell
& .venv/Scripts/python.exe scripts/manage_local_staging.py down
```

No utilizar down -v para una parada normal. Antes de migrar datos existentes, respaldarlos y revisar duplicados de correo. La validación local no acredita operación remota ni aprobación funcional de interesados.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 24/10/2026 | Configuración inicial de staging. |
| 1.0.1 | 25/10/2026 | Alcance localhost, acceso loopback y verificación TLS con CA local. |
| 1.0.2 | 25/10/2026 | Secretos cifrados con DPAPI, migración comprobada, Compose con variables en memoria y TLS mínimo explícito. |
