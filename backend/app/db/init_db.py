from app.db.base import Base
from app.db.database import engine

import app.models.profile
import app.models.user


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Tablas creadas correctamente")