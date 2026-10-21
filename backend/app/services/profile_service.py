from sqlalchemy.orm import Session

from app.models import Profile


def get_profile_by_user_id(
    db: Session,
    user_id: int,
) -> Profile | None:
    # Devuelve el perfil asociado al usuario
    return (
        db.query(Profile)
        .filter(Profile.user_id == user_id)
        .first()
    )


def update_profile(
    db: Session,
    profile: Profile,
    data: dict,
) -> Profile:
    # Actualiza solo los campos que el usuario envió
    for field, value in data.items():
        if value is not None:
            setattr(profile, field, value)
    db.commit()
    db.refresh(profile)
    return profile


def create_profile(
    db: Session,
    user_id: int,
    data: dict,
) -> Profile:
    # Crea un perfil nuevo para el usuario
    profile = Profile(user_id=user_id, **data)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile
