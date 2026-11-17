def _user_payload(email="test@example.com", password="Password123", name="Test User"):
    return {"name": name, "email": email, "password": password}


def test_register_success(client):
    response = client.post("/auth/register", json=_user_payload())

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["name"] == "Test User"
    assert data["is_active"] is True
    assert "id" in data
    assert "password" not in data
    assert "password_hash" not in data


def test_register_duplicate_email_returns_409(client):
    payload = _user_payload(email="dup@example.com")
    first = client.post("/auth/register", json=payload)
    assert first.status_code == 201

    second = client.post("/auth/register", json=payload)
    assert second.status_code == 409


def test_register_weak_password_returns_422(client):
    response = client.post(
        "/auth/register",
        json=_user_payload(email="weak@example.com", password="weakpass"),
    )

    assert response.status_code == 422


def test_login_success_returns_token(client):
    client.post("/auth/register", json=_user_payload(email="login@example.com"))
    response = client.post(
        "/auth/login",
        json={"email": "login@example.com", "password": "Password123"},
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_credentials_returns_401(client):
    client.post("/auth/register", json=_user_payload(email="badlogin@example.com"))
    response = client.post(
        "/auth/login",
        json={"email": "badlogin@example.com", "password": "WrongPassword1"},
    )

    assert response.status_code == 401
