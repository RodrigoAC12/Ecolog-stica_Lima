[← Volver al README](../../README.md)

# SonarQube Cloud y análisis desde GitHub

**Proyecto:** EcoLogística Lima · **Versión:** 1.3.0 · **Fecha:** 27/10/2026 (Lima).

## Diagnóstico

El análisis automático del 27/10 a las 18:52:35 utilizó `da3eef2`, correspondiente a la base 1.2.4 del fork. Registró 17 problemas de seguridad, seis de fiabilidad, duplicación de 1,4 %, cobertura sin importar y puerta de calidad sin calcular. Ese resultado no correspondía al incremento integrado en el repositorio principal mediante `3f1b4fe`.

Se sincronizó `main` del fork con `3f1b4fe`. El análisis automático posterior, a las 18:59:54, acredita esa revisión. La sincronización elimina la causa del desfase; las correcciones y la importación de cobertura requieren un análisis posterior desde CI.

El [análisis local conservado](<../03 Implementación/Sprint 03/evidencias/sonar-1.3.0.json>) sigue describiendo su revisión y alcance originales. No demuestra por sí solo que Cloud haya aprobado Dockerfiles, workflows y herramientas: Cloud inspecciona un alcance más amplio.

## Cambios preparados

| Hallazgo | Tratamiento |
|---|---|
| Destino de consulta derivado del filtro de pedidos | Lista explícita de estados y rutas constantes; rechazo del valor manipulado antes de llamar a la API. |
| Expresiones regulares con retroceso en enlaces Markdown | Recorrido lineal con soporte de paréntesis, escapes y títulos; pruebas con entrada extensa. |
| Instalación Python sin fijación ni comprobación de integridad | Dependencias y herramientas fijadas con SHA-256; instalación exclusiva de paquetes binarios. |
| Ejecución automática de scripts durante `npm ci` | Instalación con `--ignore-scripts`; compilación explícita posterior. |
| Contenedores con usuario privilegiado y copia general | Usuario sin privilegios y copia de archivos necesarios en cada imagen. |
| Cobertura ausente en Cloud | CI conserva e importa XML de backend y herramientas, y LCOV de frontend. |
| Evidencia de un análisis anterior | Exportador comprueba que la revisión analizada coincide con `GITHUB_SHA`. |

Las cuatro incidencias de botones de formulario del análisis antiguo ya estaban corregidas en Sprint 3. El nuevo análisis debe confirmar el estado final de todas las reglas; la tabla describe el tratamiento realizado, no una aprobación anticipada.

## Configuración de las cuentas

1. Entrar en [SonarQube Cloud](https://sonarcloud.io), abrir el avatar, **My Account → Security**, generar un token y copiarlo. Usar una cuenta con permiso para ejecutar análisis del proyecto.
2. Abrir [los secretos de Actions del fork](https://github.com/RodrigoAC12/Ecolog-stica_Lima/settings/secrets/actions), elegir **New repository secret**, escribir `SONAR_TOKEN` en **Name**, pegar el token en **Secret** y guardar con **Add secret**. No colocarlo en archivos ni mensajes.
3. En [el proyecto Cloud](https://sonarcloud.io/summary/overall?id=RodrigoAC12_Ecolog-stica_Lima&branch=main), abrir **Administration → Analysis Method** y desactivar **Automatic Analysis**. Seleccionar **With GitHub Actions** si aparece el asistente. Si no aparece Administration, iniciar sesión con la cuenta administradora del proyecto.
4. Publicar la revisión en `main` del fork o ejecutar **ECO - CI de calidad → Run workflow**, seleccionando `main`. El trabajo SonarQube Cloud se ejecuta después de documentación y pruebas. La configuración está en [sonar-project.cloud.properties](../../sonar-project.cloud.properties).
5. Comprobar en Actions y Cloud la misma revisión, la cobertura importada, el resultado de la puerta y los problemas abiertos. Descargar `sonarcloud-report` como evidencia. Una ejecución fallida o una puerta sin calcular permanece pendiente.

El secreto `SONAR_TOKEN` ya figura creado en el fork; GitHub no permite recuperar su valor. Su validez se comprueba al ejecutar el análisis.

## Validación y límites

Las comprobaciones locales realizadas incluyen 36 pruebas backend (93,43 % de cobertura de sentencias), 23 pruebas frontend y compilación (93,05 % de cobertura de líneas), y 12 pruebas de herramientas. Los resultados de cobertura de herramientas varían entre Windows y Linux porque DPAPI depende de Windows.

Los archivos de bloqueo Python se resolvieron para Python 3.12 en Linux, entorno utilizado por CI y Docker. Incluyen hashes de los paquetes binarios publicados para cada versión. Para desarrollo en Windows se conserva `requirements.txt`; no instalar el bloqueo Linux como si fuera multiplataforma.

El entorno de operación continúa en localhost. La revisión del cliente o del usuario sigue pendiente. Las dos advertencias y el riesgo de dependencia mostrado en Cloud deben contrastarse con el nuevo análisis y sus detalles; una auditoría sin vulnerabilidades conocidas no equivale automáticamente a eliminar todos los riesgos que muestra Cloud.

Referencia: [configuración oficial de GitHub Actions para SonarQube Cloud](https://docs.sonarsource.com/sonarqube-cloud/analyzing-source-code/ci-based-analysis/github-actions-for-sonarcloud/).
