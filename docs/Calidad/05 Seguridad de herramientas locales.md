[← Volver al README](../../README.md)

# Seguridad de las herramientas locales — Sprint 3

**Versión documental:** 1.0.0 · **Proyecto:** 1.3.0 · **Fecha:** 25/10/2026 (Lima).<br>
**Responsable:** Jhon Robert Paitan Montes; apoyo de Rodrigo Vladimir Arce Curi.

## Hallazgos y correcciones

El [corte inicial de CodeQL](<../03 Implementación/Sprint 03/evidencias/codeql-herramientas-inicial.json>) registra tres alertas abiertas en herramientas locales, aunque el workflow terminaba correctamente. Se distinguen de los cero hallazgos del análisis Sonar, cuyo alcance se concentra en el código de la aplicación.

| Alerta | Severidad del analizador | Alcance y corrección aplicada | Verificación local |
|---|---|---|---|
| #1, `py/clear-text-storage-sensitive-data` | Alta | El preparador escribía credenciales en un `.env` fuera del repositorio. Ahora guarda `staging.settings.dpapi` cifrado para la cuenta de Windows; Compose recibe los valores descifrados en memoria. La migración conserva todos los valores y retira el archivo de texto únicamente después de verificar el cifrado. | Cuatro pruebas de integración DPAPI aprobadas; configuración existente migrada sin rotación de claves ni cambios de datos; `config --quiet` y operación de Compose comprobados. |
| #2, `py/insecure-protocol` | Alta | El comprobador dependía de los valores predeterminados de `ssl.create_default_context`. Se fija expresamente `minimum_version = TLSv1_2`, conservando validación de cadena y hostname. La alerta no acredita que la conexión anterior negociase TLS antiguo. | Comprobación HTTPS sobre la CA local y versión TLS realmente negociada en la evidencia de staging. |
| #3, `js/http-to-file-access` | Media | El nombre del video se construía a partir de la versión recibida por HTTP. Ahora utiliza la versión local validada del paquete; la respuesta de la API solo se compara con ella. | Auditoría Edge repetida: 13 estados, 16 comprobaciones dirigidas, 437 comprobaciones de contraste, sin infracciones ni resultados incompletos sobre contenido funcional. |

La comprobación de login inválido espera la pantalla de acceso y verifica HTTP 401 antes de evaluar su alerta; evita rellenar un campo de correo de la pantalla anterior durante el cambio de vista.

Las [pruebas de configuración protegida](<../03 Implementación/Sprint 03/evidencias/configuracion-protegida-1.3.0.json>), el [nuevo recorrido de interfaz](<../03 Implementación/Sprint 03/evidencias/accesibilidad-cierre-herramientas.json>) y la [verificación HTTPS](<../03 Implementación/Sprint 03/evidencias/staging-local.json>) conservan los resultados sin credenciales.

## Protección de configuración

El [módulo de configuración](../../scripts/local_staging_settings.py) utiliza DPAPI sin solicitar diálogos y libera la memoria asignada por Windows. Las pruebas comprueban recuperación exacta, ausencia del secreto en el archivo cifrado, rechazo de contenido alterado y conservación de credenciales existentes sin mostrarlas. No se afirma protección frente a un proceso que ya controle la misma cuenta de Windows.

El [administrador de staging](../../scripts/manage_local_staging.py) entrega los valores al proceso Compose mediante variables de entorno y exige `config --quiet` para no mostrar la configuración. El archivo de texto anterior ya no es el procedimiento vigente; consultar la [guía actualizada](<../Despliegue/Guía de staging.md>).

La [API de protección de datos de Microsoft](https://learn.microsoft.com/en-us/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) documenta el ámbito de usuario y la comprobación de integridad. El archivo protegido se excluye de Git y el procedimiento no exporta una clave de descifrado al repositorio.

## Repetición y cierre

```powershell
& .venv/Scripts/python.exe -m unittest discover -s scripts -p test_local_staging_settings.py -v
& .venv/Scripts/python.exe scripts/prepare_local_staging.py
& .venv/Scripts/python.exe scripts/manage_local_staging.py config --quiet
& .venv/Scripts/python.exe scripts/verify_local_staging.py
node scripts/audit_accessibility.mjs cierre-herramientas edge
```

El cierre de las alertas debe verificarse en el nuevo análisis de CodeQL de `Sprint-3`; no se descartan alertas manualmente ni se modifica su severidad para obtener un resultado favorable. Las auditorías evalúan su alcance concreto y la revisión del cliente o del usuario permanece pendiente.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 25/10/2026 | Tres hallazgos de herramientas, correcciones y validaciones de cifrado, TLS y auditoría de interfaz. |

[← Volver al README](../../README.md)
