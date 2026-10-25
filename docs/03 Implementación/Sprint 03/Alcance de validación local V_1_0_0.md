[← Volver al README](../../../README.md)

# Alcance de validación local del Sprint 3

**Versión documental:** V_1_0_0 · **Fecha:** 25/10/2026 (Lima).

El alcance acordado de despliegue y comprobación es exclusivamente localhost. No se requiere contratar un servidor, publicar la aplicación en Internet, configurar DNS público ni acreditar acceso remoto. Las referencias anteriores a infraestructura externa no constituyen bloqueos de esta entrega.

## Entorno de aceptación técnica

- Frontend y gateway accesibles solo por la interfaz local.
- PostgreSQL y API en red interna sin publicar sus puertos al anfitrión.
- HTTP local en 8080 y HTTPS local en 8443.
- Certificados de una CA interna para localhost; verificación de cadena y hostname en el cliente de pruebas.
- Credenciales privadas fuera del repositorio y CA seleccionada expresamente para la comprobación.

La [guía de staging local](<../../Despliegue/Guía de staging.md>) describe cómo reproducir el entorno. La [evidencia de comprobación](evidencias/staging-local.json) identifica servicios y resultados medidos.

## Efecto sobre requisitos y DoD

DoD-07 se verifica mediante el entorno local reproducible. El cifrado se comprueba en la entrada HTTPS local; HTTP de loopback se declara expresamente y no se presenta como tráfico externo cifrado. No se amplía la evaluación a dispositivos remotos.

Las pruebas y el despliegue local no sustituyen revisión independiente, aceptación funcional, contraste, tecnologías de asistencia ni confirmación de calendario y responsables. Esos pendientes se mantienen cuando corresponden.

Los cinco informes conservan los nombres de archivo requeridos y remiten a esta adenda versionada para el alcance vigente. Las evidencias del 24/10 conservan sus fechas y resultados.

[← Volver al README](../../../README.md)
