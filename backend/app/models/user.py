from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.profile import Profile

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
    Integer,
    primary_key=True,
)

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    preferred_language: Mapped[str] = mapped_column(
        String(10),
        default="es",
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    profile: Mapped["Profile"] = relationship(
    back_populates="user"
    )

    def __repr__(self):
        return f"User(email='{self.email}')"

    