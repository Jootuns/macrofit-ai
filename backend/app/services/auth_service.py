from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.repositories.user_repository import create_user, get_user_by_email
from app.schemas.auth import LoginRequest, RegisterRequest


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


def login_user(
    db: Session,
    data: LoginRequest,
):
    user = get_user_by_email(
        db=db,
        email=str(data.email),
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo electrónico o contraseña incorrectos.",
        )

    #Comprobar contraseña
    password_is_valid = verify_password(
        plain_password=data.password,
        hashed_password=user.password_hash,
    )

    if not password_is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo electrónico o contraseña incorrectos.",
        )

    #Generar JWT con user.id
    access_token = create_access_token(user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }