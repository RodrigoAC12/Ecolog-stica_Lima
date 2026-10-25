[← Volver al README](../../README.md)

# Guía de staging — EcoLogística Lima

**Versión del proyecto:** 1.2.4 · **Etapa:** Pre-Sprint 3.

La configuración de staging se define en `docker-compose.staging.yml`, `src/frontend/Dockerfile.staging` y `src/frontend/Caddyfile.staging`. Se mantiene separada del Compose local: PostgreSQL y el backend no publican puertos del anfitrión. Caddy sirve React compilado y actúa como proxy HTTPS para la API.

## Prerrequisitos de despliegue real

1. Servidor **no productivo** autorizado, DNS propio para staging y puertos 80/443 disponibles.
2. Archivo `.env.staging` fuera del control de Git con secretos distintos a producción, basándose en `.env.staging.example` y reemplazando todos los valores ficticios.
3. Volumen de base de datos aislado, firewall y control de acceso; no importar datos personales reales sin autorización.
4. Prueba de resolución DNS, renovación automática de certificados TLS y respuesta de `https://<dominio>/health`.

## Comprobación y ejecución

Desde la raíz del repositorio:

```bash
docker compose --env-file .env.staging.example -f docker-compose.staging.yml config --quiet
# Únicamente con secretos y servidor de staging autorizados:
docker compose --env-file .env.staging -f docker-compose.staging.yml up -d --build
```

La ejecución de `docker compose config` y la compilación de la imagen en CI solo validan **configuración y construcción**. No demuestran que un certificado real haya sido emitido ni que el servicio esté accesible externamente.

**Antes de migrar** una base ya usada, realizar respaldo y revisar correos de cliente duplicados, porque la migración `0002_clients_email_unique` se detendrá al detectarlos. Evitar `docker compose down -v` porque elimina volúmenes persistentes. Registrar responsable, fecha, SHA desplegado, certificado, controles de roles, formularios y pruebas BDD.

**Evidencia de despliegue real:** pendiente de infraestructura y de aprobación del equipo.
