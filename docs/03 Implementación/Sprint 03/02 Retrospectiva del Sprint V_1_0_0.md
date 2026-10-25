[← Volver al README](../../../README.md)

# Retrospectiva del sprint

**Nombre del Proyecto:** EcoLogística Lima<br>
**Líder del Proyecto:** Marco Jhair Martinez Llanos, según el acta de constitución.<br>
**Versión documental:** V_1_0_4 · **Versión del proyecto:** 1.3.0 · **Actualizado:** 25/10/2026 (Lima).

**Estado documental:** versión 1.3.0 con evidencias conservadas para revisión.

## ¿Qué aprendimos?

El alcance vigente se limita a localhost; la [adenda del 25/10/2026](<Alcance de validación local V_1_0_0.md>) y la [evidencia local](evidencias/staging-local.json) sustituyen la dependencia de infraestructura remota por una validación reproducible en esta PC.

Aprendimos a distinguir la primera línea base de SonarQube de una evaluación efectiva del código nuevo: el primer Quality Gate devolvía condiciones vacías y el reanálisis posterior sí evaluó sus umbrales. La ausencia de alertas estáticas tampoco cubría toda la seguridad: una prueba negativa detectó la aceptación de tokens sin expiración y permitió corregirla.

La evaluación de interfaz mostró otra diferencia útil: axe no notificó infracciones automáticas, pero las comprobaciones dirigidas detectaron seis fallas de foco relacionadas con una causa común. La revisión de la interacción y de las capturas complementó las métricas.

El cierre técnico mostró que el contraste indeterminado podía resolverse eliminando fondos superpuestos al texto, sin inventar un porcentaje global de conformidad. Las 437 comprobaciones de texto pasan. Cuatro pruebas de cancelación de edición elevaron los formularios a 100 % de líneas y comprobaron un comportamiento relevante: descartar cambios no debe enviar una escritura al servidor.

## ¿Qué estamos haciendo bien?

- Conservamos evidencias antes y después de las correcciones.
- Reutilizamos pruebas y añadimos regresiones para los defectos encontrados.
- Verificamos el backend sobre SQLite y PostgreSQL sin reutilizar bases de otros proyectos.
- Mantuvimos separados el código frontend/backend y los resultados generados.
- Relacionamos cada informe con los ocho criterios de la consigna y con Jira.
- Conservamos los cortes históricos y diferenciamos implementación técnica de aceptación.

## ¿Qué podemos hacer mejor?

### Personas

Distribuir con claridad la revisión de seguridad, accesibilidad y documentación. El conocimiento de herramientas debe compartirse mediante el procedimiento reproducible y una transferencia breve, evitando que la validación dependa de una sola persona.

### Relaciones

Hacer explícita la revisión entre pares y recoger las observaciones de interesados sobre el incremento. La aceptación funcional y la revisión técnica tienen propósitos diferentes y deben quedar registradas.

### Procesos

Actualizar Jira con el avance sustentado y corregir la discrepancia de los calendarios mediante decisiones del equipo. Incorporar pruebas negativas y accesibilidad desde el inicio del cambio, en lugar de concentrarlas al cierre. Revisar la cobertura por módulo, no solo la cifra global.

### Herramientas

Ejecutar CI, CodeQL y auditorías sobre `main` y la rama de entrega. Mantener un scanner reproducible, reportes de cobertura y un entorno aislado para la auditoría web. Los resultados decorativos no evaluables y los límites del navegador deben conservarse explícitos; no convertirlos en una aprobación universal de accesibilidad.

### Acciones a realizar

| Acción verificable | Responsable asignado | Seguimiento | Resultado y evidencia |
|---|---|---|---|
| Revisar autenticación, permisos, estados y evidencias | Jhon Robert Paitan Montes y Luis Antony Gonzalo Guerrero | 26/10/2026 | [Revisión técnica](<Revisión técnica y plan de cierre V_1_0_0.md>); observación de contraste móvil identificada y corregida |
| Completar la matriz técnica de accesibilidad y navegadores | Luis Antony Gonzalo Guerrero | 27/10/2026 | [WCAG](<05 WCAG V_1_0_0.md>); comprensión con tecnología de asistencia en revisión del cliente o del usuario |
| Priorizar limitación de intentos, alertas, retención y recuperación | Jhon Robert Paitan Montes y Rodrigo Vladimir Arce Curi | 27 a 30/10/2026 | Cuatro mejoras ordenadas con criterios de cierre en el plan; implementación posterior según riesgo |
| Conciliar responsables y fechas de seguimiento en Jira | Marco Jhair Martinez Llanos | 26/10/2026 | Reparto nominal y Sprint 3 replanificado; el antecedente de Sprints 1 y 2 se conserva en ECO-49 |
| Mantener regresiones y compilación del frontend | Rodrigo Vladimir Arce Curi | En cada cambio afectado | 11 pruebas y cobertura por módulo; comprobaciones de navegadores sobre la aplicación real |
| Revisar versiones, cinco informes y enlaces | Piero Pool Chauris Leguia | 26/10/2026 | Comprobador de enlaces y versión 1.3.0; contraste de norma PFA al recibir su texto |

Este plan queda asignado por indicación del solicitante el 25/10/2026. Los plazos son fechas de seguimiento y no se presentan como compromisos personales ya aceptados ni como constancia de una reunión. Los aprendizajes y acciones derivan de las comprobaciones efectivamente registradas.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| V_1_0_0 | 24/10/2026 | Aprendizajes sustentados, cuatro dimensiones de mejora y acciones verificables. |
| V_1_0_1 | 25/10/2026 | Resultados del contraste y cobertura, acciones realizadas y mejoras futuras diferenciadas. |
| V_1_0_2 | 25/10/2026 | Actualización de versión, evidencias y trazabilidad documental. |
| V_1_0_3 | 25/10/2026 | Análisis 1.3.0, recorrido técnico registrado y actualización editorial. |
| V_1_0_4 | 25/10/2026 | Responsables nominales, plazos de seguimiento y revisión técnica documentada. |

[← Volver al README](../../../README.md)
