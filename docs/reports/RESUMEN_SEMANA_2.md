# Resumen Semana 2 — MacroFit AI

**Fecha:** 6 Oct — 10 Nov 2026

## Lo que se hizo

### 1. Refactor de la API (`main.py`, `dependencies.py`)
- Se añadió **CORS** con `CORSMiddleware` (abierto en desarrollo).
- Se añadió un **manejador global de errores** (`@app.exception_handler`) que loguea y devuelve un 500 limpio sin filtrar detalles internos.
- El **health check** ahora comprueba de verdad la conexión a PostgreSQL (`SELECT 1`), no solo responde `ok`.
- `get_current_user` verifica `user.is_active` en cada request.

### 2. Logging y validación de contraseñas
- Logging básico con `logging.getLogger(__name__)` en `auth_service.py`.
- Validación de contraseñas con `@field_validator`: mínimo 8 caracteres, una mayúscula y un número.

### 3. Endpoint de perfil completo (`/users/me/profile`)
- `GET` → devuelve el perfil o **404** si aún no existe.
- `POST` → crea el perfil (**409** si ya existe), completa el flujo tras el registro.
- `PATCH` → actualización parcial (solo los campos enviados).
- Schema `ProfileCreate` (campos obligatorios) y `ProfileUpdate` (todos opcionales).
- Lógica en `profile_service.py`, rutas en `api/users.py` respetando la arquitectura en capas.

### 4. Bug crítico corregido
- `Profile.user` tenía `back_populates="user"` (incorrecto) y rompía **todas** las operaciones de DB con un 500, incluido el registro.
- Correcto: `back_populates="profile"` (apunta al nombre de la relación en el otro lado).

### 5. Verificación real de la API
- Se probó con uvicorn + requests reales, no solo con imports:

| Endpoint | Resultado |
|----------|-----------|
| `POST /auth/register` | 201 |
| `POST /auth/login` | 200 |
| `POST /users/me/profile` | 201 / 409 si ya existe |
| `GET /users/me/profile` | 200 / 404 si no existe |
| `PATCH /users/me/profile` | 200 (parcial) |

### 6. Herramientas y documentación
- `AGENTS.md` completo con todas las secciones del template.
- Custom Commands: `/feature`, `/review`, `/refactor`.
- `MEMORY.md` mantenido como diario entre sesiones (≤ 50 líneas).
- Datos de prueba borrados de la DB de desarrollo.

## Lo que se aprendió

- **Probar de verdad:** un import correcto no garantiza que el endpoint funcione; hay que levantar el servidor y hacer requests.
- **`back_populates`:** apunta al nombre del atributo del **otro** lado de la relación.
- **Upsert vs create:** `PATCH` no debe crear; el flujo de "completar perfil" necesita un `POST` explícito.
- **Errores en capas:** un fallo en el mapper de SQLAlchemy aparece como 500 genérico; hay que leer el log del servidor.
- **Limpieza de datos de test:** los tests deben aislar y borrar sus datos (fixtures con rollback + DB de test separada).
- **PEP 8:** 2 líneas entre funciones, espacio tras `#`, sin trailing whitespace.

## Pendiente para la próxima semana

1. **Tests con pytest + httpx** (fixtures con rollback, DB de test separada). ← siguiente
2. Alembic (migraciones) antes de añadir más modelos.
3. Endpoint de logout.
4. Docker: `docker-compose.yml` + `Dockerfile`.
5. Fase 4: cálculo de calorías/macros (Mifflin-St Jeor).
