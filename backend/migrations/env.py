from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from app.db.base import Base
from app.db.database import settings
# Importar modelos para que Base.metadata tenga todas las tablas
from app.models import Profile, User  # noqa: F401

# Objeto de configuración de Alembic (lee alembic.ini)
config = context.config

# Usa la URL desde la configuración de la app (.env), no la de alembic.ini
# configparser interpreta "%" como interpolación; hay que escaparlo como "%%"
db_url = settings.database_url.render_as_string(hide_password=False)
config.set_main_option("sqlalchemy.url", db_url.replace("%", "%%"))

# Configura el logging de Alembic según alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata de los modelos para soportar autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Ejecuta migraciones en modo offline (genera SQL sin conectar)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecuta migraciones en modo online (conectado a la DB)."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
