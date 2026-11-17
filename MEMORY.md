# MEMORY.md — MacroFit AI

Memoria del proyecto entre sesiones. Máximo ~50 líneas: resume o elimina lo que ya no aporte.

## Estado actual

- Backend en Fase 3 de 14: auth (registro, login, JWT) funcionando.
- Perfil completo: GET, POST (crear) y PATCH /users/me/profile.
- Tests (pytest + TestClient): auth y perfil cubiertos; DB de test separada (`macrofit_ai_test`) con `create_all/drop_all` por test.
- Arquitectura en capas: api → services → repositories → models.
- CORS, health check real, logging y error handling global implementados.
- Validación de contraseñas con @field_validator.
- Sin Docker, Alembic ni CI/CD todavía (siguiente: Alembic o logout).

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
- Tests: DB separada + fixtures que crean/borran esquema por test; override de `get_db`; no mezclar deps de dev en `requirements.txt`.
- Nunca loguear datos sensibles.

## Próximos pasos

1. Alembic (migraciones) antes de añadir más modelos (reconstruir config, baseline).
2. Endpoint de logout.
3. Docker: docker-compose.yml + Dockerfile.
4. Fase 4: cálculo de calorías/macros (Mifflin-St Jeor) con SDD.

## Herramientas configuradas

- Custom Commands: `/feature`, `/review`, `/refactor`.
- Informes semanales en Markdown en `docs/reports/`.
