from rest_framework import serializers
from .models import Course
from .models import Enrollment

class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.ReadOnlyField(source = "instructor.username")
    class Meta:
        model = Course
        fields = ["id","title","description","instructor","created_at"]

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ["id","course","created_at"]
        read_only_fields = ["id", "created_at"]

        