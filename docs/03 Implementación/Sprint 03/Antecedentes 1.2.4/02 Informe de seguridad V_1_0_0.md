[← Volver al README](../../../../README.md)

# Informe de seguridad — base histórica 1.2.4

> Antecedente histórico de la base 1.2.4, integrado documentalmente al Sprint 3 el 25/10/2026. Se conservan las fechas, resultados y límites del corte original. La entrega vigente es [Sprint 3 — versión 1.3.0](<../../../Versiones/1.3.0.md>), con [evaluaciones y alcance actuales](<../Matriz de entrega y rúbrica V_1_0_0.md>).

**Versión documental:** 1.0.1 · **Versión del proyecto:** 1.2.4 · **Fecha:** 24/10/2026.

## Alcance y método

El proyecto cuenta con controles continuos de seguridad para las funcionalidades existentes de Sprints 1 y 2. Los archivos [CodeQL](../../../../.github/workflows/codeql.yml) y [Auditoría de dependencias](../../../../.github/workflows/dependency-audit.yml) se ejecutaron en la rama histórica `Pre-Sprint-3` y en solicitudes de cambio hacia `main`.

- **CodeQL v4:** análisis de Python y JavaScript/TypeScript con consultas `security-extended`, exportación de SARIF y comprobación de severidad crítica.
- **Python:** `pip-audit` inspecciona las dependencias del backend e informa avisos de seguridad publicados.
- **Frontend:** `npm audit` comprueba las dependencias del lockfile, incluyendo herramientas de desarrollo, con umbral `high`.
- **Integración:** el [CI](../../../../.github/workflows/ci.yml) ejecuta los tests sobre SQLite y PostgreSQL y valida la documentación y la construcción de staging.

## Actualizaciones incorporadas

| Área | Medida | Limitación |
|---|---|---|
| Pruebas Python | Restricción de `pytest >= 9.0.3` | Repetir auditoría si cambia el árbol de dependencias |
| Herramientas frontend | Actualización compatible de Vitest 5, Vite 6.4 y dependencias transitivas | El servidor de desarrollo no es un servidor público |
| Base de datos | URL de prueba validada y transacciones de entidades/auditoría | Comprobar siempre que la base sea desechable |
| Red local | Los puertos de Compose de desarrollo se enlazan a `127.0.0.1` | No equivale a TLS externo ni firewall de producción |
| Staging | Proxy Caddy y red privada para API y PostgreSQL | No se acredita servidor, DNS ni certificado real |

## Evidencias

[GitHub Actions históricos de la base 1.2.4](https://github.com/RodrigoAC12/Ecolog-stica_Lima/actions?query=branch%3APre-Sprint-3) conserva los resultados y artefactos JSON/SARIF. Registrar fecha y SHA concreto de la ejecución de la versión aprobada. Un workflow exitoso **no garantiza** que no existan vulnerabilidades desconocidas ni reemplaza la revisión de cada alerta abierta de Code Scanning.

## Validaciones externas y DoD

Continúan sujetas a evidencia real: revisión por un integrante diferente al autor, autorización del propietario, despliegue externo HTTPS/TLS, gestión de secretos, revisión manual de accesibilidad, aceptación BDD y controles de seguridad posteriores. No atribuir estas validaciones a una sesión que no conste documentada.

**Relacionados:** [Informe de integridad y auditoría](<03 Informe de integridad y auditoría V_1_0_0.md>) · [Versión 1.2.4](<../../../Versiones/1.2.4.md>) · [Checklist](<../../../Calidad/02 Checklist de validación.md>).

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.1 | 25/10/2026 | Integración de antecedentes en Sprint 03, retiro de la etapa separada y enlaces actualizados. |
