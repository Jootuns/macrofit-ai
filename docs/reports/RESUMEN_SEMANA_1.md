# Resumen Semana 1 — MacroFit AI

**Fecha:** 29 Sep — 5 Oct 2026

## Lo que se hizo

### 1. Limpieza de imports en models (`user.py`, `profile.py`)
- Se reorganizaron los imports siguiendo PEP 8: estándar → terceros → tuyo → circular
- Se eliminaron imports duplicados (`Mapped`, `mapped_column`, `relationship`)
- Se corrigió el orden del bloque `TYPE_CHECKING` para evitar imports circulares

### 2. Corrección de `datetime.utcnow` → `datetime.now(timezone.utc)`
- `datetime.utcnow()` está deprecado en Python 3.12+
- Se cambió a `lambda: datetime.now(timezone.utc)` para que SQLAlchemy genere la fecha en cada insert

### 3. Check de `is_active` en autenticación (`dependencies.py`)
- Se añadió verificación de `user.is_active` en `get_current_user`
- Ahora un usuario desactivado no puede seguir usando la app aunque su JWT no haya expirado
- Se corrigió el orden: primero buscar al usuario, luego verificar si está activo

### 4. Documentación del proyecto
- Se creó `AGENTS.md` con instrucciones para futuras sesiones
- Se creó `MEMORY.md` como diario de estudio entre sesiones
- Se estableció la regla de actualizar `MEMORY.md` al terminar cada tarea

## Lo que se aprendió

- **Imports en Python:** orden estándar → terceros → tuyo → circular (TYPE_CHECKING)
- **Imports circulares:** se resuelven con `if TYPE_CHECKING:` para que solo se importen en type checking, no en runtime
- **datetime deprecado:** `datetime.utcnow()` → `datetime.now(timezone.utc)`
- **SQLAlchemy callables:** `default=lambda: ...` en vez de `default=funcion`
- **Borrado lógico:** `is_active` permite desactivar usuarios sin borrarlos de la DB
- **Orden de validaciones:** cada paso depende del anterior (token → user_id → buscar → existe → activo)

## Pendiente para la próxima semana

1. CORS en `main.py`
2. Logging básico
3. Manejo de errores global
4. Mejorar validación de contraseñas
5. Completar Fase 3: endpoint de perfil (GET/PATCH), logout
6. Configurar Alembic
7. Tests básicos de auth
8. Docker: docker-compose.yml + Dockerfile
