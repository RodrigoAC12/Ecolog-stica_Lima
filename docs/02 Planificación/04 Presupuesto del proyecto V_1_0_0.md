[← Volver al README Principal](../../README.md)

# Presupuesto del proyecto — EcoLogística Lima

| Campo | Detalle |
|---|---|
| **Proyecto** | EcoLogística Lima – Optimizador de Rutas Sostenibles para DistriRápido S.A.C. |
| **Fase** | 02 – Planificación del Proyecto |
| **Versión** | 1.0.0 |
| **Fecha de elaboración** | 23/10/2026 |
| **Moneda principal** | USD (según consigna de planificación) |
| **Escenario económico** | Proyección referencial académica del costo de desarrollo del MVP; no corresponde a desembolsos reales ni a cotizaciones aceptadas |
| **Horizonte** | 14 semanas de proyecto; 4 meses equivalentes para aprovisionamiento de servicios |

> **Advertencia metodológica.** Las tarifas, horas, licencias, precios de nube y el tipo de cambio usados a continuación son **supuestos de modelamiento** elegidos para construir un presupuesto verificable. **No** están respaldados por nóminas, facturas ni ofertas de proveedores. Deben revisarse y aprobarse por el equipo antes de constituir una línea base de gasto real. El proyecto es académico y la empresa de referencia es un escenario simulado.

## 1. Objetivo, alcance y línea base de referencia

El objetivo es estimar de forma desagregada los recursos humanos (CAPEX en la clasificación exigida por la consigna), licencias, infraestructura cloud (OPEX) y contingencia de la plataforma logística. Se contemplan los módulos de gestión de pedidos, vehículos, conductores y clientes, así como los componentes **futuros** previstos: optimización/re-optimización, mapas, indicadores y sostenibilidad. Su inclusión financiera no significa que hayan sido implementados.

La [Acta de Constitución](../01%20Inicio/02.%20Acta%20de%20constituci%C3%B3n%20V_1_0_0.md) fija un **techo máximo de S/ 500,000** para el MVP, **14 semanas** y un escenario separado de **S/ 120,000 anuales** de operación y soporte posterior. El [Registro de Supuestos y Restricciones](../01%20Inicio/04.%20Registro%20de%20supuestos%20y%20restricciones%20V_1_0_0.md) confirma el techo económico; este informe **no lo reemplaza**. Es una estimación de abajo hacia arriba para comparar con ese máximo.

**Hipótesis principales:** (a) cinco integrantes pueden asumir varios roles sin equivaler a ocho contrataciones distintas; (b) las horas por rol no representan partes de trabajo ya ejecutados, sino dedicación económica estimada; (c) los servicios se valorizan durante cuatro meses para cubrir las 14 semanas y un margen de configuración; (d) tipo de cambio **hipotético S/ 3.75 por USD**, usado solo para comparar con el techo expresado en soles; (e) las tarifas son costos de oportunidad de trabajo profesional, aunque el desarrollo estudiantil podría no generar pagos salariales.

## 2. Recursos humanos — CAPEX

**Fórmula:** `Costo por rol (USD) = Horas asignadas × Tarifa hora (USD)`; las horas no deben sumarse como jornadas de una sola persona.

| Rol | Horas estimadas | Tarifa USD/h | Costo USD | Actividad principal |
|---|---:|---:|---:|---|
| Dirección del proyecto (Project Manager) | 140 | 30.00 | **4,200.00** | Gestión de cronograma, entregables, riesgos y coordinación |
| Arquitectura de software (Software Architect) | 180 | 35.00 | **6,300.00** | Diseño técnico, APIs, modelo de datos y arquitectura de optimización |
| Desarrollo backend y optimización | 280 | 26.00 | **7,280.00** | API FastAPI, reglas de negocio y motor de rutas proyectado |
| Desarrollo frontend | 240 | 24.00 | **5,760.00** | React, formularios, mapas y tableros previstos |
| QA, seguridad y pruebas | 180 | 24.00 | **4,320.00** | Automatización, cobertura, OWASP, accesibilidad y pruebas |
| Diseño UI/UX | 120 | 22.00 | **2,640.00** | Prototipos, experiencia de usuario y diseño accesible |
| Base de datos e integración | 120 | 25.00 | **3,000.00** | PostgreSQL, migraciones, integración de datos y geocodificación |
| Análisis funcional y documentación | 100 | 20.00 | **2,000.00** | BDD, trazabilidad, documentación y apoyo a la aceptación |
| **Total recursos humanos** | **1,360** | — | **35,500.00** | Distribución de roles entre el equipo por definir |

**Criterio de capacidad:** 1,360 horas agregadas / 14 semanas = aproximadamente 97.1 horas-persona semanales; repartidas equitativamente entre cinco integrantes equivaldrían a 19.4 horas semanales por integrante. Es un escenario de planificación, no una asignación confirmada de responsables.

## 3. Licenciamiento de software y herramientas

Se prioriza software de código abierto; se incluyen provisiones para herramientas de gestión, diseño y análisis. Si el equipo opera con planes gratuitos, el gasto de caja podría ser inferior. **No se presenta ningún precio como tarifa oficial del proveedor.**

| Licencia/herramienta | Cantidad | Supuesto USD/unidad/periodo | Periodos | Subtotal USD |
|---|---:|---:|---:|---:|
| Atlassian Jira, 5 cuentas (supuesto de pago) | 5 | 8.00 (USD/usuario/mes) | 4 | 160.00 |
| Figma, 1 editor (supuesto de pago) | 1 | 15.00 (USD/editor/mes) | 4 | 60.00 |
| SonarQube/SonarCloud, cuota reservada (supuesto) | 1 | 65.00 (USD/mes) | 4 | 260.00 |
| GitHub, Git, VS Code, Python y bibliotecas libres | 1 | 0.00 (USD/mes (escenario sin plan de pago)) | 4 | 0.00 |
| **Total licencias y herramientas** | — | — | — | **480.00** |

## 4. Infraestructura cloud y servicios — OPEX de desarrollo

**Fórmula:** `Costo servicio (USD) = Cantidad × Tarifa estimada × Meses` (o una anualidad cuando se indique). El despliegue público y los servicios de mapas son presupuestados a futuro; el repositorio observado contiene por ahora configuración **local de desarrollo con Docker Compose**.

| Servicio | Cantidad | Supuesto USD/unidad/periodo | Periodos | Subtotal USD |
|---|---:|---:|---:|---:|
| Aplicación y API: instancia de pruebas | 1 | 100.00 (USD/mes) | 4 | 400.00 |
| Entorno staging independiente | 1 | 80.00 (USD/mes) | 4 | 320.00 |
| PostgreSQL gestionado de prueba | 1 | 120.00 (USD/mes) | 4 | 480.00 |
| Respaldos y almacenamiento | 1 | 30.00 (USD/mes) | 4 | 120.00 |
| Mapas/geocodificación/tráfico: provisión | 1 | 60.00 (USD/mes) | 4 | 240.00 |
| CI/CD: cuota de cómputo adicional | 1 | 30.00 (USD/mes) | 4 | 120.00 |
| Registro, métricas y monitoreo | 1 | 40.00 (USD/mes) | 4 | 160.00 |
| Dominio web: provisión anual | 1 | 20.00 (USD/año) | 1 | 20.00 |
| Certificado TLS automatizado | 1 | 0.00 (USD/año (escenario gratuito)) | 1 | 0.00 |
| **Total infraestructura / servicios** | — | — | — | **1,860.00** |

**Distinción temporal:** el gasto de infraestructura de esta tabla se refiere a desarrollo/staging dentro del horizonte del MVP. Los **S/ 120,000 anuales** de mantenimiento y soporte posterior registrados en el Acta constituyen un escenario operativo separado que **no se suma** al presupuesto de construcción para evitar doble conteo entre periodos.

## 5. Reserva de contingencia e identificación de riesgos

Se adopta una **reserva del 12% del subtotal**, dentro del 10–15% recomendado por la consigna de planificación, como provisión presupuestaria frente a la matriz de riesgos. `Reserva = 37,840.00 × 12% = 4,540.80 USD`.

La reserva atiende eventualidades sujetas a control de cambios, por ejemplo: **RSK-01/RSK-02** (rendimiento del optimizador), **RSK-03** (servicios de mapas/tráfico), **RSK-07/RSK-08** (vulnerabilidades y permisos), **RSK-10** (estimaciones y calendario), según el [Registro de riesgos](03%20Registro%20de%20riesgos%20V_1_0_0.md). Los riesgos no significan que esos eventos hayan ocurrido.

**Conciliación con el Acta:** el Acta distribuye S/ 25,000 para contingencia (5% de su **techo** de S/ 500,000), mientras este presupuesto utiliza 12% del **subtotal estimado**. La reserva aquí equivale a **S/ 17,028.00**, menor que aquellos S/ 25,000. Las bases de cálculo son distintas y se indican explícitamente; el techo global se conserva. Una futura ampliación que haga rebasar la reserva asignada al techo exigiría aprobación y revisión de la línea base.

## 6. Tabla resumen financiera

| Categoría | Subtotal USD | % del total estimado | Equivalente PEN* |
|---|---:|---:|---:|
| 1. Recursos Humanos (CAPEX) | 35,500.00 | 83.76% | S/ 133,125.00 |
| 2. Licenciamiento de software | 480.00 | 1.13% | S/ 1,800.00 |
| 3. Infraestructura Cloud (OPEX) | 1,860.00 | 4.39% | S/ 6,975.00 |
| **SUBTOTAL DEL PROYECTO** | **37,840.00** | **89.29%** | **S/ 141,900.00** |
| 4. Reserva de contingencia (**12% del subtotal**) | 4,540.80 | 10.71% | S/ 17,028.00 |
| **PRESUPUESTO TOTAL ESTIMADO** | **USD 42,380.80** | **100.00%** | **S/ 158,928.00** |

*Tipo de cambio de simulación: **USD 1 = S/ 3.75**. No representa una cotización vigente ni fija obligaciones reales. Porcentajes calculados sobre el **total con contingencia**; el subtotal representa 100% únicamente cuando se presenta como base de cálculo previa a la reserva.*

### Control del techo máximo del MVP

| Indicador | Resultado |
|---|---:|
| Techo de inversión previsto en el Acta | S/ 500,000.00 |
| Presupuesto total de este escenario (incluye contingencia) | S/ 158,928.00 |
| Margen restante frente al techo (no comprometido) | S/ 341,072.00 |
| Consumo teórico del techo | 31.79% |

El margen no comprometido **no constituye ahorro realizado** y no habilita automáticamente nuevas funcionalidades. Diferencias frente a los porcentajes generales del Acta proceden de este presupuesto detallado por rol/servicio; antes de adoptar esta proyección como línea base oficial el equipo debe validar su alcance y distribución.

## 7. Gestión presupuestal, seguimiento y aprobación

1. **Validación inicial:** contrastar horas estimadas con el Product Backlog, Story Points y las cuatro iteraciones del Acta; confirmar las tarifas ficticias con el criterio de evaluación del docente.
2. **Cotización y factibilidad:** verificar disponibilidad de planes gratuitos y obtener precios reales de Jira, SonarQube/SonarCloud, hosting, Postgres, tráfico/mapas y dominio antes de comprometer fondos.
3. **Control por sprint:** registrar `Planificado (USD)`, `Comprometido (USD)`, `Ejecutado (USD)`, `Variación` y justificación al cierre de cada iteración; no rellenar ejecutados sin evidencia.
4. **Riesgo y contingencia:** cualquier uso de reserva exige causa, riesgo asociado, importe, decisión del responsable y efecto sobre el margen frente al techo.
5. **Gobierno:** no modificar el techo de S/ 500,000 ni la línea base de 14 semanas sin acuerdo y aprobación documentados; separar los supuestos académicos de acuerdos efectivos de la empresa simulada.
6. **Cierre financiero:** presentar conciliación con registros de desembolsos únicamente si existen; de lo contrario etiquetar las cifras como *estimadas*.

## 8. Trazabilidad documental

- [Acta de Constitución — cronograma, techo y contingencia histórica](../01%20Inicio/02.%20Acta%20de%20constituci%C3%B3n%20V_1_0_0.md)
- [Registro de supuestos y restricciones — límite C2](../01%20Inicio/04.%20Registro%20de%20supuestos%20y%20restricciones%20V_1_0_0.md)
- [Registro de riesgos — matriz de 16 riesgos](03%20Registro%20de%20riesgos%20V_1_0_0.md)
- [Transformando a ágil — épicas, historias y enablers](01%20Transformando%20a%20%C3%A1gil%20V_1_0_1.md)
- [Artefactos Jira — backlog, roadmap, Sprint Goal y release](02%20Artefactos%20Jira%20V_1_0_2.md)

## 9. Historial de control de cambios

| Versión | Fecha | Descripción |
|---|---|---|
| **1.0.0** | **23/10/2026** | Primera propuesta de presupuesto académico desagregado en USD, reconciliado con el techo de S/ 500,000 y la referencia anual de soporte del Acta; tarifas y tipo de cambio explícitamente hipotéticos. |

[← Volver al README Principal](../../README.md)