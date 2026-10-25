[← Volver al README](../../README.md)

# Matriz de pruebas BDD — Sprints 1 y 2

**Versión del proyecto:** 1.2.4 · **Etapa:** Pre-Sprint 3. Los escenarios completos Gherkin se conservan en [Transformando a ágil](<../02 Planificación/01 Transformando a ágil V_1_0_1.md>). La siguiente matriz relaciona cada historia con los tests implementados; no afirma aceptación formal.

| Historia | Alcance | Prueba automatizada relacionada |
|---|---|---|
| US-001 | Registro de vehículos | `test_vehicles.py` |
| US-002 | Consulta de flota | `test_vehicles.py` |
| US-003 | Actualización de vehículos | `test_vehicles.py` |
| US-004 | Desactivación lógica de vehículos | `test_vehicles.py` |
| US-005 | Registro de pedidos | `test_orders.py` |
| US-006 | Consulta y filtros de pedidos | `test_orders.py` |
| US-007 | Edición de pedidos pendientes | `test_orders.py` |
| US-008 | Cancelación de pedidos | `test_orders.py` |
| US-009 | Registro de conductores | `test_drivers.py` |
| US-010 | Consulta de conductores | `test_drivers.py` |
| US-011 | Actualización de conductores | `test_drivers.py` |
| US-012 | Desactivación de conductores | `test_drivers.py` |
| US-013 | Registro de clientes | `test_clients.py`, `test_client_email_uniqueness.py` |
| US-014 | Consulta de clientes | `test_clients.py` |
| US-015 | Actualización de clientes y condiciones de entrega | `test_clients.py`, `test_client_email_uniqueness.py` |

## Controles transversales

- **Integridad y auditoría:** `test_transaction_audit.py`, `test_database_safety.py`, `test_client_email_uniqueness.py`.
- **Autenticación y permisos:** `test_auth.py` y las respuestas HTTP probadas por cada módulo.
- **Frontend:** `src/frontend/src/App.test.tsx` con React Testing Library y mocks de red; incluye enlace de salto por teclado.
- **Entorno:** tests backend con SQLite y PostgreSQL 16 aislado; migraciones, documentación y compilación en [Actions](https://github.com/RodrigoAC12/Ecolog-stica_Lima/actions?query=branch%3APre-Sprint-3).

## Aceptación adicional requerida

- [ ] Ejecutar y aprobar cada escenario oficial Gherkin con el interesado responsable.
- [ ] Documentar sesión o acta de revisión funcional, fecha real y defectos detectados.
- [ ] Verificar accesibilidad WCAG, navegación completa, 360 px y navegadores reales.
- [ ] Confirmar revisión independiente y evidencias de Definition of Done antes de fusionar el cambio.

El resultado de un test unitario o de integración no equivale a la aceptación del escenario completo por los interesados.
