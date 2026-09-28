from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash

from app.db.database import settings


password_hasher = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hasher.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    return password_hasher.verify(
        plain_password,
        hashed_password,
    )


def create_access_token(user_id: int) -> str:
    # Calcula la fecha de expiración del token en UTC.
    expires_at = datetime.now(timezone.utc) + timedelta(
        minutes=settings.jwt_expire_minutes
    )

    # Información que se incluirá dentro del token.
    payload = {
        "sub": str(user_id),
        "exp": expires_at,
    }

    # Firma y devuelve el token JWT.
    return jwt.encode(
        payload,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    )