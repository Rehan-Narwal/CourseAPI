# CourseAPI

CourseAPI is a backend-only REST API built with Django and Django REST Framework.
It provides user authentication, role-based permissions, course management,
and enrollment functionality using JWT-based authentication.

This project is designed as a clean, production-style backend suitable for
a fresher-level backend developer portfolio.

## Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- PostgreSQL (Production)
- SQLite (Development)
- pytest
- Render (Deployment)

## Features

### Authentication
- User registration
- User login using JWT access tokens
- JWT-protected endpoints
- User profile endpoint (`/users/me/`)

### Roles & Permissions
- Two user roles: **student** and **instructor**
- Instructor-only course creation
- Student-only course enrollment
- Permission checks enforced at API level

### Courses
- Create courses (instructor only)
- List available courses
- Retrieve course details

### Enrollment
- Enroll in courses
- Prevent duplicate enrollments
- Enrollment linked to authenticated user

### Admin Panel
- Manage users
- Manage courses
- Manage lessons

## API Endpoints

### Authentication
- `POST /api/auth/register/` — Register a new user
- `POST /api/auth/login/` — Login and receive JWT access token

### Users
- `GET /api/users/me/` — Get authenticated user profile

### Courses
- `GET /api/courses/` — List all courses (JWT required)
- `POST /api/courses/` — Create a course (Instructor only)
- `GET /api/courses/{id}/` — Retrieve course details

### Enrollment
- `POST /api/courses/{id}/enroll/` — Enroll in a course (Student only)

## Running Locally

### Prerequisites
- Python 3.10+
- PostgreSQL (optional for local use)

### Setup

Clone the repository:

```bash
git clone https://github.com/Rehan-Narwal/CourseAPI.git
cd CourseAPI
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
open in browser with the localhost link
