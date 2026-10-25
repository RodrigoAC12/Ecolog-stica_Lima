[← Volver al README](../../../../README.md)

# Informe de la base técnica 1.2.4

> Antecedente histórico de la base 1.2.4, integrado documentalmente al Sprint 3 el 25/10/2026. Se conservan las fechas, resultados y límites del corte original. La entrega vigente es [Sprint 3 — versión 1.3.0](<../../../Versiones/1.3.0.md>), con [evaluaciones y alcance actuales](<../Matriz de entrega y rúbrica V_1_0_0.md>).

**Versión documental:** 1.0.1 · **Versión del proyecto:** 1.2.4 · **Fecha:** 24/10/2026 · **Rama:** `Pre-Sprint-3`.

## Propósito

Completar la documentación de Planificación y preparar un incremento verificable de las funcionalidades US-001 a US-015, sin modificar el alcance del Sprint 3. Conservar las fechas y el contenido de los documentos históricos de los Sprints 1 y 2.

## Organización documental

- Inicio: 13 documentos de definición del proyecto.
- Planificación: transformación ágil, artefactos Jira, registro de riesgos y presupuesto como **cuarto entregable**. El seguimiento del Sprint 2 se mantiene como anexo.
- Implementación: [Sprint 1](<../../Sprint 1>), [Sprint 2](<../../Sprint 2>) y los antecedentes de la base 1.2.4 integrados en Sprint 03, cada uno con material diferenciable.
- Referencias técnicas: arquitectura, pruebas y despliegue en carpetas dedicadas dentro de `docs/`.

## Trabajo técnico

1. Backend FastAPI: salvaguarda de base de datos de pruebas; rollback transaccional y auditoría de intentos rechazados.
2. PostgreSQL/Alembic: esquema inicial con DDL explícito y revisión incremental de unicidad de correos; no se eliminan datos duplicados automáticamente.
3. Frontend: las vistas operativas y sus formularios se presentan desde componentes separados, sin modificar rutas de API ni comportamiento de negocio previsto.
4. Seguridad: CodeQL Python/TypeScript, auditoría de dependencias y control automatizado de calidad.
5. Staging: imagen estática de frontend y gateway HTTPS configurado; desplegarlo requiere infraestructura externa.

## Situación respecto de los sprints anteriores

Los informes originales registran los cortes del 29/09 y 06/10/2026. El estado técnico actual del repositorio y los registros Jira posteriores se distinguen en [Estado de Sprints 1 y 2](<04 Estado de Sprints 1 y 2 V_1_0_0.md>). La ejecución de CI no demuestra retrospectivamente que hayan tenido lugar la Sprint Review, la retrospectiva ni una aceptación BDD.

## Criterios de entrega

- Ejecutar los controles de GitHub Actions de la rama definitiva.
- Comprobar enlaces locales tras la organización documental y tipado de la interfaz.
- Documentar los resultados en [Versión 1.2.4](<../../../Versiones/1.2.4.md>) y [Checklist de validación](<../../../Calidad/02 Checklist de validación.md>).
- Presentar **una sola entrega** al propietario, con revisión independiente antes del merge.

Los resultados técnicos son diferentes de las aprobaciones de personas y del estado administrativo de Jira.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.1 | 25/10/2026 | Integración de antecedentes en Sprint 03, retiro de la etapa separada y enlaces actualizados. |
