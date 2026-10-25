[← Volver al README](../../../README.md)

# Evaluación de Calidad de Código — SonarQube

**Nombre del Proyecto:** EcoLogística Lima<br>
**Fecha de Análisis:** 2026-10-25, 02:03:48 (America/Lima).<br>
**Versión documental:** V_1_0_4 · **Versión del proyecto:** 1.3.0<br>
**Versión del Análisis:** V_1_0_3, corte del 25/10/2026 a las 02:03:48 (Lima).<br>
**Herramientas:** SonarQube Community Build 26.10.0.133078, SonarScanner para NPM 5.0.2.<br>
**Revisión Git analizada:** `2af41c1c1b1caa8fbc7c55078fe3b5a7d4a99ef9`, sin cambios sin commit al iniciar el scanner.<br>
**Versión técnica analizada:** `1.3.0`.
**Estado documental:** versión 1.3.0 con evidencias conservadas para revisión.

## 1. Resumen Ejecutivo de Quality Gate

El despliegue se evalúa exclusivamente en localhost conforme a la [adenda del 25/10/2026](<Alcance de validación local V_1_0_0.md>). La [verificación local](evidencias/staging-local.json) se distingue del corte de métricas Sonar identificado a continuación.

- **Estado del Quality Gate:** PASSED.
- **Porcentaje de Cobertura de Pruebas (Coverage):** 92,4 % global en SonarQube; combina líneas y condiciones.
- **Duplicación de Código:** 0,0 %.
- **Cobertura de líneas:** 93,2 %; **cobertura de condiciones:** 88,1 %.
- **Código fuente no comentado:** 1.529 líneas.

El análisis `9874884e-ff57-4dd0-9224-738fa4ab98bd` finalizó con procesamiento `SUCCESS`. Esta ejecución evaluó tres condiciones respecto de `1.2.4-sprint3-final`, sin ignorar ninguna:

| Condición de código nuevo | Umbral aplicado por el servidor | Resultado | Estado |
|---|---|---:|---|
| Cobertura | Al menos 80 % | 100,0 % | Aprobado |
| Duplicación | Como máximo 3 % | 0,0 % | Aprobado |
| Nuevos problemas | 0 | 0 | Aprobado |

**Evidencia vigente:** [sonar-1.3.0.json](evidencias/sonar-1.3.0.json), [cobertura frontend por archivo](evidencias/frontend-cobertura-1.3.0.json), [guía reproducible](<../../Calidad/03 SonarQube local.md>) y [panel local](http://localhost:9000/dashboard?id=ecologistica-lima). Los JSON permiten revisar los resultados sin acceso al servidor de esta PC.

**Antecedentes conservados:** [análisis inicial](../../Calidad/evidencias-sonar/2026-10-24-inicial.json), [primera remediación](../../Calidad/evidencias-sonar/2026-10-24-remediacion.json) y [corte previo a publicar](evidencias/sonar-final.json). El análisis posterior de `cde28d7` (`dfc82560-3601-494b-9ee7-6182c662f80b`) obtuvo 89,9 % global y 95,8 % nuevo; el corte vigente incorpora las nuevas pruebas y no reemplaza retrospectivamente esos valores.

## 2. Métricas Principales

| Categoría | Cantidad inicial | Cantidad tras corrección | Severidad (Bloqueante / Alta / Media / Baja) |
|---|---:|---:|---|
| Bugs | 4 | 0 | Inicial: Media; actual: ninguna pendiente |
| Vulnerabilidades | 0 | 0 | Ninguna detectada por los perfiles activos |
| Code Smells | 0 | 0 | Ninguna detectada por los perfiles activos |
| Security Hotspots | 0 | 0 | No se generaron hotspots para revisar en este corte |

Los cuatro bugs iniciales tienen impacto de fiabilidad `MEDIUM` en la API del servidor, que se presenta como **Media** según la columna solicitada. Su severidad heredada es `MAJOR`. La [evidencia vigente](evidencias/sonar-entrega.json) conserva ambos campos y su resolución `FIXED`.

| Ejecución de pruebas | Resultado | Cobertura y alcance |
|---|---|---|
| Backend local, Python 3.12.13 | 36 aprobadas en SQLite temporal y 36 en PostgreSQL 16 aislado | 93,43 % de líneas; nueve casos adicionales de seguridad; migraciones y ausencia de deriva verificadas |
| Frontend local, Node.js 24.14.1 y Vitest 5.0.5 | 11 aprobadas después de corregir | 92,19 % de líneas; 91,53 % de sentencias; 88,13 % de ramas; 94,82 % de funciones |
| TypeScript y Vite | Compilación aprobada | No sustituye pruebas en navegadores ni aceptación BDD |

Las cifras de Pytest y Vitest tienen denominadores diferentes de SonarQube. La [cobertura por archivo](evidencias/frontend-cobertura-1.3.0.json) acredita 100 % de líneas en los cuatro formularios y 90 % en `App.tsx`; el backend de seguridad alcanza 95 % redondeado en Pytest. Las cuatro pruebas añadidas verifican que cancelar una edición con cambios no provoca escrituras al servidor ni altera el registro original. No se excluyó código para elevar cobertura.

La versión 1.3.0, revisión `3ea875b`, aprobó [CI en Node.js 22](https://github.com/RodrigoAC12/Ecolog-stica_Lima/actions/runs/40169865983), [CodeQL](https://github.com/RodrigoAC12/Ecolog-stica_Lima/actions/runs/40169865979) y [auditoría de dependencias](https://github.com/RodrigoAC12/Ecolog-stica_Lima/actions/runs/40169865986). Los controles de cada nueva revisión se consultan en la rama Sprint-3.

## 3. Plan de Remediación y Deuda Técnica

- **Deuda Técnica Estimada:** el indicador de mantenibilidad `sqale_index` es 0 minutos en ambos cortes; no incluye toda la deuda funcional, operativa o de seguridad del proyecto.
- **Estimación de los hallazgos iniciales:** SonarQube asignó 2 minutos por bug, 8 minutos en total. Es una estimación de herramienta, no horas reales de trabajo ni plazo de validación.
- **Corrección aplicada:** declarar `type="submit"` en los botones de envío y conservar `type="button"` para cancelar, evitando depender del tipo implícito del navegador.

| Hallazgo | Componente | Acción | Comprobación | Estado |
|---|---|---|---|---|
| S9011, botón sin tipo explícito | `ClientForm.tsx:23` | Añadido `type="submit"` | Suite frontend y reanálisis | FIXED |
| S9011, botón sin tipo explícito | `DriverForm.tsx:25` | Añadido `type="submit"` | Suite frontend y reanálisis | FIXED |
| S9011, botón sin tipo explícito | `OrderForm.tsx:33` | Añadido `type="submit"` | Suite frontend y reanálisis | FIXED |
| S9011, botón sin tipo explícito | `VehicleForm.tsx:27` | Añadido `type="submit"` | Suite frontend y reanálisis | FIXED |

La evaluación posterior incorporó dos mejoras adicionales: validación obligatoria de `exp`/`sub` en JWT y gestión de foco al cambiar de pantalla. Las [pruebas de seguridad](../../../src/backend/tests/test_security_assessment.py) y las [evidencias WCAG](evidencias/accesibilidad-final.json) documentan su comprobación. No fueron alertas Sonar inventadas: proceden de pruebas dinámicas y de interacción.

| Seguimiento de deuda y entrega | Acción siguiente | Responsable | Momento de verificación |
|---|---|---|---|
| Cobertura por componente y funciones frontend | Verificación actual: formularios 100 % de líneas y App 90 %; mantener regresiones y priorizar el resto según riesgo | Rodrigo Vladimir Arce Curi | En cada cambio afectado |
| Dependencias y alcance de seguridad | Mantener auditorías Python/npm y evaluación OWASP; el scanner omitió SCA | Jhon Robert Paitan Montes | Informe de seguridad y revisión final |
| Revisión técnica y seguimiento | Revisar código y evidencias; conservar la revisión del cliente o del usuario pendiente | Jhon Robert Paitan Montes y Luis Antony Gonzalo Guerrero | Seguimiento 26/10/2026 |
| Accesibilidad y aceptación | Evaluación WCAG y escenarios BDD con evidencia real | Luis Antony Gonzalo Guerrero y Marco Jhair Martinez Llanos | Revisión del cliente o del usuario pendiente |

No se cambiaron umbrales, perfiles ni exclusiones para resolver los hallazgos. El análisis utiliza los perfiles `Sonar way core` disponibles. Cero vulnerabilidades detectadas no es una certificación de seguridad: el informe OWASP documenta los controles complementarios. El scanner vigente identifica `2af41c1`, recupera la información SCM y analiza un árbol de trabajo limpio; debe repetirse si cambia el código fuente posteriormente. El token temporal se revocó al terminar.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| V_1_0_0 | 24/10/2026 | Informe oficial de los cortes inicial/final, remediación, seguridad, accesibilidad y límites de aceptación. |
| V_1_0_1 | 25/10/2026 | Análisis del commit de entrega, severidad MEDIUM respaldada por API y cobertura de los cuatro formularios. |
| V_1_0_2 | 25/10/2026 | Actualización de versión, evidencias y trazabilidad documental. |
| V_1_0_3 | 25/10/2026 | Análisis 1.3.0, recorrido técnico registrado y actualización editorial. |
| V_1_0_4 | 25/10/2026 | Revisión técnica, compatibilidad ampliada, responsables nominales y seguimiento actualizado. |

[← Volver al README](../../../README.md)
