import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importar Base y modelos para que las tablas se registren en metadata
from app.db.base import Base
from app.db.database import get_db, settings
from app.main import app
from app.models import Profile, User  # noqa: F401

# Misma conexión que .env pero apuntando a la DB de test
TEST_DATABASE_URL = settings.database_url.set(database="macrofit_ai_test")

engine_test = create_engine(TEST_DATABASE_URL, pool_pre_ping=True)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine_test,
)


@pytest.fixture(scope="function")
def db_session():
    # Crea y destruye el esquema en cada test: aislamiento total aunque falle.
    # No usamos rollback simple porque los servicios hacen commit().
    Base.metadata.create_all(bind=engine_test)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine_test)


@pytest.fixture(scope="function")
def client(db_session):
    # Sobrescribe get_db para que la API use la sesión/DB de test
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
