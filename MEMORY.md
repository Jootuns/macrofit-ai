# MEMORY.md — Diario de Estudio

Memoria del proyecto entre sesiones. Máximo ~50 líneas: resume o elimina lo que ya no
aporte.

## Estado actual

- Backend en Fase 3 de 14: auth (registro, login, JWT) funcionando.
- Endpoint de perfil: GET, POST (crear) y PATCH /users/me/profile.
- Modelos User + Profile creados y sincronizados con PostgreSQL.
- Arquitectura en capas: api → services → repositories → models.
- Check de `is_active`, CORS, health check, logging y error handling global implementados.
- Validación de contraseñas con @field_validator (mínimo 8 caracteres, mayúscula y número).
- Frontend (React Native/Expo) no iniciado.
- Sin tests, sin Docker, sin Alembic, sin CI/CD todavía.

## Decisiones (y por qué)

- Arquitectura en capas: separar HTTP de lógica de negocio facilita testear y mantener.
- JWT sin refresh token (por ahora): el MVP no lo necesita; se documenta como limitación.
- Comentarios y commits en español: el equipo es hispanohablante.
- Argon2id para contraseñas: estándar actual, más seguro que bcrypt.
- Sin CORS restringido en desarrollo: permite probar la app móvil sin fricción.

## Aprendizajes y errores a evitar

- Los imports en Python van en orden: estándar → terceros → tuyo → circular (TYPE_CHECKING).
- `datetime.utcnow()` está deprecado: usar `datetime.now(timezone.utc)`.
- Verificar `user.is_active` en cada request autenticado, no solo al crear la cuenta.
- SQLAlchemy necesita `default=lambda: ...` para callables, no `default=funcion`.
- Sin Alembic, cada cambio en los modelos es manual y propenso a errores.
- El orden de validaciones importa: no puedes verificar `is_active` antes de buscar al usuario en la DB.
- La indentación inconsistente en relationships de SQLAlchemy confunde: mantener en una sola línea o con indentación correcta.
- `logger.warning()` y `raise HTTPException()` son independientes: primero se registra, luego se lanza el error.
- Nunca registrar datos sensibles en logs: contraseñas, tokens, números de tarjeta.
- En llamadas a funciones, no poner espacio alrededor del `=`: `status_code=500`.
- Estructura lógica de main.py: imports → logger → app → middleware → handlers → rutas.
- No dejar espacios al final de líneas (trailing whitespace).
- La indentación en funciones de varias líneas debe ser consistente.
- `Session` se importa de `sqlalchemy.orm`, NO de `sqlalchemy`.
- En `relationship(back_populates=...)` se apunta al nombre de la relación en el OTRO lado: User.profile ↔ Profile.user.
- Los endpoints se prueban con el servidor real (uvicorn) + requests, no solo con import checks.
- En PEP 8 van 2 líneas en blanco entre funciones a nivel de módulo.
- Los comentarios siempre llevan un espacio después del `#`.

## Próximos pasos

1. Arreglos técnicos pendientes: logging, error handling, health check real.
2. Completar Fase 3: endpoint de perfil (GET/PATCH), logout.
3. Configurar Alembic antes de añadir más modelos.
4. Tests básicos de auth con pytest.
5. Docker: docker-compose.yml + Dockerfile.
6. Empezar Fase 4: cálculo de calorías y macros (Mifflin-St Jeor) — adoptar SDD.

## Herramientas configuradas

- Custom Commands en `.opencode/commands/`: `/feature`, `/review`, `/refactor`
- AGENTS.md completo con todas las secciones del template
- Resúmenes semanales en Markdown (sustituyen a los PDFs diarios)
