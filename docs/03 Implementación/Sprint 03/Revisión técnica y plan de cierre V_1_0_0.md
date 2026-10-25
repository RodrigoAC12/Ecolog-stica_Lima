[← Volver al README](../../../README.md)

# Revisión técnica y plan de cierre — Sprint 3

**Versión documental:** V_1_0_3 · **Proyecto:** EcoLogística Lima 1.3.0 · **Fecha:** 25/10/2026 (Lima).<br>
**Alcance:** aplicación, API y bases de evaluación en localhost; historias US-001 a US-015.

## Responsables y seguimiento

La asignación se registra por indicación del solicitante el 25/10/2026. Los nombres corresponden al equipo actual del README; no se altera la composición de los documentos históricos. Los vencimientos son plazos de seguimiento, no fechas atribuidas a reuniones ni a aprobaciones.

| Integrante | Responsabilidad asignada | Tareas Jira | Fecha de seguimiento |
|---|---|---|---|
| Marco Jhair Martinez Llanos | Coordinar el incremento, el calendario y la revisión del cliente o del usuario | ECO-51, ECO-59 y ECO-49 | 26/10/2026; seguimiento de aceptación el 27/10 |
| Luis Antony Gonzalo Guerrero | Retrospectiva, revisión técnica de interfaz, accesibilidad y compatibilidad | ECO-52, ECO-55 y ECO-48 | 26/10 retrospectiva; 27/10 accesibilidad |
| Jhon Robert Paitan Montes | Seguridad, revisión de API y seguimiento de la desactivación de conductores | ECO-54, ECO-18 y ECO-47 | 26/10/2026 |
| Rodrigo Vladimir Arce Curi | Calidad de código, pruebas reproducibles y organización frontend/backend | ECO-53 y ECO-56 | 26/10/2026 |
| Piero Pool Chauris Leguia | Coherencia documental, versiones, enlaces y preparación del paquete de entrega | ECO-57, ECO-58 y ECO-50 | 26/10/2026 |

La cuenta de Piero se identificó con la confirmación del solicitante. La asignación de trabajo no atribuye a los integrantes la ejecución o aprobación personal de las comprobaciones técnicas conservadas.

## Revisión técnica del incremento

Se revisaron autenticación y caducidad JWT, permisos de los endpoints de los cuatro módulos, validación de entradas y estados, transacciones con auditoría, exclusión de secretos, composición de páginas y formularios, navegación y mensajes accesibles. La revisión combina lectura del código con pruebas y resultados reproducibles; no certifica ausencia de todo defecto.

| Punto revisado | Resultado comprobado | Evidencia |
|---|---|---|
| Autenticación | Firma y expiración exigidas; tokens incompletos, vencidos y sin firma rechazados | Pruebas de seguridad y [OWASP](<04 OWASP V_1_0_0.md>) |
| API y persistencia | Restricciones de edición, desactivación y cancelación; duplicados y rollback con auditoría | 36 pruebas backend y [JUnit PostgreSQL](evidencias/backend-postgres.xml) |
| Interfaz | Gestión de foco, etiquetas, estados y cancelación de edición | 11 pruebas frontend, [cobertura](evidencias/frontend-cobertura-1.3.0.json) y recorrido grabado |
| Contraste móvil | Se detectó una superposición del adorno de Inicio sobre el texto en la ampliación de navegadores; se oculta el adorno a 600 px o menos | `responsive.css`; [matriz consolidada](evidencias/compatibilidad-1.3.0.json), seis versiones aprobadas |
| Calidad estática | Consultar el análisis identificado y el alcance de sus métricas | [Informe de calidad](<03 Calidad de código V_1_0_0.md>) |
| Seguridad de despliegue | Servicios de evaluación aislados; HTTPS y recursos protegidos comprobados en loopback | [Entorno local](evidencias/staging-local.json) |
| Documentación | Cinco informes canónicos, versión 1.3.0, ida/vuelta con README y exclusión de temporales | Comprobador de enlaces, `.gitignore` y matriz de rúbrica |

Luis y Jhon asumen el seguimiento de la revisión técnica según su ámbito. El documento no registra su firma ni una aprobación personal que no haya sido recibida.

La [matriz consolidada de navegadores](evidencias/compatibilidad-1.3.0.json) registra seis versiones aprobadas, 78 estados y 504 comprobaciones. Un reintento de Chrome 155 se identifica expresamente. La [prueba parcial con NVDA](<../../Calidad/06 Prueba con lector de pantalla.md>) acredita seis comprobaciones del acceso y de Inicio mediante su salida real. El recorrido integral sigue pendiente: la captura dejó de producir anuncios y la inspección de Windows se interrumpió por la verificación de URL; no se registra una aprobación completa.

La API del frontend solicita respuestas sin almacenamiento en caché como medida preventiva de consistencia y privacidad; no se presenta una causa de fallo de caché como confirmada.

La [remediación de herramientas locales](<../../Calidad/05 Seguridad de herramientas locales.md>) incorpora configuración cifrada con DPAPI, migración sin cambio de credenciales, mínimo TLS explícito y nombre de video controlado localmente. Las cuatro pruebas de configuración y la repetición de 13 estados de interfaz aprobaron; el nuevo CodeQL y su evidencia final confirman las tres alertas corregidas, con cero abiertas.

## Plan priorizado de mejoras de seguridad

La acción de esta entrega es evaluar y priorizar las mejoras. Implementarlas corresponde a su planificación posterior; no se convierten en exigencias adicionales de la consigna.

| Orden | Mejora | Responsable | Seguimiento | Criterio verificable para su implementación |
|---|---|---|---|---|
| 1 | Limitar intentos de autenticación con recuperación del acceso | Jhon Robert Paitan Montes; apoyo de Rodrigo Vladimir Arce Curi | 27/10/2026, ECO-54 | Exceso de intentos devuelve 429, expira el bloqueo y no filtra si existe una cuenta; pruebas de concurrencia y recuperación |
| 2 | Registrar y alertar sobre fallos repetidos de autenticación | Jhon Robert Paitan Montes | 28/10/2026, ECO-54 | Éxitos, fallos y bloqueos correlacionables sin contraseñas ni tokens en logs; alerta local comprobable |
| 3 | Definir retención y recuperación de auditoría | Rodrigo Vladimir Arce Curi; coordinación de Marco Jhair Martinez Llanos | 29/10/2026, ECO-54 | Política de retención documentada, copia aislada y restauración verificable sin borrar evidencia vigente |
| 4 | Ampliar la matriz de autorización y pruebas de fallos del servicio | Jhon Robert Paitan Montes; apoyo de Luis Antony Gonzalo Guerrero | 30/10/2026, ECO-54 | Roles previstos y operaciones permitidas/denegadas; fallo controlado de base, rollback y recuperación sin pérdida de integridad |

## Conciliación de Jira

La [evidencia de seguimiento](evidencias/jira-seguimiento-1.3.0.json) conserva responsables, estados y fechas. La versión Jira **1.3.0** está creada sin liberar y vinculada a ECO-51 a ECO-59. Las tareas siguen asignadas a los cinco integrantes.

La consulta previa verificó que las diez tarjetas de Sprint 1 (ID 3) ya tenían categoría `done`. Se registró su **cierre administrativo el 25/10/2026 a las 16:06:57 (Lima)**, sin cambiar los estados de las historias, sus fechas planificadas ni atribuir una aceptación nueva. Los datos [anteriores](evidencias/jira-regularizacion-antes.json) y [posteriores](evidencias/jira-regularizacion-despues.json) se conservan.

Sprint 3 (ID 38) está **activo desde el 25/10/2026 a las 16:07:13 (Lima)**, con fin planificado el 08/11/2026 a las 18:00. Se conserva la programación anterior como antecedente y se registra la apertura administrativa real; no se afirma que se haya celebrado una reunión.

Sprint 2 (ID 37) mantiene cuatro historias finalizadas y **ECO-18 en QA**, pendiente de revisión del cliente o del usuario. Se conserva `future` y su programación histórica: no se inicia ni se cierra una iteración incompleta para aparentar aceptación. ECO-49 conserva ese seguimiento residual a cargo de Marco; no se mueven sus historias a Sprint 3.

## Preparación y revisión pendiente

La preparación técnica incluye los cinco informes, la demostración grabada, resultados de calidad, seguridad y accesibilidad, pruebas, responsables y enlaces. El alcance de ejecución sigue siendo localhost.

El [registro de revisión preparado](<Registro de revisión del cliente o del usuario V_1_0_0.md>) contiene los 30 escenarios oficiales de las 15 historias, campos de participantes, observaciones, decisiones y Done. Los campos de resultado permanecen pendientes.

**Pendiente: revisión del cliente o del usuario.** Marco coordina la presentación y el registro de observaciones, comprensión con tecnología de asistencia, aceptación de escenarios y resultado aplicable del Done. No se registra una presentación o aprobación todavía no recibida.

La consigna cita además «TP2-ISI Consigna del repositorio PFA». La búsqueda repetida en el repositorio y Descargas no localizó ese texto; la consulta conectada devolvió únicamente su referencia en ECO-57 y advirtió fuentes parcialmente disponibles. Piero queda a cargo de contrastarlo cuando se facilite. Sí se verifican las reglas explícitas del adjunto recibido: Markdown, ubicación, nombres de los cinco informes y enlaces bidireccionales.



### Cierre de entregables en Jira — 25/10/2026

La [consulta posterior](evidencias/jira-seguimiento-1.3.0.json) verifica **ECO-52 a ECO-58 en Finalizada**: informe retrospectivo, calidad, seguridad, evaluación WCAG, organización, versionado y publicación documental. Cada tarjeta registra el motivo y el alcance del cierre. El [corte anterior](evidencias/jira-seguimiento-antes-cierre-entregables.json) se conserva.

El cierre de ECO-55 corresponde al informe de evaluación, que incluye límites y comprobaciones pendientes; no declara recorrido integral NVDA aprobado ni conformidad AA universal. **ECO-51 y ECO-18 siguen en QA; ECO-47 a ECO-49 y ECO-59 siguen en curso; ECO-50 sigue en QA.** El recorrido NVDA restante se conserva en ECO-48. No se libera la versión ni se cierra la épica por completar los documentos.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| V_1_0_0 | 25/10/2026 | Revisión técnica, distribución nominal, mejoras priorizadas y seguimiento de cierre. |
| V_1_0_1 | 25/10/2026 | Correcciones y comprobaciones de las herramientas locales de evaluación. |
| V_1_0_2 | 25/10/2026 | Cierre administrativo de Sprint 1, activación real de Sprint 3 y preparación de los 30 escenarios de revisión. |
| V_1_0_3 | 25/10/2026 | Prueba parcial con NVDA y límites del recorrido completo. |

[← Volver al README](../../../README.md)
