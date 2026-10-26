[← Volver al README](../../README.md)

# Compatibilidad de navegadores — Sprint 3

**Versión documental:** 1.0.0 · **Proyecto:** 1.3.0 · **Fecha:** 25/10/2026 (Lima).<br>
**Responsable de seguimiento:** Luis Antony Gonzalo Guerrero.

## Recursos y alcance

La [matriz consolidada](<../03 Implementación/Sprint 03/evidencias/compatibilidad-1.3.0.json>) evalúa Chrome for Testing 156.0.8078.47 y 155.0.8059.84, Microsoft Edge 156.0.4314.42 y 155.0.4283.62, y Firefox 158.0.1 y 157.0.1 en Windows. La selección toma la versión estable y la familia mayor estable anterior; no pretende probar todos los parches publicados ni versiones futuras.

| Recurso | Uso | Ubicación o fuente |
|---|---|---|
| Node.js, dependencias frontend y `.venv` backend | Iniciar aplicación y API aisladas | Preparación habitual del repositorio |
| Selenium WebDriver 4 | Controlar navegadores oficiales mediante sus drivers | Dependencia de herramientas en `tmp/browser-tools`; no se incorpora al producto |
| ChromeDriver y Chrome for Testing | Dos familias de Chrome con versiones correspondientes | [Catálogo estable](https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json) y [catálogo por versión mayor](https://googlechromelabs.github.io/chrome-for-testing/latest-versions-per-milestone-with-downloads.json) |
| Microsoft Edge y EdgeDriver | Dos familias de Edge con driver compatible | [Catálogo oficial](https://edgeupdates.microsoft.com/api/products?view=enterprise) y [WebDriver de Microsoft](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) |
| Firefox y GeckoDriver | Versiones estables de Firefox con perfiles nuevos | [Versión vigente](https://product-details.mozilla.org/1.0/firefox_versions.json), [historial](https://product-details.mozilla.org/1.0/firefox_history_stability_releases.json) y [GeckoDriver](https://github.com/mozilla/geckodriver/releases) |
| axe-core | Comprobar criterios automáticos y registrar resultados incompletos | Dependencia frontend existente |
| JSON y capturas | Conservar resultados verificables sin sesiones personales | `docs/03 Implementación/Sprint 03/evidencias/` |

Los navegadores descargados, drivers, instaladores y perfiles se guardan en `tmp/`, excluido de Git. Las copias de evaluación no sustituyen las instalaciones personales. El MSI de Edge 155 se verificó contra el SHA-256 publicado por Microsoft y se extrajo para ejecutar su binario sin instalar otra versión del navegador del usuario.

## Reproducción

1. Preparar dependencias del frontend y backend según el README. Instalar las herramientas separadas con `npm install --prefix tmp/browser-tools selenium-webdriver`.
2. Preparar los seis binarios y drivers oficiales. Crear `tmp/browser-matrix.json` con una entrada por versión. Cada entrada contiene `id`, `family`, `version`, `binary`, `driver` y `source`; `binary` y `driver` deben ser rutas completas a los ejecutables disponibles. `family` admite `chrome`, `MicrosoftEdge` y `firefox`.
3. Desde la raíz, ejecutar `node scripts/verify_browser_matrix.mjs tmp/browser-matrix.json`.
4. El [script](../../scripts/verify_browser_matrix.mjs) crea su propia SQLite, credenciales aleatorias y procesos de aplicación/API en 127.0.0.1:5175/8003. Esos puertos deben estar libres; los procesos propios se detienen al finalizar.
5. Leer el resultado y las capturas. Una comprobación fallida produce un resultado fallido y salida no satisfactoria; no se convierte en aprobación por omitir el error. Un nuevo recorrido sobrescribe el JSON de trabajo: conservar y distinguir los cortes que se utilicen en el informe.

En Chromium el tamaño del contenido se fija mediante CDP y en Firefox mediante WebDriver BiDi, evitando confundir el ancho mínimo de una ventana de escritorio con un viewport de 360 px. Se utilizan eventos de teclado para los campos de texto; las fechas y selecciones se establecen con sus eventos de formulario. Los cambios se comprueban contra la API real y el listado resultante.

## Resultado y límites

Cada versión aprobó 84 comprobaciones en 13 estados. En total: seis versiones, 78 estados, 504 comprobaciones y 3.258 ocurrencias de contraste sin infracciones automáticas en el alcance aprobado. Los datos de evaluación crecen dentro de la base exclusiva del recorrido; por eso las ocurrencias de texto no son idénticas entre todas las sesiones.

La evidencia consolidada identifica un reintento de Chrome 155 tras ajustar la espera del fin de envío y actualización del listado. El código de la aplicación se mantiene igual entre el recorrido conjunto final y ese reintento. El [corte anterior](<../03 Implementación/Sprint 03/evidencias/compatibilidad-antes-lecturas.json>) conserva sus resultados; no se declara una única ejecución sin fallos.

La [evaluación WCAG](<../03 Implementación/Sprint 03/05 WCAG V_1_0_0.md>) documenta los cuatro principios, los hallazgos y las correcciones. La revisión del cliente o del usuario sigue pendiente, incluida la comprensión con lector de pantalla. La comprobación de NVDA 2026.2 no quedó acreditada porque el control de Windows se interrumpió al no verificar la URL; no se presenta como prueba aprobada.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 25/10/2026 | Seis versiones, herramientas separadas, procedimiento, resultados y límites. |

[← Volver al README](../../README.md)
