from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.repositories.user_repository import create_user, get_user_by_email
from app.schemas.auth import RegisterRequest


def register_user(
    db: Session,
    data: RegisterRequest,
):
    existing_user = get_user_by_email(
        db=db,
        email=str(data.email),
    )

    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe una cuenta registrada con este correo electrónico.",
        )

    hashed_password = hash_password(data.password)

    new_user = create_user(
        db=db,
        name=data.name,
        email=str(data.email),
        password_hash=hashed_password,
    )

    return new_user