from backend.app.repositories.user_repository import get_user_by_email


def login_user(data):
    user = get_user_by_email(data.email)

    return {
        "message": "Login simulado correcto",
        "user": user
    }


def register_user(data):
    return {
        "message": "Registro simulado correcto",
        "email": data.email
    }