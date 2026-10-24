[← Volver al README](../../README.md)

# Checklist de validación — Pre-Sprint 3

**Versión del proyecto:** 1.2.4 · **Rama:** `Pre-Sprint-3` · **Fecha:** 24/10/2026.

Este registro distingue **implementación técnica en la rama** de **aceptación formal**. Cada control de CI debe comprobarse nuevamente en el commit definitivo.

## Entregables y código

- [x] Conservar los 13 documentos de Inicio sin modificar los hechos históricos.
- [x] Incorporar el presupuesto como cuarto entregable de Planificación; seguimiento Jira en Anexos.
- [x] Agrupar informes en carpetas Sprint 1, Sprint 2 y Pre-Sprint 3; documentar las modificaciones globales en [Versión 1.2.4](../Versiones/1.2.4.md).
- [x] Centralizar diagramas de API y C4 en `docs/Arquitectura/`.
- [x] Incorporar migraciones explícitas Alembic e índice de unicidad de correo del cliente.
- [x] Añadir pruebas de rollback, auditoría y salvaguarda de bases de prueba.
- [x] Separar frontend en `pages/`, `forms/`, `components/` y `styles/` sin añadir historias futuras.
- [x] Preparar workflows de CI, CodeQL y auditoría de dependencias.
- [x] Preparar configuración de staging aislado sin presentar un despliegue externo como hecho.
- [x] Crear [matriz BDD](<01 Matriz de pruebas BDD.md>) de US-001 a US-015.

## Verificaciones automáticas

- [x] [CI de Pre-Sprint 3](https://github.com/RodrigoAC12/Ecolog-stica_Lima/actions/runs/40141894546): 27 pruebas backend tanto en SQLite como en PostgreSQL 16, cobertura del 92,85 %, 6 pruebas frontend, build, migraciones Alembic, Docker y enlaces.
- [x] [Auditoría de dependencias](https://github.com/RodrigoAC12/Ecolog-stica_Lima/actions/runs/40141894558) aprobada.
- [x] [CodeQL Python/TypeScript](https://github.com/RodrigoAC12/Ecolog-stica_Lima/actions/runs/40141894532) aprobado con los análisis SARIF exportados.
- [ ] Realizar triage humano de las alertas visibles en el panel Code Scanning, si las hubiera; un workflow verde no certifica que no exista ningún riesgo.
- [x] Validación automática de enlaces locales Markdown aprobada durante el CI de Pre-Sprint 3.

## Validaciones formales pendientes

- [ ] Aprobación presupuestal y del contenido académico por el equipo/docente.
- [ ] Prueba de staging real con DNS válido, certificado HTTPS/TLS y secretos gestionados fuera del repositorio.
- [ ] Pruebas manuales de accesibilidad WCAG, 360 px, teclado y navegadores soportados.
- [ ] Demostración y aceptación de los escenarios oficiales Gherkin por interesados.
- [ ] Revisión independiente del código y aprobación del Pull Request por el propietario.
- [ ] Confirmación de responsables, estado de sprints y ceremonias reales en Jira; no inventar reuniones ni fechas.

**Referencias:** [Informe de seguridad](<../03 Implementación/Pre-Sprint 3/02 Informe de seguridad V_1_0_0.md>), [Integridad y auditoría](<../03 Implementación/Pre-Sprint 3/03 Informe de integridad y auditoría V_1_0_0.md>) y [Versión 1.2.4](../Versiones/1.2.4.md).
