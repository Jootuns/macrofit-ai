# MEMORY.md — MacroFit AI

Memoria del proyecto entre sesiones. Máximo ~50 líneas: resume o elimina lo que ya no aporte.

## Estado actual

- Backend en Fase 3 de 14: auth (registro, login, JWT) funcionando.
- Perfil completo: GET, POST (crear) y PATCH /users/me/profile.
- Arquitectura en capas: api → services → repositories → models.
- CORS, health check real, logging y error handling global implementados.
- Validación de contraseñas con @field_validator.
- Sin tests, Docker, Alembic ni CI/CD todavía (siguiente: tests).

## Decisiones (y por qué)

- Arquitectura en capas: separa HTTP de lógica de negocio, facilita testear.
- JWT sin refresh token: el MVP no lo necesita; limitación documentada.
- Argon2id para contraseñas: estándar actual, más seguro que bcrypt.
- CORS abierto en desarrollo; restringir en producción.

## Aprendizajes y errores a evitar

- Imports Python: estándar → terceros → propios → circular (TYPE_CHECKING).
- `datetime.utcnow()` deprecado: usar `datetime.now(timezone.utc)`.
- `Session` va en `sqlalchemy.orm`, no en `sqlalchemy`.
- `relationship(back_populates=...)` apunta al nombre del OTRO lado (User.profile ↔ Profile.user).
- Verificar `user.is_active` en cada request, no solo al registrar.
- SQLAlchemy: `default=lambda: ...` para callables.
- Orden en auth: token → user_id → buscar → existe → activo.
- PEP 8: 2 líneas entre funciones, espacio tras `#`, sin trailing whitespace.
- Probar endpoints con uvicorn real, no solo con import checks.
- Nunca loguear datos sensibles.

## Próximos pasos

1. Tests con pytest + httpx (fixtures con rollback, DB de test separada).
2. Alembic (migraciones) antes de añadir más modelos.
3. Endpoint de logout.
4. Docker: docker-compose.yml + Dockerfile.
5. Fase 4: cálculo de calorías/macros (Mifflin-St Jeor) con SDD.

## Herramientas configuradas

- Custom Commands: `/feature`, `/review`, `/refactor`.
- Informes semanales en Markdown en `docs/reports/`.
