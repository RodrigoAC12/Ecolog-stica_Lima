[← Volver al README](../../../README.md)

# Informe de preparación del Pre-Sprint 3

**Versión documental:** 1.0.0 · **Versión del proyecto:** 1.2.4 · **Fecha:** 24/10/2026 · **Rama:** `Pre-Sprint-3`.

## Propósito

Completar la documentación de Planificación y preparar un incremento verificable de las funcionalidades US-001 a US-015, sin modificar el alcance del Sprint 3. Conservar las fechas y el contenido de los documentos históricos de los Sprints 1 y 2.

## Organización académica

- Inicio: 13 documentos de definición del proyecto.
- Planificación: transformación ágil, artefactos Jira, registro de riesgos y presupuesto como **cuarto entregable**. El seguimiento del Sprint 2 se mantiene como anexo.
- Implementación: [Sprint 1](../Sprint%201/), [Sprint 2](../Sprint%202/) y Pre-Sprint 3, cada uno con material diferenciable.
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
- Documentar los resultados en [Versión 1.2.4](<../../Versiones/1.2.4.md>) y [Checklist de validación](<../../Calidad/02 Checklist de validación.md>).
- Presentar **una sola entrega** al propietario, con revisión independiente antes del merge.

Los resultados técnicos son diferentes de las aprobaciones de personas y del estado administrativo de Jira.
