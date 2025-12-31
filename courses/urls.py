from django.urls import path
from .views import CourseListView
from .views import EnrollmentListView

urlpatterns = [
    path("courses/",CourseListView.as_view(), name="course-list"),
    path("courses/<int:course_id>/enroll/", EnrollmentListView.as_view(),name="course-enroll"),
]