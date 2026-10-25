[← Volver al README](../../../README.md)

# Evaluación de Calidad de Código — SonarQube

**Nombre del Proyecto:** EcoLogística Lima<br>
**Fecha de Análisis:** 2026-10-24, 23:39:58 (America/Lima)
**Versión del Análisis:** V_1_0_0<br>
**Herramientas:** SonarQube Community Build 26.10.0.133078, SonarScanner para NPM 5.0.2.<br>
**Base Git:** `da3eef2d037d38d62dd09c6e09792951df204b67`, con cambios locales sin publicar.<br>
**Versión técnica analizada:** `1.2.4-sprint3-final`.
**Estado documental:** informe del corte técnico indicado; actualizar si cambia el código evaluado antes de la entrega.

## 1. Resumen Ejecutivo de Quality Gate

- **Estado del Quality Gate:** PASSED.
- **Porcentaje de Cobertura de Pruebas (Coverage):** 89,9 % global en SonarQube; combina líneas y condiciones.
- **Duplicación de Código:** 0,0 %.
- **Cobertura de líneas:** 91,3 %; **cobertura de condiciones:** 83,1 %.
- **Código fuente no comentado:** 1.532 líneas.

El análisis `27f7541e-5ee3-474a-9461-d27b17198d8f` finalizó con procesamiento `SUCCESS`. A diferencia de la primera línea base, esta ejecución evaluó tres condiciones respecto de `1.2.4-sprint3-remediacion`, sin ignorar ninguna:

| Condición de código nuevo | Umbral aplicado por el servidor | Resultado | Estado |
|---|---|---:|---|
| Cobertura | Al menos 80 % | 100,0 % | Aprobado |
| Duplicación | Como máximo 3 % | 0,0 % | Aprobado |
| Nuevos problemas | 0 | 0 | Aprobado |

**Evidencias:** [análisis inicial](../../Calidad/evidencias-sonar/2026-10-24-inicial.json), [primera remediación](../../Calidad/evidencias-sonar/2026-10-24-remediacion.json), [análisis final del incremento](evidencias/sonar-final.json), [guía reproducible](<../../Calidad/03 SonarQube local.md>) y [panel del servidor local](http://localhost:9000/dashboard?id=ecologistica-lima). El panel solo funciona donde sea accesible este servidor; los archivos JSON conservan los resultados para revisión desde el repositorio.

## 2. Métricas Principales

| Categoría | Cantidad inicial | Cantidad tras corrección | Severidad pendiente |
|---|---:|---:|---|
| Bugs | 4 | 0 | Ninguna detectada en este corte |
| Vulnerabilidades | 0 | 0 | Ninguna detectada por los perfiles activos |
| Code Smells | 0 | 0 | Ninguna detectada por los perfiles activos |
| Security Hotspots | 0 | 0 | No se generaron hotspots para revisar en este corte |

Los cuatro bugs iniciales tenían severidad nativa `MAJOR`; no se convierten arbitrariamente a la escala Bloqueante/Alta/Media/Baja de la plantilla. Todos quedaron cerrados por el reanálisis como `FIXED`.

| Ejecución de pruebas | Resultado | Cobertura y alcance |
|---|---|---|
| Backend local, Python 3.12.13 | 36 aprobadas en SQLite temporal y 36 en PostgreSQL 16 aislado | 93,43 % de líneas; nueve casos adicionales de seguridad; migraciones y ausencia de deriva verificadas |
| Frontend local, Node.js 24.14.1 y Vitest 5.0.5 | 7 aprobadas después de corregir | 83,41 % de líneas; 83,07 % de sentencias; 83,05 % de ramas; 79,31 % de funciones |
| TypeScript y Vite | Compilación aprobada | No sustituye pruebas en navegadores ni aceptación BDD |

Las cifras de Pytest y Vitest tienen definiciones y denominadores diferentes de SonarQube. La cobertura global no acredita por sí sola 80 % en cada módulo afectado: los formularios tienen cobertura menor y requieren revisar el DoD por cambio. El CI del proyecto utiliza Node.js 22; falta validar la revisión publicada en ese entorno.

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
| Cobertura por componente y funciones frontend | Priorizar escenarios no cubiertos según riesgo, sin excluir código para elevar métricas | Por asignar en Jira | Antes de declarar DoD completo |
| Dependencias y alcance de seguridad | Mantener auditorías Python/npm y evaluación OWASP; el scanner omitió SCA | Por asignar en Jira | Informe de seguridad y revisión final |
| Revisión independiente y publicación | Revisar PR, ejecutar CI y analizar la revisión definitiva | Revisor técnico por confirmar | Antes de integrar |
| Accesibilidad y aceptación | Evaluación WCAG y escenarios BDD con evidencia real | Equipo e interesados por confirmar | Antes del cierre del sprint |

No se cambiaron umbrales, perfiles ni exclusiones para resolver los cuatro hallazgos. El análisis utiliza los perfiles `Sonar way core` disponibles en esta instalación. Cero vulnerabilidades detectadas no es una certificación de seguridad: se documentan las comprobaciones adicionales en el informe OWASP. Los cambios locales generan advertencias de información `blame` incompleta; la revisión definitiva debe analizarse de nuevo después de publicar.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| V_1_0_0 | 24/10/2026 | Informe oficial de los cortes inicial/final, remediación, seguridad, accesibilidad y límites de aceptación. |

[← Volver al README](../../../README.md)
