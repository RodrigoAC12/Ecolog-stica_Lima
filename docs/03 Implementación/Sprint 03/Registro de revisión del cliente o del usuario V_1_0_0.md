[← Volver al README](../../../README.md)

# Registro de revisión del cliente o del usuario — Sprint 3

**Versión documental:** V_1_0_0 · **Proyecto:** EcoLogística Lima 1.3.0 · **Preparado:** 25/10/2026 (Lima).

**Estado: pendiente de revisión del cliente o del usuario.** Este registro contiene los 30 escenarios oficiales de US-001 a US-015 y campos para documentar el resultado cuando se realice la revisión. No registra una presentación ni una aprobación recibida.

**Coordinación:** Marco Jhair Martinez Llanos. **Apoyo funcional y accesibilidad:** Luis Antony Gonzalo Guerrero. **Soporte de API:** Jhon Robert Paitan Montes. **Entorno:** Rodrigo Vladimir Arce Curi. **Consolidación documental:** Piero Pool Chauris Leguia.

## Datos de la revisión

| Campo | Registro |
|---|---|
| Fecha y hora efectiva | Pendiente |
| Cliente o usuario participante y rol | Pendiente |
| Participantes del equipo | Por registrar |
| Versión y revisión Git presentadas | 1.3.0; confirmar la revisión al presentar |
| Entorno | Localhost; comprobar disponibilidad antes de iniciar |
| Resultado global | Pendiente |

## Preparación técnica disponible

- Aplicación: [localhost](http://localhost:8080) y [HTTPS local](https://localhost:8443). El responsable inicia sesión sin registrar credenciales en el informe.
- [Demostración técnica grabada](evidencias/demostracion-1.3.0.webm), [trazabilidad BDD](<../../Calidad/01 Matriz de pruebas BDD.md>) y [fuente oficial de los escenarios](<../../02 Planificación/01 Transformando a ágil V_1_0_1.md>).
- [Compatibilidad de seis versiones](evidencias/compatibilidad-1.3.0.json), [Sonar](evidencias/sonar-1.3.0.json), [CodeQL](evidencias/codeql-herramientas-final.json) y [HTTPS local](evidencias/staging-local.json).
- Utilizar datos de evaluación y conservar observaciones y resultados; no modificar registros de uso habitual para preparar una evidencia.

## Escenarios a revisar

Para cada escenario, registrar resultado observado, fecha efectiva, evidencia y decisión. Seleccionar Aprobado o Requiere corrección únicamente después de comprobar el escenario con el cliente o el usuario; los resultados técnicos existentes no preseleccionan esa decisión.

### US-001 — Registrar vehículo

**US-001-E1: Registro válido de vehículo**

```gherkin
Dado que el operador logístico está autenticado y dispone de los datos obligatorios de un vehículo
Cuando registra el vehículo con identificador único, capacidad y datos operativos válidos
Entonces el sistema almacena el vehículo y lo deja disponible según el estado registrado
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-001-E2: Rechazo de vehículo inválido**

```gherkin
Dado que el operador logístico está autenticado
Cuando intenta registrar un vehículo sin un dato obligatorio o con un identificador ya existente
Entonces el sistema rechaza el registro e informa los campos que deben corregirse
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-002 — Consultar vehículos de la flota

**US-002-E1: Consulta de flota registrada**

```gherkin
Dado que existen vehículos registrados en la flota
Cuando el operador consulta el listado de vehículos
Entonces el sistema muestra los vehículos con su estado y datos operativos permitidos
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-002-E2: Consulta sin vehículos**

```gherkin
Dado que no existen vehículos registrados
Cuando el operador consulta la flota
Entonces el sistema muestra una lista vacía e informa que no existen vehículos registrados
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-003 — Actualizar información de un vehículo

**US-003-E1: Actualización válida de vehículo**

```gherkin
Dado que existe un vehículo registrado
Cuando el operador modifica capacidad, consumo, factor de emisión o disponibilidad con valores válidos
Entonces el sistema guarda los cambios y presenta la información actualizada
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-003-E2: Actualización con datos inválidos**

```gherkin
Dado que existe un vehículo registrado
Cuando el operador intenta guardar valores fuera de los rangos permitidos
Entonces el sistema rechaza la actualización y conserva los datos anteriores
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-004 — Desactivar vehículo

**US-004-E1: Desactivación de vehículo**

```gherkin
Dado que existe un vehículo activo registrado
Cuando el operador confirma su desactivación
Entonces el sistema cambia su estado a inactivo y lo excluye de nuevas planificaciones
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-004-E2: Desactivación de vehículo inexistente**

```gherkin
Dado que el identificador indicado no corresponde a un vehículo registrado
Cuando el operador solicita desactivarlo
Entonces el sistema rechaza la operación e informa que el vehículo no existe
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-005 — Registrar pedido

**US-005-E1: Registro válido de pedido**

```gherkin
Dado que el operador dispone de los datos obligatorios del pedido
Cuando registra el pedido con ubicación, carga, volumen, ventana de tiempo y prioridad válidos
Entonces el sistema almacena el pedido y lo deja disponible para planificación
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-005-E2: Registro con ventana inválida**

```gherkin
Dado que el operador está registrando un pedido
Cuando ingresa una ventana de tiempo cuyo fin es anterior o igual al inicio
Entonces el sistema rechaza el pedido e informa que la ventana de tiempo es inválida
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-006 — Consultar pedidos registrados

**US-006-E1: Consulta de pedidos**

```gherkin
Dado que existen pedidos registrados
Cuando el operador consulta el listado de pedidos
Entonces el sistema muestra los pedidos con su estado e información operativa permitida
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-006-E2: Consulta sin resultados**

```gherkin
Dado que no existen pedidos que cumplan los filtros seleccionados
Cuando el operador ejecuta la consulta
Entonces el sistema muestra un resultado vacío sin alterar los pedidos existentes
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-007 — Actualizar pedido pendiente

**US-007-E1: Actualización de pedido pendiente**

```gherkin
Dado que existe un pedido en estado editable
Cuando el operador modifica un dato permitido con un valor válido
Entonces el sistema guarda el cambio y utiliza la información actualizada en la siguiente planificación
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-007-E2: Intento de modificar pedido no editable**

```gherkin
Dado que el pedido se encuentra en un estado que no permite edición
Cuando el operador intenta modificarlo
Entonces el sistema rechaza el cambio e informa el motivo
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-008 — Cancelar pedido

**US-008-E1: Cancelación válida de pedido**

```gherkin
Dado que existe un pedido cancelable
Cuando el operador confirma la cancelación
Entonces el sistema cambia el pedido a estado cancelado y lo excluye de nuevas planificaciones
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-008-E2: Cancelación no permitida**

```gherkin
Dado que el pedido se encuentra en un estado no cancelable
Cuando el operador intenta cancelarlo
Entonces el sistema rechaza la operación e informa la restricción aplicable
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-009 — Registrar conductor

**US-009-E1: Registro válido de conductor**

```gherkin
Dado que el operador dispone de los datos obligatorios de un conductor
Cuando registra al conductor con información válida
Entonces el sistema almacena el conductor y lo deja disponible según su estado
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-009-E2: Registro inválido de conductor**

```gherkin
Dado que el operador intenta registrar un conductor
Cuando omite un dato obligatorio o ingresa un identificador duplicado
Entonces el sistema rechaza el registro e informa la causa
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-010 — Consultar conductores

**US-010-E1: Consulta de conductores**

```gherkin
Dado que existen conductores registrados
Cuando el operador consulta el listado
Entonces el sistema muestra los conductores y su disponibilidad
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-010-E2: Consulta sin conductores disponibles**

```gherkin
Dado que existen conductores pero ninguno está disponible
Cuando el operador filtra por disponibilidad
Entonces el sistema muestra un resultado vacío e informa que no hay conductores disponibles
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-011 — Actualizar información de conductor

**US-011-E1: Actualización válida de conductor**

```gherkin
Dado que existe un conductor registrado
Cuando el operador modifica datos permitidos con valores válidos
Entonces el sistema guarda los cambios y refleja la nueva condición
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-011-E2: Actualización inválida de conductor**

```gherkin
Dado que existe un conductor registrado
Cuando el operador intenta guardar información incompatible o incompleta
Entonces el sistema rechaza la actualización y conserva el estado anterior
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-012 — Desactivar conductor

**US-012-E1: Desactivación de conductor**

```gherkin
Dado que existe un conductor activo
Cuando el operador confirma su desactivación
Entonces el sistema cambia su estado a inactivo y evita nuevas asignaciones
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-012-E2: Desactivación de conductor inexistente**

```gherkin
Dado que el conductor solicitado no existe
Cuando el operador intenta desactivarlo
Entonces el sistema rechaza la operación e informa que el registro no fue encontrado
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-013 — Registrar cliente y condiciones de entrega

**US-013-E1: Registro válido de cliente**

```gherkin
Dado que el operador dispone de los datos requeridos del cliente
Cuando registra al cliente con preferencias y restricciones válidas
Entonces el sistema almacena la información y la deja disponible para pedidos asociados
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-013-E2: Registro con datos incompatibles**

```gherkin
Dado que el operador está registrando condiciones de entrega
Cuando ingresa datos incompatibles con las reglas definidas
Entonces el sistema rechaza la información inconsistente y explica la causa
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-014 — Consultar información de cliente

**US-014-E1: Consulta de cliente registrado**

```gherkin
Dado que existe un cliente registrado
Cuando el operador consulta su ficha
Entonces el sistema muestra sus datos y condiciones de entrega vigentes
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-014-E2: Consulta de cliente inexistente**

```gherkin
Dado que no existe un cliente con el identificador solicitado
Cuando el operador intenta consultarlo
Entonces el sistema informa que el cliente no fue encontrado
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

### US-015 — Actualizar condiciones de entrega del cliente

**US-015-E1: Actualización válida de preferencias**

```gherkin
Dado que existe un cliente registrado
Cuando el operador actualiza una preferencia o restricción con un valor válido
Entonces el sistema guarda el cambio y lo utiliza en planificaciones futuras
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

**US-015-E2: Actualización incompatible**

```gherkin
Dado que existe un cliente registrado
Cuando el operador introduce una condición incompatible con las reglas de entrega
Entonces el sistema rechaza el cambio e informa la causa
```

| Campo | Registro |
|---|---|
| Resultado observado | Pendiente |
| Evidencia o incidencia | Por registrar |
| Decisión del cliente o del usuario | Pendiente |
| Observaciones | Por registrar |

## Accesibilidad y comprensión

- [ ] El cliente o usuario puede recorrer y comprender los formularios utilizando teclado.
- [ ] El cliente o usuario comprueba los anuncios del lector de pantalla, los nombres de campos, errores y mensajes de resultado.
- [ ] Registrar lector, navegador, versión, pasos y dificultades encontradas.
- [ ] Revisar la comprensión de los mensajes y las vistas de 360 px.

La matriz de navegadores y las comprobaciones técnicas están disponibles. La comprobación de lector de pantalla anterior se interrumpió; no se da por aprobada en este registro.

## Resultado de historias y Done

| Control | Estado al preparar el registro |
|---|---|
| Pruebas, análisis estático y seguridad | Evidencia técnica disponible; consultar sus cortes |
| Compatibilidad y navegación comprobadas técnicamente | Seis versiones; resultados conservados |
| Treinta escenarios oficiales revisados por el cliente o usuario | Pendiente |
| Observaciones y defectos registrados | Pendiente |
| Decisiones de aceptación por historia | Pendiente |
| Comprensión con tecnología de asistencia | Pendiente |
| Aceptación global y criterios aplicables del Done | Pendiente |

## Acuerdos y resultado final

| Observación o cambio solicitado | Historia afectada | Responsable | Plazo acordado | Resultado |
|---|---|---|---|---|
| Por registrar | Por registrar | Por registrar | Por registrar | Pendiente |

**Decisión final del cliente o del usuario:** pendiente.

## Control documental

| Versión | Fecha | Cambio |
|---|---|---|
| V_1_0_0 | 25/10/2026 | Preparación de los 30 escenarios y campos de revisión, observaciones y Done. |

[← Volver al README](../../../README.md)
