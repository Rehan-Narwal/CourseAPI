import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_instructor_can_create_course():
    client = APIClient()

    instructor = User.objects.create_user(
        username="Instructor1",
        password="Ins001",
        role="instructor",
        is_active = True
    )

    refresh = RefreshToken.for_user(instructor)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    response = client.post(
        "/api/courses/",
        {
            "title":"Python",
            "description":"Learn Python"
        },
        format="json"
    )

    assert response.status_code == 201

@pytest.mark.django_db
def test_student_cannot_create_course():
    client = APIClient()

    student = User.objects.create_user(
        username="Student1",
        password="Stu001",
        role="student",
        is_active=True
    )

    refresh = RefreshToken.for_user(student)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    response = client.post(
        "/api/courses/",
        {
            "title":"Python",
            "description":"Learn Pyhton"
        },
        format="json"
    )
    assert response.status_code == 403

