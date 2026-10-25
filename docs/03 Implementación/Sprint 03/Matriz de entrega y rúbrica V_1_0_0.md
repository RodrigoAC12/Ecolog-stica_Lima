[← Volver al README](../../../README.md)

# Matriz de entrega y rúbrica — Sprint 3

**Versión documental:** V_1_0_5 · **Versión del proyecto:** 1.3.0 · **Fecha:** 25/10/2026 (Lima).<br>
**Fuente:** consigna oficial «Implementación, Calidad de Código y Evaluación», adjunta por el solicitante.<br>
**Estado documental:** versión 1.3.0 con evidencias conservadas para revisión.
**Alcance de ejecución:** exclusivamente localhost. Esta matriz permite revisar primero con el solicitante; no asigna una nota ni sustituye revisión del cliente o del usuario.

## Los ocho criterios

| Ítem y exigencia de la rúbrica | Evidencia entregada | Estado y límite |
|---|---|---|
| 1. Review: secciones completas, HU y Done, demostración a interesados y pendientes reales | [Informe 01](<01 Revisión del Sprint V_1_0_0.md>), tabla de US-001 a US-015, DoD, recorrido y capturas | **Preparado para revisión:** video, resultados técnicos y [registro de 30 escenarios](<Registro de revisión del cliente o del usuario V_1_0_0.md>). La revisión del cliente o del usuario permanece pendiente. |
| 2. Retrospectiva: aprendizajes, aciertos y acciones concretas en Personas, Relaciones, Procesos y Herramientas | [Informe 02](<02 Retrospectiva del Sprint V_1_0_0.md>), acciones con responsables nominales, fechas de seguimiento y evidencia | **Documento actualizado:** cuatro dimensiones cubiertas y plan asignado a los cinco integrantes por indicación del solicitante; no se atribuyen reuniones ni aprobaciones personales. |
| 3. Calidad: Quality Gate, bugs, smells, cobertura, duplicación y plan de deuda | [Informe 03](<03 Calidad de código V_1_0_0.md>), [Sonar 1.3.0](evidencias/sonar-1.3.0.json) y [cobertura por archivo](evidencias/frontend-cobertura-1.3.0.json) | **Evaluado:** gate aprobado; 92,4 % global, 100 % nuevo, duplicación 0 %, cero problemas abiertos. Plan y antecedentes incluidos. |
| 4. OWASP 2025: diez categorías, hallazgos/hotspots y correcciones | [Informe 04](<04 OWASP V_1_0_0.md>), Sonar, auditorías, pruebas negativas y evidencia TLS local | **Evaluación documentada:** cero hotspots detectados y defecto JWT corregido. Se explicitan categorías bajo revisión y límites del perfil estático. No se afirma seguridad completa ni se inventan hotspots. |
| 5. WCAG AA: cuatro principios, interpretación y tabla de problemas/componentes/correcciones | [Informe 05](<05 WCAG V_1_0_0.md>), [matriz de seis versiones](evidencias/compatibilidad-1.3.0.json), corte de 13 estados, video y capturas antes/después | **Evaluación ampliada:** seis versiones aprobadas, 78 estados, 504 comprobaciones y 3.258 ocurrencias de contraste; reintento identificado. Seis comprobaciones del acceso con salida real de NVDA acreditadas; recorrido integral y revisión del cliente o del usuario pendientes. No se declara conformidad AA universal. |
| 6. Frontend/backend modular y `.gitignore` sin temporales | [Frontend](../../../src/frontend/), [backend](../../../src/backend/) y [.gitignore](../../../.gitignore) | **Preparado:** componentes separados; se excluyen secretos, dependencias instaladas, coberturas de trabajo, cachés y copias temporales. Se conserva evidencia seleccionada. |
| 7. Coherencia y actualización/versionamiento de documentos afectados | Cinco informes con versión documental identificada; [versión 1.3.0](../../Versiones/1.3.0.md), [adenda de planificación](<../../02 Planificación/Anexos/Planificación Sprint 3 V_1_0_0.md>), [base histórica](../../Versiones/1.2.4.md), notas y guías con historial | **Actualizado:** 1.3.0 identifica el proyecto y sus metadatos. Las evidencias anteriores mantienen su corte. Se conservan nombres canónicos de los cinco archivos exigidos y sus versiones documentales independientes. |
| 8. Cinco Markdown en `docs/03 Implementación/Sprint 03` y enlaces de ida/vuelta con README | [README](../../../README.md), cinco informes enlazados y comprobador de enlaces | **Preparado:** ubicación y enlaces verificados; aceptación e incorporación final pendientes. |

La regularización administrativa conserva cortes antes/después: Sprint 1 cerrado con las diez tarjetas que ya estaban finalizadas y Sprint 3 activo con fecha real. Sprint 2 conserva ECO-18 en QA; no se atribuyen reuniones ni aceptación.

## Cómo revisar la entrega

1. Leer los cinco informes oficiales y abrir sus JSON/capturas desde GitHub; no se necesita acceso al Sonar de esta PC para revisar las métricas conservadas.
2. Consultar los controles de la [rama Sprint-3 del fork](https://github.com/RodrigoAC12/Ecolog-stica_Lima/actions?query=branch%3ASprint-3). La CI ejecuta backend SQLite/PostgreSQL, migraciones, frontend en Node 22, compilación, enlaces y configuración/build Compose. CodeQL y auditorías se ejecutan por separado.
3. Para reproducir en la PC local, seguir la [guía de staging](<../../Despliegue/Guía de staging.md>) y la [guía Sonar](<../../Calidad/03 SonarQube local.md>). Las credenciales operativas permanecen fuera de Git.
4. La auditoría de interfaz se reproduce desde `src/frontend` mediante `npm run audit:accessibility -- entrega-edge edge`, con Edge instalado y la `.venv` del backend preparada. Utiliza procesos y SQLite propios en localhost.
5. Registrar observaciones de la revisión funcional y completar la revisión del cliente o del usuario antes de declarar todo el Done.

## Obligaciones y plan de mejora

La consigna pide evaluar, interpretar y documentar correcciones y remediación; no exige declarar todas las categorías OWASP limpias ni implementar de inmediato toda mejora encontrada. Limitación de intentos, alertas/retención y pruebas adicionales de recuperación se conservan en el plan de mejora. No se añaden US-016 a US-023 ni infraestructura externa a esta entrega.

El adjunto remite además a «TP2-ISI Consigna del repositorio PFA», cuyo texto no acompaña el archivo recibido. Se verifican aquí las reglas explícitas de ubicación, Markdown y enlaces del adjunto; no se atribuye verificación de reglas adicionales no disponibles.



### Cierre de entregables en Jira — 25/10/2026

La [consulta posterior](evidencias/jira-seguimiento-1.3.0.json) verifica **ECO-52 a ECO-58 en Finalizada**: informe retrospectivo, calidad, seguridad, evaluación WCAG, organización, versionado y publicación documental. Cada tarjeta registra el motivo y el alcance del cierre. El [corte anterior](evidencias/jira-seguimiento-antes-cierre-entregables.json) se conserva.

El cierre de ECO-55 corresponde al informe de evaluación, que incluye límites y comprobaciones pendientes; no declara recorrido integral NVDA aprobado ni conformidad AA universal. **ECO-51 y ECO-18 siguen en QA; ECO-47 a ECO-49 y ECO-59 siguen en curso; ECO-50 sigue en QA.** El recorrido NVDA restante se conserva en ECO-48. No se libera la versión ni se cierra la épica por completar los documentos.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| V_1_0_0 | 25/10/2026 | Actualización de versión, evidencias y trazabilidad documental. |
| V_1_0_1 | 25/10/2026 | Actualización de versión, evidencias y trazabilidad documental. |
| V_1_0_2 | 25/10/2026 | Análisis 1.3.0, recorrido técnico registrado y actualización editorial. |
| V_1_0_3 | 25/10/2026 | Revisión técnica, compatibilidad ampliada, responsables nominales y seguimiento actualizado. |
| V_1_0_4 | 25/10/2026 | Regularización administrativa y registro de 30 escenarios oficiales disponible. |
| V_1_0_5 | 25/10/2026 | Incorporación de prueba parcial NVDA sin atribuir conformidad completa. |

[← Volver al README](../../../README.md)
