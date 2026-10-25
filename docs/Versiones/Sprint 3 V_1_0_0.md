[← Volver al README](../../README.md)

# Entrega técnica del Sprint 3

**Versión documental:** V_1_0_3 · **Versión del proyecto:** 1.3.0 · **Actualizado:** 25/10/2026 (Lima).<br>
**Base:** versión 1.2.4, commit `da3eef2`.<br>
**Rama:** `Sprint-3`.<br>
**Estado documental:** versión 1.3.0 con evidencias conservadas para revisión.

## Cambios del incremento

| Área | Cambio | Evidencia |
|---|---|---|
| Calidad | Configuración Sonar, XML/LCOV y corrección de cuatro botones | [Informe 03](<../03 Implementación/Sprint 03/03 Calidad de código V_1_0_0.md>) |
| Seguridad | JWT exige expiración y sujeto; nueve pruebas negativas adicionales | [Informe 04](<../03 Implementación/Sprint 03/04 OWASP V_1_0_0.md>) |
| Accesibilidad | Gestión de foco y estilos de controles; auditoría reproducible de 13 estados | [Informe 05](<../03 Implementación/Sprint 03/05 WCAG V_1_0_0.md>) |
| Documentación | Cinco Markdown oficiales, enlaces bidireccionales y adenda EP-06 | [README](../../README.md) y [planificación](<../02 Planificación/Anexos/Planificación Sprint 3 V_1_0_0.md>) |
| CI | Controles al actualizar `main`, `Pre-Sprint-3` y `Sprint-3`; cobertura frontend conservada | `.github/workflows/` |
| Organización | Resultados generados ignorados, evidencia seleccionada conservada | `.gitignore` y `docs/03 Implementación/Sprint 03/evidencias/` |

## Verificaciones locales

- Backend: 36 pruebas aprobadas en SQLite y 36 en PostgreSQL 16 aislado; cobertura 93,43 %.
- Migraciones: revisión `0002_clients_email_unique` en head; sin nuevas operaciones en `alembic check`.
- Frontend: 11 pruebas y compilación aprobadas; cobertura de líneas 92,19 %, cuatro formularios 100 % y App 90 %.
- Sonar: [análisis de la versión 1.3.0](<../03 Implementación/Sprint 03/evidencias/sonar-1.3.0.json>) del commit `3ea875b`; Quality Gate aprobado con tres condiciones, cobertura global 92,4 %, nueva 100 %, duplicación 0 % y cero problemas abiertos.
- Auditorías Python/npm: sin vulnerabilidades conocidas detectadas en las ejecuciones conservadas.
- Interfaz: 13 estados axe sin infracciones automáticas; 16 comprobaciones dirigidas, 437 comprobaciones de contraste y ningún resultado incompleto sobre contenido funcional. Sin desbordamientos en el alcance medido.
- Infraestructura local: configuraciones Compose de desarrollo y staging validadas sin imprimir credenciales; los servicios de otros proyectos no se modificaron.

## Límites y revisión requerida

El contraste del contenido funcional quedó medido y aprobado; los resultados incompletos restantes son elementos decorativos identificados en el JSON. El uso humano de lector de pantalla y la matriz completa de navegadores siguen por comprobar. También quedan demostración/aceptación con interesados, revisión independiente y decisiones de calendario. No se cierra la épica ni se alteran fechas de ceremonias a partir de las pruebas automáticas.

**Actualización del 25/10/2026:** el [alcance vigente](<../03 Implementación/Sprint 03/Alcance de validación local V_1_0_0.md>) es localhost. El [entorno local](<../03 Implementación/Sprint 03/evidencias/staging-local.json>) verifica frontend HTTP/HTTPS, certificado TLS, salud, login y recursos protegidos; no se requiere infraestructura externa.

La [revisión](<../03 Implementación/Sprint 03/01 Revisión del Sprint V_1_0_0.md>) y la [retrospectiva](<../03 Implementación/Sprint 03/02 Retrospectiva del Sprint V_1_0_0.md>) documentan el incremento y su plan de mejora con hechos observables. Los acuerdos personales y aprobaciones requieren registro por el equipo.

El proyecto, la versión OpenAPI, el paquete frontend y la configuración del análisis Sonar se identifican como **1.3.0**. Los identificadores `1.2.4-sprint3-*` distinguen cortes de análisis anteriores y no se modifican retrospectivamente. Los V_1_0_x son versiones documentales. Los informes de Sprints 1 y 2 se conservan como antecedentes.

La [matriz de entrega frente a la consigna](<../03 Implementación/Sprint 03/Matriz de entrega y rúbrica V_1_0_0.md>) relaciona los ocho criterios con sus evidencias y distingue las evidencias técnicas de los puntos de aceptación todavía pendientes.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| V_1_0_0 | 24/10/2026 | Preparación de la entrega y resultados iniciales. |
| V_1_0_1 | 25/10/2026 | Actualización de versión, evidencias y trazabilidad documental. |
| V_1_0_2 | 25/10/2026 | Actualización de versión, evidencias y trazabilidad documental. |
| V_1_0_3 | 25/10/2026 | Análisis 1.3.0, recorrido técnico registrado y actualización editorial. |
