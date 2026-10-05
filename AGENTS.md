# AGENTS.md

## Descripción del proyecto

MacroFit AI — app móvil de nutrición y entrenamiento. Backend en Python/FastAPI, frontend (React Native/Expo) aún no iniciado. El proyecto está en desarrollo temprano (Fase 3 de 14).

## Cómo arrancar el backend

```bash
cd backend
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # luego editar con credenciales reales
python -m app.db.init_db  # crear tablas
uvicorn app.main:app --reload --port 8000
```

Documentación de la API en `http://localhost:8000/docs` (Swagger UI).

## Arquitectura

Arquitectura en capas — cada capa tiene una única responsabilidad:

```
api/           → solo rutas HTTP, sin lógica de negocio
services/      → lógica de negocio, orquestación
repositories/  → solo consultas a la base de datos
models/        → modelos ORM de SQLAlchemy
schemas/       → esquemas de validación con Pydantic
core/          → seguridad (JWT, hash de contraseñas), dependencias
db/            → engine, sesión, configuración
```

**Regla:** Nunca llamar repositories directamente desde `api/`. Siempre pasar por `services/`.

## Stack y convenciones

- Python 3.12+, FastAPI, SQLAlchemy 2.0 (estilo tipado `Mapped[]`), Pydantic v2
- PostgreSQL vía psycopg2
- Autenticación: JWT (HS256) + hash de contraseñas Argon2id
- Comentarios y mensajes de commit en español
- Sin tests, sin Docker, sin CI/CD, sin Alembic todavía — todo está en el backlog

## Variables de entorno

Necesarias en `backend/.env`:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=macrofit_ai
DB_USER=macrofit_app
DB_PASSWORD=change_me
JWT_SECRET_KEY=change_me
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30
```

## Qué está implementado

- Registro e inicio de sesión de usuarios (JWT)
- `GET /users/me` (endpoint protegido)
- Modelos User + Profile con relación
- Endpoint de health check

## Qué viene después (según BACKLOG.md)

1. Migraciones con Alembic
2. Endpoint para completar perfil
3. Cálculo de calorías y macros (Fase 4)
4. App móvil (Fase 5)
5. Planificación de comidas (Fase 6)

## Archivos clave

- `backend/app/main.py` — punto de entrada de la app FastAPI
- `backend/app/db/database.py` — Settings, engine, factory de sesiones
- `backend/app/core/security.py` — crear/decodificar JWT, hash/verify de contraseñas
- `backend/app/core/dependencies.py` — dependencia `get_current_user`
- `docs/BACKLOG.md` — lista completa de tareas por fases
- `docs/MVP.md` — alcance del MVP y criterios de éxito

## Memoria

- Al empezar, lee `MEMORY.md` para conocer el estado del proyecto y las decisiones tomadas.
- Al terminar una tarea, actualízalo: estado actual, decisiones importantes (con su porqué) y errores a evitar.
- Mantenlo breve (máximo ~50 líneas): resume o elimina lo que ya no aporte.
- Si algo se convierte en una regla permanente, propón moverlo a `AGENTS.md` en lugar de dejarlo en la memoria.
- No guardes nunca datos sensibles (claves, tokens, datos personales).

## Límites

- **Siempre:** actualizar `MEMORY.md` al terminar cada tarea.
