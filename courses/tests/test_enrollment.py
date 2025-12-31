import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from courses.models import Course

User = get_user_model()

@pytest.mark.django_db
def test_student_can_enroll():
    client = APIClient()

    instructor = User.objects.create_user(
        username="Inst1",
        password="Inst001",
        role="Instructor",
        is_active=True
    )

    student = User.objects.create_user(
        username="Stud1",
        password="Std001",
        role="student",
        is_active=True
    )

    course = Course.objects.create(
        title="Python",
        description="Learn Python",
        instructor=instructor
    )

    refresh = RefreshToken.for_user(student)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    response = client.post(f"/api/courses/{course.id}/enroll/")

    assert response.status_code == 201

@pytest.mark.django_db
def test_student_cannot_enroll_twice():

    client = APIClient()

    instructor = User.objects.create_user(
        username="Inst1",
        password="Inst001",
        role="Instructor",
        is_active=True
    )

    student = User.objects.create_user(
        username="Stud1",
        password="Stud001",
        role="student",
        is_active=True
    )

    course = Course.objects.create(
        title="Python",
        description="Learn Pyhton",
        instructor=instructor
    )

    refresh = RefreshToken.for_user(student)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    client.post(f"/api/courses/{course.id}/enroll/")
    response = client.post(f"/api/courses/{course.id}/enroll/")

    assert response.status_code == 400