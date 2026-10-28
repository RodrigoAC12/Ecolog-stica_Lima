[← Volver al README](../../README.md)

# Prueba con lector de pantalla — 1.3.0

**Versión documental:** 1.0.1 · **Fecha:** 25/10/2026 (Lima).<br>
**Resultado:** APROBADA en el alcance técnico descrito: 53/53 comprobaciones, cero fallos y 74 anuncios reales.<br>
**Herramientas:** NVDA 2026.2 AMD64 y Microsoft Edge 156.0.4314.42 en Windows 11.

Se ejecutó NVDA real sobre la aplicación en localhost, con API, SQLite y operador sintéticos exclusivos de la prueba. Se utilizaron perfiles nuevos del navegador y de NVDA. La extensión de solo lectura recoge el evento oficial `pre_speech`: registra lo que NVDA genera antes de sintetizarlo, sin producir ni sustituir anuncios. El sintetizador silencioso permite verificar el contenido textual; no acredita pronunciación, calidad acústica ni comprensión de una persona.

## Resultado comprobado

La [evidencia final](<../03 Implementación/Sprint 03/evidencias/lector-pantalla-1.3.0.json>) identifica fechas, 53 comprobaciones, 74 anuncios reales y hashes de siete archivos. Los hashes se conciliaron con el código registrado en `647f0a2`, sin cambios posteriores de aplicación. El recorrido final se ejecutó aproximadamente entre las 16:58 y las 17:00 (Lima).

| Grupo | Comprobaciones | Resultado |
|---|---:|---|
| Acceso, enlace de salto, campos protegidos, error e Inicio | 6 | Aprobado |
| Navegación y anuncio del contenido correcto de cuatro módulos | 8 | Aprobado |
| Campos y botones de los formularios de vehículos, pedidos, conductores y clientes | 37 | Aprobado |
| Registro de cliente anunciado y regreso al acceso al cerrar sesión | 2 | Aprobado |
| **Total** | **53** | **53 aprobadas; cero fallos** |

Se comprobaron nombres, campos requeridos, valores iniciales de selectores, controles numéricos, fechas y campos multilínea. La navegación se activa por Enter tras enfocar el botón; los controles se enfocan individualmente mediante el navegador. Los dos pasos Tab del acceso también quedan registrados. No se presenta este método como un recorrido manual completo de teclado realizado por una persona.

Son 53 comprobaciones del recorrido definido, no 53 criterios WCAG ni todas las operaciones de las quince historias. El éxito dinámico probado con lector corresponde al registro de cliente; la regresión funcional y la demostración de las demás operaciones conservan sus evidencias propias.

## Hallazgos y correcciones verificadas

| Observación real | Corrección | Verificación final |
|---|---|---|
| NVDA podía leer el contenido anterior o «en blanco» al cambiar de módulo | Región principal con nombre de la vista y un nodo renovado al cambiar de pantalla | Cada destino se anuncia con su propio nombre y región; no se acepta el nombre de la pantalla anterior |
| El mensaje de registro aparecía visualmente, sin anuncio capturado | Región `status` persistente y atómica cuyo contenido se actualiza | «Cliente registrado.» anunciado sin dirigir el foco a la notificación |
| El cierre de sesión no anunciaba el regreso al acceso | Foco al contenido al salir y región principal «Acceso» identificada | «Acceso principal región» y contenido del formulario anunciados |

Se conservan el [intento inicial interrumpido](<../03 Implementación/Sprint 03/evidencias/lector-pantalla-inicial-1.3.0.json>) y el [recorrido anterior a las correcciones](<../03 Implementación/Sprint 03/evidencias/lector-pantalla-antes-correcciones-1.3.0.json>), con 50/53 comprobaciones aprobadas. Los intentos fallidos no se reescriben como aprobados.

La repetición final con las correcciones aprobó las 53 comprobaciones. La suite de 11 pruebas frontend y la compilación aprobaron; axe repitió 13 estados, 16 interacciones y 437 comprobaciones de contraste sin fallos.

## Alcance pendiente de la revisión del cliente o del usuario

La prueba técnica de NVDA está aprobada en la combinación y los escenarios identificados. Permanecen pendientes pronunciación y calidad acústica, comprensión por una persona, observaciones y aceptación de los escenarios y Done. Coordina Marco Jhair Martinez Llanos, con apoyo de Luis Antony Gonzalo Guerrero. No se declara conformidad universal WCAG AA ni aceptación recibida.

## Recursos y reproducción del alcance comprobado

- NVDA portable ya disponible; no se instala ni se sustituye una sesión personal.
- Microsoft Edge, Node.js, dependencias Playwright del frontend y entorno `.venv` del backend.
- Puertos locales 8004/5176 libres y directorio temporal excluido de Git.
- [Ejecutor del recorrido](../../scripts/verify_screen_reader.mjs) y [capturador de salida NVDA](../../scripts/nvda_speech_capture.py).

Desde la raíz, ejecutar `node scripts/verify_screen_reader.mjs`. El ejecutor utiliza la ruta fija `tmp/browser-tools/nvda/nvda.exe`, comprueba que no haya NVDA personal activo, usa un perfil scratchpad desechable, inicia sus servicios propios y los detiene al terminar. Su alcance son las 53 comprobaciones técnicas descritas; no sustituye la revisión del cliente o del usuario. El complemento utiliza el [mecanismo de desarrollo documentado por NV Access](https://download.nvaccess.org/releases/2026.2/documentation/developerGuide.html).

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 25/10/2026 | Seis comprobaciones con salida real de NVDA, interrupción y alcance pendiente documentados. |
| 1.0.1 | 25/10/2026 | Recorrido de 53 comprobaciones aprobado tras corregir anuncios, región principal y cierre de sesión. |

[← Volver al README](../../README.md)
