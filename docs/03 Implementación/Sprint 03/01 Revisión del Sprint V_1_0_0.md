[← Volver al README](../../../README.md)

# Revisión del sprint

**Nombre del Proyecto:** EcoLogística Lima<br>
**Líder del Proyecto:** Marco Jhair Martinez Llanos, según el acta de constitución.<br>
**Sprint:** 3 — Calidad, seguridad, accesibilidad y mantenibilidad.<br>
**Versión documental:** V_1_0_5 · **Versión del proyecto:** 1.3.0 · **Actualizado:** 25/10/2026 (Lima).<br>
**Rama de entrega:** `Sprint-3`.

**Estado documental:** versión 1.3.0 con evidencias conservadas para revisión.

## Historias de Usuario completadas en este Sprint

**Alcance vigente, 25/10/2026:** ejecución exclusiva en localhost, según la [adenda de validación local](<Alcance de validación local V_1_0_0.md>). La [evidencia local](evidencias/staging-local.json) verifica frontend, API, login, recursos protegidos y TLS; no se requiere infraestructura remota.

El incremento se concentra en trabajo transversal sobre US-001 a US-015. Estas funcionalidades proceden de los Sprints 1 y 2; no se presentan como historias nuevas completadas en Sprint 3. Las tareas técnicas verificadas son:

| Trabajo del incremento | Resultado comprobado | Trazabilidad |
|---|---|---|
| Evaluación y corrección estática | Cuatro botones de formularios con tipo de envío explícito; hallazgos S9011 corregidos | ECO-53 y [calidad de código](<03 Calidad de código V_1_0_0.md>) |
| Seguridad de autenticación | JWT sin `exp` rechazado; firma y caducidad probadas | ECO-54 y [OWASP](<04 OWASP V_1_0_0.md>) |
| Acceso y persistencia | 36 pruebas backend aprobadas sobre SQLite y PostgreSQL aislados; migraciones sin deriva | ECO-54, DoD-03/09 y evidencia técnica |
| Interfaz accesible | Foco gestionado, superficies con contraste medible; 13 estados, 16 comprobaciones dirigidas y 437 comprobaciones de contraste | ECO-55 y [WCAG](<05 WCAG V_1_0_0.md>) |
| Regresión frontend | Once pruebas y compilación aprobadas; formularios con 100 % de cobertura de líneas | ECO-53/55 y DoD-01/03 |
| Organización y documentación | Backend/frontend separados; resultados generados excluidos; cinco informes y adenda de planificación | ECO-56/57/58 |

Las pruebas técnicas verifican comportamientos concretos. La declaración formal de Done requiere revisión independiente y aceptación de los criterios aplicables; no se equipara la ejecución local al cierre administrativo de Jira.

| Historias existentes | Funcionalidad evaluada | Estado técnico y Done |
|---|---|---|
| US-001 a US-004 | Registro, consulta, actualización y desactivación de vehículos | Regresión API y frontend aprobada; revisión del cliente o del usuario pendiente |
| US-005 a US-008 | Registro, consulta, edición y cancelación de pedidos | Regresión API y frontend aprobada; revisión del cliente o del usuario pendiente |
| US-009 a US-012 | Registro, consulta, actualización y desactivación de conductores | Regresión API y frontend aprobada; ECO-18 permanece en QA según el corte Jira documentado |
| US-013 a US-015 | Registro, consulta y actualización de clientes | Regresión API y frontend aprobada; revisión del cliente o del usuario pendiente |

La [matriz BDD](<../../Calidad/01 Matriz de pruebas BDD.md>) detalla la trazabilidad por historia. DoD-01/02/03 tienen evidencias de cobertura, análisis y pruebas; DoD-05/07 cuentan con validación local. La revisión técnica se registra en el plan de cierre; DoD-04/10/12 mantienen la revisión del cliente o del usuario y la aceptación/integración aplicables. DoD-08 se informa con las versiones efectivamente ejecutadas y su límite de revisión con tecnología de asistencia.

## Demostración del trabajo completado

**Fecha del recorrido:** 25/10/2026, 02:04:56 (Lima).<br>
**Versión:** 1.3.0 · **Entorno:** aplicación web y API reales en localhost, con base exclusiva de evaluación.<br>
**Registro:** [video del recorrido](evidencias/demostracion-1.3.0.webm) y [resultados verificables](evidencias/accesibilidad-demostracion-1-3-0.json).

Se ejecutó el recorrido de los cuatro módulos, verificando operaciones sobre registros de evaluación, cambios de estado y mensajes de resultado. Los datos se conservaron durante la ejecución para comprobar que la desactivación y cancelación no eliminan los registros. La base de la aplicación de uso habitual no se modificó.

| Operación demostrada | Historias relacionadas | Resultado visible comprobado | Evidencia |
|---|---|---|---|
| Registro y consulta del cliente | US-013, US-014 | Cliente registrado. | [Captura](evidencias/demostracion-01.png) |
| Actualización de condiciones y consulta de clientes activos | US-014, US-015 | Cliente actualizado. | [Captura](evidencias/demostracion-02.png) |
| Registro y consulta del vehículo | US-001, US-002 | Vehículo registrado. | [Captura](evidencias/demostracion-03.png) |
| Actualización de capacidad del vehículo | US-003 | Vehículo actualizado. | [Captura](evidencias/demostracion-04.png) |
| Desactivación lógica conservando el vehículo | US-004 | Vehículo desactivado. | [Captura](evidencias/demostracion-05.png) |
| Registro y consulta del conductor | US-009, US-010 | Conductor registrado. | [Captura](evidencias/demostracion-06.png) |
| Actualización del contacto del conductor | US-011 | Conductor actualizado. | [Captura](evidencias/demostracion-07.png) |
| Desactivación y exclusión del filtro de conductores disponibles | US-010, US-012 | Conductor desactivado. | [Captura](evidencias/demostracion-08.png) |
| Registro y consulta del pedido pendiente | US-005, US-006 | Pedido registrado. | [Captura](evidencias/demostracion-09.png) |
| Edición del pedido pendiente | US-007 | Pedido actualizado. | [Captura](evidencias/demostracion-10.png) |
| Cancelación y consulta del pedido cancelado | US-006, US-008 | Pedido cancelado. | [Captura](evidencias/demostracion-11.png) |

### Observaciones de la revisión técnica

| Observación | Resultado y acción |
|---|---|
| Las condiciones de entrega deben mantenerse después de editar el cliente | Se guardó una preferencia distinta y se verificó su presentación en el listado. |
| Desactivar conserva la trazabilidad del vehículo y conductor | El vehículo permanece como INACTIVO; el conductor deja de aparecer al filtrar disponibles. |
| Los pedidos pendientes deben poder editarse y cancelarse | La dirección actualizada aparece en el listado; la cancelación cambia el estado a CANCELADO y se comprueba su filtro. |
| La navegación debe ser operable con teclado y mostrar el foco | Los cinco formularios y cambios de vista pasan las 16 comprobaciones dirigidas del recorrido. |
| Los errores de autenticación deben ser perceptibles | El intento con credenciales incorrectas muestra una alerta visible. |

### Resultado de la revisión de historias y Done

Los pasos ejercitan las 15 historias existentes, con resultados técnicos aprobados en el alcance descrito. Se complementan con 36 pruebas backend y 11 frontend, cobertura por componente, análisis SonarQube 1.3.0 y comprobación del entorno local. El registro corresponde a la demostración técnica; la revisión del cliente o del usuario y su aceptación funcional permanecen pendientes.

## Trabajo completado y seguimiento

La [revisión técnica y el plan de cierre](<Revisión técnica y plan de cierre V_1_0_0.md>) reúnen las comprobaciones, responsables nominales y mejoras priorizadas. Las asignaciones se registran por indicación del solicitante el 25/10/2026; no atribuyen aprobaciones personales ni reuniones al equipo.

| Control | Resultado y seguimiento | Responsable |
|---|---|---|
| Revisión técnica del incremento | Código, pruebas y evidencias revisados; observación de contraste móvil corregida y comprobaciones de regresión ejecutadas | Jhon Robert Paitan Montes (API/seguridad) y Luis Antony Gonzalo Guerrero (interfaz) |
| Accesibilidad y navegadores | Matriz técnica ampliada con versiones identificadas, etiquetas, foco, reflow y operaciones funcionales; comprensión con tecnología de asistencia incluida en la revisión del usuario | Luis Antony Gonzalo Guerrero |
| Mejoras de seguridad | Plan priorizado de limitación de intentos, alertas, retención y recuperación, con responsables y criterios verificables | Jhon Robert Paitan Montes y Rodrigo Vladimir Arce Curi |
| Conciliación Jira | Tareas asignadas; Sprint 1 cerrado administrativamente con 10/10 tarjetas finalizadas y Sprint 3 activo desde el 25/10, con fin planificado el 08/11. Sprint 2 conserva ECO-18 en QA | Marco Jhair Martinez Llanos |
| Preparación de la versión final | Cinco informes, evidencias, versión 1.3.0 y enlaces revisados; temporales excluidos | Piero Pool Chauris Leguia y Rodrigo Vladimir Arce Curi |

## Pendientes

| Pendiente | Acción de cierre | Responsable |
|---|---|---|
| Revisión del cliente o del usuario | Completar el [registro preparado de 30 escenarios](<Registro de revisión del cliente o del usuario V_1_0_0.md>): participantes, observaciones, comprensión con tecnología de asistencia, aceptación y resultado del Done | Marco Jhair Martinez Llanos, con apoyo de Luis Antony Gonzalo Guerrero |

La preparación técnica no registra una aceptación todavía no recibida. El texto adicional «TP2-ISI Consigna del repositorio PFA» no se localizó; Piero verificará sus reglas complementarias cuando esté disponible. Las reglas explícitas del adjunto recibido sí se comprueban.

No se incluyen en esta entrega US-016 a US-023: optimización, reoptimización, mapa, indicadores y sostenibilidad funcional continúan en su backlog.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| V_1_0_0 | 24/10/2026 | Revisión del incremento técnico, recorrido reproducible y pendientes de aceptación. |
| V_1_0_1 | 25/10/2026 | Evidencias vigentes, historias y DoD trazados, publicación única y demostración a interesados diferenciada. |
| V_1_0_2 | 25/10/2026 | Actualización de versión, evidencias y trazabilidad documental. |
| V_1_0_3 | 25/10/2026 | Análisis 1.3.0, recorrido técnico registrado y actualización editorial. |
| V_1_0_4 | 25/10/2026 | Revisión técnica, distribución nominal y revisión del cliente o del usuario pendiente. |
| V_1_0_5 | 25/10/2026 | Regularización administrativa comprobada y registro de revisión del cliente preparado. |

[← Volver al README](../../../README.md)
