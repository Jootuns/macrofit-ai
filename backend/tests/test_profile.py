PROFILE_PAYLOAD = {
    "birth_date": "1995-05-15",
    "biological_sex": "male",
    "height_cm": 180.5,
    "current_weight_kg": 75.0,
    "goal": "gain_muscle",
    "activity_level": "moderate",
}


def auth_headers(client, email="profile@example.com"):
    # Registra y hace login para obtener un token válido
    client.post(
        "/auth/register",
        json={"name": "Profile User", "email": email, "password": "Password123"},
    )
    login = client.post(
        "/auth/login",
        json={"email": email, "password": "Password123"},
    )
    token = login.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_get_profile_without_profile_returns_404(client):
    headers = auth_headers(client, email="noprof@example.com")
    response = client.get("/users/me/profile", headers=headers)

    assert response.status_code == 404


def test_create_profile_returns_201(client):
    headers = auth_headers(client, email="create@example.com")
    response = client.post("/users/me/profile", json=PROFILE_PAYLOAD, headers=headers)

    assert response.status_code == 201
    data = response.json()
    assert data["height_cm"] == 180.5
    assert data["goal"] == "gain_muscle"
    assert "id" in data


def test_create_profile_twice_returns_409(client):
    headers = auth_headers(client, email="conflict@example.com")
    first = client.post("/users/me/profile", json=PROFILE_PAYLOAD, headers=headers)
    assert first.status_code == 201

    second = client.post("/users/me/profile", json=PROFILE_PAYLOAD, headers=headers)
    assert second.status_code == 409


def test_get_profile_returns_200(client):
    headers = auth_headers(client, email="get@example.com")
    client.post("/users/me/profile", json=PROFILE_PAYLOAD, headers=headers)

    response = client.get("/users/me/profile", headers=headers)

    assert response.status_code == 200
    assert response.json()["biological_sex"] == "male"


def test_patch_profile_updates_only_sent_fields(client):
    headers = auth_headers(client, email="patch@example.com")
    client.post("/users/me/profile", json=PROFILE_PAYLOAD, headers=headers)

    response = client.patch(
        "/users/me/profile",
        json={"height_cm": 182.0},
        headers=headers,
    )

    assert response.status_code == 200
    data = response.json()
    # Solo cambia height_cm; el resto se mantiene
    assert data["height_cm"] == 182.0
    assert data["goal"] == "gain_muscle"
    assert data["current_weight_kg"] == 75.0


def test_profile_endpoints_require_auth(client):
    response = client.get("/users/me/profile")
    # HTTPBearer sin credenciales devuelve 403 en FastAPI
    assert response.status_code in (401, 403)
