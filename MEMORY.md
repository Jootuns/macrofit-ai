# MEMORY.md — Diario de Estudio

Memoria del proyecto entre sesiones. Máximo ~50 líneas: resume o elimina lo que ya no
aporte.

## Estado actual

- Backend en Fase 3 de 14: auth (registro, login, JWT) funcionando.
- Modelos User + Profile creados y sincronizados con PostgreSQL.
- Arquitectura en capas: api → services → repositories → models.
- Check de `is_active` añadido en `get_current_user` (dependencies.py).
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

## Próximos pasos

1. Arreglos técnicos pendientes: CORS, logging, error handling, health check real.
2. Completar Fase 3: endpoint de perfil (GET/PATCH), logout.
3. Configurar Alembic antes de añadir más modelos.
4. Tests básicos de auth con pytest.
5. Docker: docker-compose.yml con PostgreSQL + backend.
6. Empezar Fase 4: cálculo de calorías y macros (Mifflin-St Jeor).
