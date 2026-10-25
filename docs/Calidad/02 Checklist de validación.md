[← Volver al README](../../README.md)

# Checklist de validación — Sprint 3

**Versión documental:** 1.0.10 · **Versión del Sprint 3:** 1.3.0 · **Actualizado:** 25/10/2026. Se identifican los resultados históricos y las adendas posteriores.

**Corte histórico de base:** versión 1.2.4 · **Rama:** `Pre-Sprint-3` · **Fecha:** 24/10/2026.

Este registro distingue **implementación técnica en la rama** de **aceptación formal**. Cada control de CI debe comprobarse nuevamente en el commit definitivo.

## Entregables y código

- [x] Conservar los 13 documentos de Inicio sin modificar los hechos históricos.
- [x] Incorporar el presupuesto como cuarto entregable de Planificación; seguimiento Jira en Anexos.
- [x] Agrupar informes en carpetas Sprint 1, Sprint 2 y antecedentes de la base 1.2.4 integrados en Sprint 03; documentar las modificaciones globales en [Versión 1.2.4](../Versiones/1.2.4.md).
- [x] Centralizar diagramas de API y C4 en `docs/Arquitectura/`.
- [x] Incorporar migraciones explícitas Alembic e índice de unicidad de correo del cliente.
- [x] Añadir pruebas de rollback, auditoría y salvaguarda de bases de prueba.
- [x] Separar frontend en `pages/`, `forms/`, `components/` y `styles/` sin añadir historias futuras.
- [x] Preparar workflows de CI, CodeQL y auditoría de dependencias.
- [x] Preparar configuración de staging aislado sin presentar un despliegue externo como hecho.
- [x] Crear [matriz BDD](<01 Matriz de pruebas BDD.md>) de US-001 a US-015.

## Verificaciones automáticas

- [x] [CI de la base histórica 1.2.4](https://github.com/RodrigoAC12/Ecolog-stica_Lima/actions/runs/40141894546): 27 pruebas backend tanto en SQLite como en PostgreSQL 16, cobertura del 92,85 %, 6 pruebas frontend, build, migraciones Alembic, Docker y enlaces.
- [x] [Auditoría de dependencias](https://github.com/RodrigoAC12/Ecolog-stica_Lima/actions/runs/40141894558) aprobada.
- [x] [CodeQL Python/TypeScript](https://github.com/RodrigoAC12/Ecolog-stica_Lima/actions/runs/40141894532) aprobado con los análisis SARIF exportados.
- [x] Triage técnico actualizado el 25/10: tres alertas corregidas y cero abiertas; evidencia en la adenda de Sprint 3.
- [x] Validación automática de enlaces locales Markdown aprobada durante el CI de la base histórica 1.2.4.

## Validaciones formales pendientes

- [ ] Aprobación presupuestal y del contenido documental por el equipo.
- [x] Staging en localhost verificado el 25/10/2026, con HTTPS local y secretos fuera del repositorio.
- [ ] Pruebas manuales de accesibilidad WCAG, 360 px, teclado y navegadores soportados.
- [ ] Demostración y aceptación de los escenarios oficiales Gherkin por interesados.
- [ ] Revisión independiente del código y aceptación del equipo responsable.
- [x] Integración técnica de la base 1.2.4 con 24/10/2026; no sustituye la revisión independiente requerida.
- [ ] Confirmación de responsables, estado de sprints y ceremonias reales en Jira; no inventar reuniones ni fechas.

**Referencias:** [Informe de seguridad](<../03 Implementación/Sprint 03/Antecedentes 1.2.4/02 Informe de seguridad V_1_0_0.md>), [Integridad y auditoría](<../03 Implementación/Sprint 03/Antecedentes 1.2.4/03 Informe de integridad y auditoría V_1_0_0.md>) y [Versión 1.2.4](../Versiones/1.2.4.md).

## Adenda de Sprint 3 — estado vigente al 25/10/2026

- [x] Triage de CodeQL: tres alertas de herramientas corregidas y verificadas en el reanálisis, cero abiertas. Configuración operativa cifrada y cuatro pruebas DPAPI aprobadas.

- [x] Cinco informes oficiales preparados en `docs/03 Implementación/Sprint 03/` con retorno al README.
- [x] Cuatro hallazgos S9011 corregidos y reanalizados.
- [x] JWT sin expiración rechazado y probado.
- [x] Gestión de foco corregida y comprobada en la aplicación real.
- [x] 36 pruebas backend en SQLite y PostgreSQL; migraciones verificadas.
- [x] 11 pruebas frontend y compilación; 92,75 % de líneas, cuatro formularios 100 % y App 100 %.
- [x] Auditorías de dependencias sin avisos conocidos en el corte conservado.
- [x] Sonar 1.3.0 del commit `647f0a2` aprobado: tres condiciones, 92,6 % global, 100 % nuevo y cero problemas abiertos.
- [x] 13 estados de accesibilidad automática y 16 comprobaciones dirigidas aprobadas.
- [x] Contraste funcional medido: 437 comprobaciones, mínimo 6,66:1; restantes incompletos decorativos identificados.
- [x] Completar matriz técnica de dos versiones de Chrome, Edge y Firefox: seis versiones, 78 estados y 504 comprobaciones, con reintento identificado.
- [x] [Prueba técnica NVDA aprobada](<06 Prueba con lector de pantalla.md>): 53/53 comprobaciones, 74 anuncios y correcciones verificadas; se conservan los cortes previos.
- [ ] Registrar comprensión y aceptación en la revisión del cliente o del usuario.
- [x] Documentar revisión técnica de código, pruebas y evidencias, con responsables nominales.
- [ ] Registrar revisión del cliente o del usuario, observaciones y aceptación aplicable.
- [x] Validar el entorno local según la [adenda vigente](<../03 Implementación/Sprint 03/Alcance de validación local V_1_0_0.md>).
- [x] Asignar tareas a los cinco integrantes, fijar seguimiento, replanificar Sprint 3 y vincular versión Jira 1.3.0 sin liberar.
- [x] Jira actualizado: ECO-52 a ECO-58 Finalizada por sus entregables verificables; NVDA aprobado registrado en ECO-48 y aceptación aplicable pendiente.
- [x] Regularizar lo verificable: Sprint 1 cerrado administrativamente con 10/10 tarjetas finalizadas y Sprint 3 activo con fecha real; evidencia antes/después conservada.
- [ ] Mantener ECO-18 en QA y Sprint 2 sin cierre hasta la revisión del cliente o usuario.

- [x] Versión del Sprint 3 corregida a 1.3.0 y [matriz de los ocho criterios](<../03 Implementación/Sprint 03/Matriz de entrega y rúbrica V_1_0_0.md>) actualizada.
- [x] Recorrido técnico grabado: once operaciones comprobadas sobre las quince historias, con capturas, observaciones y resultados.
- [ ] Revisión del cliente o del usuario y observaciones para completar el criterio 1.
- [ ] Aceptación e incorporación final; los resultados técnicos no sustituyen la aprobación correspondiente.

Consultar el [registro de entrega del Sprint 3](<../Versiones/Sprint 3 V_1_0_0.md>) para resultados, límites y trazabilidad. La preparación de documentos no convierte en realizadas las validaciones pendientes.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 24/10/2026 | Checklist de la base histórica 1.2.4. |
| 1.0.1 | 24/10/2026 | Adenda del incremento de Sprint 3. |
| 1.0.2 | 25/10/2026 | Alcance y comprobación localhost. |
| 1.0.3 | 25/10/2026 | Evidencias de contraste, cobertura, Sonar y matriz de entrega única. |
| 1.0.4 | 25/10/2026 | Actualización de versión, evidencias y trazabilidad documental. |
| 1.0.5 | 25/10/2026 | Análisis 1.3.0, recorrido técnico registrado y actualización editorial. |
| 1.0.6 | 25/10/2026 | Revisión técnica, compatibilidad ampliada, responsables nominales y seguimiento actualizado. |
| 1.0.7 | 25/10/2026 | Regularización administrativa verificada y protocolo de revisión del cliente preparado. |
| 1.0.8 | 25/10/2026 | Seis comprobaciones NVDA acreditadas; recorrido integral y aceptación diferenciados. |
| 1.0.9 | 25/10/2026 | Recorrido NVDA aprobado, correcciones verificadas y aceptación del cliente o usuario pendiente. |
| 1.0.10 | 25/10/2026 | Integración de antecedentes en Sprint 03, retiro de la etapa separada y enlaces actualizados. |
