[← Volver al README](../../../README.md)

# Retrospectiva del sprint

**Nombre del Proyecto:** EcoLogística Lima<br>
**Líder del Proyecto:** Marco Jhair Martinez Llanos, según el acta de constitución.<br>
**Versión documental:** V_1_0_0 · **Fecha de corte:** 24/10/2026 (Lima).

## ¿Qué aprendimos?

Aprendimos a distinguir la primera línea base de SonarQube de una evaluación efectiva del código nuevo: el primer Quality Gate devolvía condiciones vacías y el reanálisis posterior sí evaluó sus umbrales. La ausencia de alertas estáticas tampoco cubría toda la seguridad: una prueba negativa detectó la aceptación de tokens sin expiración y permitió corregirla.

La evaluación de interfaz mostró otra diferencia útil: axe no notificó infracciones automáticas, pero las comprobaciones dirigidas detectaron seis fallas de foco relacionadas con una causa común. La revisión de la interacción y de las capturas complementó las métricas.

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

Hacer explícita la revisión entre pares y recoger las observaciones de interesados sobre el incremento. La aprobación del propietario y la revisión técnica tienen propósitos diferentes y deben quedar registradas.

### Procesos

Actualizar Jira con el avance sustentado y corregir la discrepancia de los calendarios mediante decisiones del equipo. Incorporar pruebas negativas y accesibilidad desde el inicio del cambio, en lugar de concentrarlas al cierre. Revisar la cobertura por módulo, no solo la cifra global.

### Herramientas

Ejecutar CI, CodeQL y auditorías sobre `main` y la rama de entrega. Mantener un scanner reproducible, reportes de cobertura y un entorno aislado para la auditoría web. Los resultados incompletos de contraste y las limitaciones de un navegador deben permanecer visibles para su revisión.

### Acciones a realizar

| Acción verificable | Responsable propuesto | Plazo de referencia | Evidencia de cumplimiento |
|---|---|---|---|
| Revisar el PR y las correcciones sin cambiar umbrales para ocultar hallazgos | Par técnico distinto del autor | Antes de integrar | Revisión registrada y CI aprobado |
| Completar contraste, lector de pantalla y navegadores del alcance | Calidad/UX | Antes de declarar conformidad AA | Matriz de criterios y resultados por entorno |
| Definir limitación de intentos, auditoría de login y seguridad del despliegue | Backend/infraestructura | Antes de exposición externa | Pruebas y configuración verificadas |
| Conciliar responsables, fechas y estados de Jira | Líder del proyecto y equipo | Antes del cierre administrativo | Tablero y acuerdos con fechas reales |
| Priorizar escenarios no cubiertos de los formularios | Desarrollo frontend | Próxima iteración técnica | Cobertura por módulo y nuevas pruebas pertinentes |
| Conservar los cinco informes y validar enlaces tras cada cambio | Responsable documental | En cada entrega | Comprobador de enlaces aprobado |

Las acciones representan el plan de mejora derivado del trabajo observado. Los responsables concretos y fechas de calendario requieren confirmación del equipo; no se registran como compromisos personales ya aceptados.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| V_1_0_0 | 24/10/2026 | Aprendizajes sustentados, cuatro dimensiones de mejora y acciones verificables. |

[← Volver al README](../../../README.md)
