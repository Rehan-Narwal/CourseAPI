import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(
        username="Goku",
        password="kamehameha"
    )
    assert user.username == "Goku"

@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    
    response = client.post(
        "/api/auth/register/",
        {
            "username":"Vegeta",
            "password":"ItsOver9000"
        },
        format="json"
    )
    assert response.status_code == 201

@pytest.mark.django_db
def test_login_user():
    client = APIClient()

    user = User.objects.create_user(
        username="Jhon",
        password="Doe",
        is_active=True
    )

    response = client.post(
        "/api/auth/login/",
        {
            "username":"Jhon",
            "password":"Doe"
        },
        format="json"
    )

    assert response.status_code == 200
    assert "access" in response.data
