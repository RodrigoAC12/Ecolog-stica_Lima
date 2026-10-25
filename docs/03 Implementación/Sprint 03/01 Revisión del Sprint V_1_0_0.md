[← Volver al README](../../../README.md)

# Revisión del sprint

**Nombre del Proyecto:** EcoLogística Lima<br>
**Líder del Proyecto:** Marco Jhair Martinez Llanos, según el acta de constitución.<br>
**Sprint:** 3 — Calidad, seguridad, accesibilidad y mantenibilidad.<br>
**Versión documental:** V_1_0_0 · **Fecha de corte:** 24/10/2026 (Lima).<br>
**Rama de entrega:** `Sprint-3`.

## Historias de Usuario completadas en este Sprint

El incremento se concentra en trabajo transversal sobre US-001 a US-015. Estas funcionalidades proceden de los Sprints 1 y 2; no se presentan como historias nuevas completadas en Sprint 3. Las tareas técnicas verificadas son:

| Trabajo del incremento | Resultado comprobado | Trazabilidad |
|---|---|---|
| Evaluación y corrección estática | Cuatro botones de formularios con tipo de envío explícito; hallazgos S9011 corregidos | ECO-53 y [calidad de código](<03 Calidad de código V_1_0_0.md>) |
| Seguridad de autenticación | JWT sin `exp` rechazado; firma y caducidad probadas | ECO-54 y [OWASP](<04 OWASP V_1_0_0.md>) |
| Acceso y persistencia | 36 pruebas backend aprobadas sobre SQLite y PostgreSQL aislados; migraciones sin deriva | ECO-54, DoD-03/09 y evidencia técnica |
| Interfaz accesible | Foco gestionado al cambiar de vista; controles multilínea coherentes; 13 estados evaluados | ECO-55 y [WCAG](<05 WCAG V_1_0_0.md>) |
| Regresión frontend | Siete pruebas y compilación aprobadas | ECO-53/55 y DoD-01/03 |
| Organización y documentación | Backend/frontend separados; resultados generados excluidos; cinco informes y adenda de planificación | ECO-56/57/58 |

Las pruebas técnicas verifican comportamientos concretos. La declaración formal de Done requiere revisión independiente y aceptación de los criterios aplicables; no se equipara la ejecución local al cierre administrativo de Jira.

## Demostración del trabajo completado

El recorrido de demostración permite presentar el login, el inicio y las pantallas de vehículos, pedidos, conductores y clientes. Se utiliza la aplicación real con API FastAPI y una base exclusiva de auditoría. La evidencia permite reproducir los siguientes puntos:

1. Acceso por teclado al contenido y rechazo visible de credenciales incorrectas.
2. Navegación entre módulos con el foco ubicado en el contenido principal.
3. Formularios y listados a 1.440 y 360 px; comprobación adicional de clientes a 320 px.
4. Controles de seguridad, pruebas de regresión y correcciones verificadas por SonarQube.
5. Informes y resultados antes/después, con enlaces a las evidencias.

| Evidencia del recorrido | Ubicación |
|---|---|
| Resultado automatizado y comprobaciones de teclado | [accesibilidad-final.json](evidencias/accesibilidad-final.json) |
| Captura de login | [Login 360 px](evidencias/final-login-360.png) |
| Captura de conductores | [Conductores 360 px](evidencias/final-conductores-360.png) |
| Captura de clientes | [Clientes 360 px](evidencias/final-clientes-360.png) |
| Pruebas sobre PostgreSQL | [backend-postgres.xml](evidencias/backend-postgres.xml) |

La revisión con interesados debe registrar sus observaciones y aceptación sobre este incremento. Este documento conserva los resultados del recorrido técnico y no atribuye asistentes o aprobaciones no registrados.

## Pendientes

| Pendiente | Acción de cierre | Responsable |
|---|---|---|
| Revisión del incremento | Revisar PR y evidencias; registrar observaciones | Par técnico distinto del autor, por confirmar |
| Aceptación de interesados | Validar escenarios oficiales y documentar resultado | Líder e interesados |
| Contraste y tecnología de asistencia | Completar las verificaciones WCAG no resueltas automáticamente | Equipo de calidad/UX, por asignar |
| Seguridad operativa | TLS real, limitación de intentos y alertas/retención de auditoría | Equipo técnico, por asignar |
| Conciliación Jira | Regularizar fechas y responsables con decisiones reales; conservar ECO-18 en revisión mientras corresponda | Líder y equipo |
| Integración | Publicar y revisar la rama; comprobar CI y obtener aprobación del propietario | Equipo y propietario del repositorio |

No se incluyen en esta entrega US-016 a US-023: optimización, reoptimización, mapa, indicadores y sostenibilidad funcional continúan en su backlog.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| V_1_0_0 | 24/10/2026 | Revisión del incremento técnico, recorrido reproducible y pendientes de aceptación. |

[← Volver al README](../../../README.md)
