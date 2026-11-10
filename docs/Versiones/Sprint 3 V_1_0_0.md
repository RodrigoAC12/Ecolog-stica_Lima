[← Volver al README](../../README.md)

# Entrega técnica del Sprint 3

**Versión documental:** V_1_0_8 · **Versión del proyecto:** 1.3.0 · **Actualizado:** 25/10/2026 (Lima).<br>
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
| CI | Controles al actualizar `main` y `Sprint-3`; cobertura frontend conservada | `.github/workflows/` |
| Organización | Resultados generados ignorados y solo evidencia solicitada conservada | `.gitignore` y cinco informes oficiales |

## Verificaciones locales

- Backend: 36 pruebas aprobadas en SQLite y 36 en PostgreSQL 16 aislado; cobertura 93,43 %.
- Migraciones: revisión `0002_clients_email_unique` en head; sin nuevas operaciones en `alembic check`.
- Frontend: 11 pruebas y compilación aprobadas; cobertura de líneas 92,75 %, cuatro formularios 100 % y App 100 %.
- SonarCloud: [informe oficial de calidad](<../03 Implementación/Sprint 03/03 Calidad de código V_1_0_0.md>) sobre `fd9ede18`; Quality Gate aprobado, cobertura global 81,6 %, nueva 92,9 %, duplicación 0 % y cero problemas abiertos.
- Auditorías Python/npm: sin vulnerabilidades conocidas detectadas en las ejecuciones conservadas.
- Interfaz: 13 estados axe sin infracciones automáticas; 16 comprobaciones dirigidas, 437 comprobaciones de contraste y ningún resultado incompleto sobre contenido funcional. Sin desbordamientos en el alcance medido.
- Infraestructura local: configuraciones Compose de desarrollo y staging validadas sin imprimir credenciales; los servicios de otros proyectos no se modificaron.

## Límites y revisión requerida

La evaluación de accesibilidad y compatibilidad se resume en el [informe WCAG](<../03 Implementación/Sprint 03/05 WCAG V_1_0_0.md>). La comprensión, las observaciones y la aceptación del cliente o usuario permanecen pendientes. No se atribuyen sesiones ni aprobaciones personales.

La [Retrospectiva del Sprint](<../03 Implementación/Sprint 03/02 Retrospectiva del Sprint V_1_0_0.md>) registra acciones y responsables propuestos. La versión 1.3.0 permanece sin liberar y ECO-18 continúa condicionado a la revisión del cliente o usuario.

**Actualización documental:** el alcance, las limitaciones y los pendientes se encuentran en la [Revisión del Sprint](<../03 Implementación/Sprint 03/01 Revisión del Sprint V_1_0_0.md>).

La [revisión](<../03 Implementación/Sprint 03/01 Revisión del Sprint V_1_0_0.md>) y la [retrospectiva](<../03 Implementación/Sprint 03/02 Retrospectiva del Sprint V_1_0_0.md>) documentan el incremento y su plan de mejora con hechos observables. La asignación procede de la indicación del solicitante; no se atribuyen aprobaciones personales.

El proyecto, la versión OpenAPI, el paquete frontend y la configuración del análisis Sonar se identifican como **1.3.0**. Los identificadores `1.2.4-sprint3-*` distinguen cortes de análisis anteriores y no se modifican retrospectivamente. Los V_1_0_x son versiones documentales. Los informes de Sprints 1 y 2 se conservan como antecedentes.

Los cinco informes oficiales relacionan los criterios de la consigna con resultados reales y puntos de aceptación pendientes.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| V_1_0_0 | 24/10/2026 | Preparación de la entrega y resultados iniciales. |
| V_1_0_1 | 25/10/2026 | Actualización de versión, evidencias y trazabilidad documental. |
| V_1_0_2 | 25/10/2026 | Actualización de versión, evidencias y trazabilidad documental. |
| V_1_0_3 | 25/10/2026 | Análisis 1.3.0, recorrido técnico registrado y actualización editorial. |
| V_1_0_4 | 25/10/2026 | Revisión técnica, compatibilidad ampliada, responsables nominales y seguimiento actualizado. |
| V_1_0_5 | 25/10/2026 | Cierre administrativo y activación verificados en Jira; protocolo de revisión preparado. |
| V_1_0_6 | 25/10/2026 | Resultados parciales reales de NVDA y alcance restante documentado. |
| V_1_0_7 | 25/10/2026 | Recorrido NVDA aprobado, correcciones verificadas y aceptación del cliente o usuario pendiente. |
| V_1_0_8 | 25/10/2026 | Integración de antecedentes en Sprint 03, retiro de la etapa separada y enlaces actualizados. |
