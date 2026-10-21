from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.database import get_db
from app.models import User
from app.schemas.auth import UserResponse
from app.schemas.profile import ProfileCreate, ProfileResponse, ProfileUpdate
from app.services.profile_service import (
    create_profile,
    get_profile_by_user_id,
    update_profile,
)

router = APIRouter()


@router.get(
    "/users/me",
    response_model=UserResponse,
)
def get_my_user(
    current_user: User = Depends(get_current_user),
):
    return current_user


@router.get(
    "/users/me/profile",
    response_model=ProfileResponse,
)
def get_my_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Devuelve el perfil del usuario autenticado
    profile = get_profile_by_user_id(db=db, user_id=current_user.id)

    # Si no tiene perfil (no lo completó aún), devolvemos 404
    if profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Perfil no encontrado",
        )

    return profile


@router.patch(
    "/users/me/profile",
    response_model=ProfileResponse,
)
def update_my_profile(
    data: ProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Busca el perfil del usuario autenticado
    profile = get_profile_by_user_id(db=db, user_id=current_user.id)

    if profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Perfil no encontrado",
        )

    # Actualiza solo los campos enviados y devuelve el perfil actualizado
    return update_profile(db=db, profile=profile, data=data.model_dump(exclude_unset=True))


@router.post(
    "/users/me/profile",
    response_model=ProfileResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_my_profile(
    data: ProfileCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    # Un usuario solo puede tener un perfil
    existing = get_profile_by_user_id(db=db, user_id=current_user.id)
    if existing is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El usuario ya tiene un perfil",
        )

    return create_profile(db=db, user_id=current_user.id, data=data.model_dump())
