[← Volver al README](../../README.md)

# Prueba con lector de pantalla — 1.3.0

**Versión documental:** 1.0.0 · **Fecha:** 25/10/2026 (Lima).<br>
**Resultado:** parcial; recorrido integral pendiente.<br>
**Herramientas:** NVDA 2026.2 AMD64 y Microsoft Edge 156.0.4314.42 en Windows 11.

Se ejecutó NVDA real sobre la aplicación en localhost, con API, SQLite y operador sintéticos exclusivos de la prueba. Se utilizaron perfiles nuevos del navegador y de NVDA. La extensión de solo lectura recoge el evento oficial `pre_speech`: registra lo que NVDA genera antes de sintetizarlo, sin producir ni sustituir anuncios. El sintetizador silencioso permite verificar el contenido textual; no acredita pronunciación, calidad acústica ni comprensión de una persona.

## Resultado comprobado

La [evidencia original](<../03 Implementación/Sprint 03/evidencias/lector-pantalla-1.3.0.json>) conserva marcas de tiempo, anuncios, versión del navegador y hashes de los archivos de la aplicación. El recorrido comenzó aproximadamente a las 16:31 (Lima).

| Comprobación | Salida real de NVDA, extracto | Resultado |
|---|---|---|
| Enlace de salto | «Saltar al contenido» | Comprobado |
| Correo de acceso | «Correo electrónico edición requerido» | Comprobado |
| Contraseña por Tab | «Contraseña edición contraseña requerido»; contenido enmascarado | Comprobado |
| Botón por Tab | «Ingresar botón» | Comprobado |
| Error de acceso, sin dirigir el foco a la alerta | «alerta Credenciales inválidas» | Comprobado |
| Entrada a Inicio | «principal región» y contenido del panel Inicio | Comprobado |

Los seis resultados corresponden a la salida real del lector, no a una inferencia basada únicamente en las etiquetas del documento HTML.

## Interrupción y continuación pendiente

Después del acceso, el recorrido ampliado dejó de producir anuncios capturados. La inspección de la ventana se interrumpió porque la herramienta de control de Windows no pudo determinar la URL con suficiente certeza. Se detuvieron los procesos exclusivos de la prueba. No se declara que la ausencia de anuncios pruebe un defecto de la aplicación ni que el recorrido integral haya aprobado.

Queda por comprobar con NVDA el recorrido de vehículos, pedidos, conductores y clientes: etiquetas y valores, selectores, campos de fecha y multilínea, anuncios de éxito y continuidad del foco durante operaciones completas. La pronunciación, comprensión y aceptación forman parte de la **revisión del cliente o del usuario**, pendiente a cargo de Marco Jhair Martinez Llanos, con apoyo de Luis Antony Gonzalo Guerrero.

Los resultados automáticos de axe y de seis versiones de navegadores conservan su alcance propio. Ninguno convierte esta prueba parcial en conformidad universal WCAG AA.

## Recursos y reproducción del alcance comprobado

- NVDA portable ya disponible; no se instala ni se sustituye una sesión personal.
- Microsoft Edge, Node.js, dependencias Playwright del frontend y entorno `.venv` del backend.
- Puertos locales 8004/5176 libres y directorio temporal excluido de Git.
- [Ejecutor del acceso](../../scripts/verify_screen_reader.mjs) y [capturador de salida NVDA](../../scripts/nvda_speech_capture.py).

Desde la raíz, ejecutar `node scripts/verify_screen_reader.mjs RUTA_ABSOLUTA_A_NVDA_EXE`. El ejecutor comprueba que no haya NVDA personal activo, usa un perfil scratchpad desechable, inicia sus servicios propios y los detiene al terminar. Su alcance son las seis comprobaciones de acceso e Inicio: no sustituye el recorrido restante. El complemento utiliza el [mecanismo de desarrollo documentado por NV Access](https://download.nvaccess.org/releases/2026.2/documentation/developerGuide.html).

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 25/10/2026 | Seis comprobaciones con salida real de NVDA, interrupción y alcance pendiente documentados. |

[← Volver al README](../../README.md)
