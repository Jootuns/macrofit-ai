from datetime import date

from sqlalchemy import Date, Float, ForeignKey, Integer, String
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


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(
    Integer,
    primary_key=True,
)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
    )

    birth_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    biological_sex: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    height_cm: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    current_weight_kg: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    goal: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    activity_level: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
    back_populates="profile"
    )