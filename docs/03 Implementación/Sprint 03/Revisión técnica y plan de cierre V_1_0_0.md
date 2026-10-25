[← Volver al README](../../../README.md)

# Revisión técnica y plan de cierre — Sprint 3

**Versión documental:** V_1_0_1 · **Proyecto:** EcoLogística Lima 1.3.0 · **Fecha:** 25/10/2026 (Lima).<br>
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

La [matriz consolidada de navegadores](evidencias/compatibilidad-1.3.0.json) registra seis versiones aprobadas, 78 estados y 504 comprobaciones. Un reintento de Chrome 155 se identifica expresamente. La comprobación con lector de pantalla se interrumpió por la verificación de URL del control de Windows; no se registra como aprobada.

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

La [evidencia de seguimiento](evidencias/jira-seguimiento-1.3.0.json) conserva responsables, estados y fechas. La versión Jira **1.3.0** está creada sin liberar y vinculada a ECO-51 a ECO-59. Los responsables y fechas de seguimiento se registran en las tareas existentes; no se duplican historias ni se cambia el alcance funcional. Sprint 3 (ID 38) se replanifica del **25/10/2026, 09:00**, al **08/11/2026, 18:00**, hora de Lima. Su estado administrativo permanece `future`; estas fechas son planificación y no acreditan que se haya celebrado una ceremonia.

Sprint 1 (ID 3) sigue `active` y Sprint 2 (ID 37), `future`, en el corte consultado. Se conserva ese antecedente y se asigna su regularización a Marco mediante ECO-49. No se cierran sprints históricos ni se trasladan sus historias para corregir visualmente el tablero. ECO-18 conserva QA hasta la revisión del cliente o del usuario.

## Preparación y revisión pendiente

La preparación técnica incluye los cinco informes, la demostración grabada, resultados de calidad, seguridad y accesibilidad, pruebas, responsables y enlaces. El alcance de ejecución sigue siendo localhost.

**Pendiente: revisión del cliente o del usuario.** Marco coordina la presentación y el registro de observaciones, comprensión con tecnología de asistencia, aceptación de escenarios y resultado aplicable del Done. No se registra una presentación o aprobación todavía no recibida.

La consigna cita además «TP2-ISI Consigna del repositorio PFA». Ese texto no está disponible entre los archivos localizados; Piero queda a cargo de contrastarlo cuando se facilite. Sí se verifican las reglas explícitas del adjunto recibido: Markdown, ubicación, nombres de los cinco informes y enlaces bidireccionales.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| V_1_0_0 | 25/10/2026 | Revisión técnica, distribución nominal, mejoras priorizadas y seguimiento de cierre. |
| V_1_0_1 | 25/10/2026 | Correcciones y comprobaciones de las herramientas locales de evaluación. |

[← Volver al README](../../../README.md)
