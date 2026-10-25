[← Volver al README](../../../../README.md)

# Informe de integridad transaccional y auditoría

> Antecedente histórico de la base 1.2.4, integrado documentalmente al Sprint 3 el 25/10/2026. Se conservan las fechas, resultados y límites del corte original. La entrega vigente es [Sprint 3 — versión 1.3.0](<../../../Versiones/1.3.0.md>), con [evaluaciones y alcance actuales](<../Matriz de entrega y rúbrica V_1_0_0.md>).

**Versión documental:** 1.0.1 · **Versión del proyecto:** 1.2.4 · **Corte histórico:** 24/10/2026.

## Criterio técnico

Las modificaciones de entidades y su auditoría de éxito comparten una transacción. Si falla la escritura de auditoría, se revierte la entidad. Los intentos HTTP rechazados se registran por separado sin crear datos del negocio.

## Pruebas reproducibles

| Caso | Archivo de prueba | Comportamiento esperado |
|---|---|---|
| Fallo forzado al registrar auditoría de una alta | `src/backend/tests/test_transaction_audit.py` | No se persisten vehículo ni auditoría de éxito |
| Fallo al actualizar un vehículo | `src/backend/tests/test_transaction_audit.py` | La lectura posterior conserva el estado previo |
| Escrituras HTTP rechazadas 403/422 | `src/backend/tests/test_transaction_audit.py` | Sin entidad nueva y con eventos `FALLIDO` |
| Validación de bases de pruebas | `src/backend/tests/test_database_safety.py` | Rechazar URLs no destinadas a pruebas |
| Correo de cliente duplicado con validación previa obsoleta | `src/backend/tests/test_client_email_uniqueness.py` | Restricción de base de datos y respuesta 409 |

La suite se ejecuta en SQLite efímero y PostgreSQL 16 aislado dentro de [GitHub Actions](https://github.com/RodrigoAC12/Ecolog-stica_Lima/actions?query=branch%3APre-Sprint-3). Los resultados y cobertura deben asociarse al commit definitivo.

## Esquema y migraciones

- `0001_sprint1.py`: DDL explícito del esquema inicial; no depende de `Base.metadata.create_all()` sobre modelos que pueden evolucionar.
- `0002_clients_email_unique.py`: índice único para el correo de clientes sin distinción de mayúsculas; antes de aplicarlo revisa duplicados existentes y se detiene sin borrarlos.
- CI PostgreSQL: `alembic upgrade head`, `alembic current` y `alembic check` en una base aislada.

**Precaución:** nunca aplicar el fixture de tests a una base con datos reales. Para actualizar una base preexistente, hacer copia de seguridad, inspeccionar colisiones y ejecutar migraciones siguiendo la política aprobada de despliegue.

## Límites de aceptación

Los tests documentan casos concretos, no una prueba exhaustiva de todas las concurrencias. La aprobación formal del DoD requiere revisión independiente y verificación de los escenarios oficiales; también quedan pendientes las pruebas de staging y UI por personas responsables.

**Relacionados:** [Informe de seguridad](<02 Informe de seguridad V_1_0_0.md>) · [Matriz BDD](<../../../Calidad/01 Matriz de pruebas BDD.md>) · [Versión 1.2.4](<../../../Versiones/1.2.4.md>).

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.1 | 25/10/2026 | Integración de antecedentes en Sprint 03, retiro de la etapa separada y enlaces actualizados. |
