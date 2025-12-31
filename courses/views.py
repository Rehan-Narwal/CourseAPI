from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from .models import Course
from .serializers import CourseSerializer
from .models import Enrollment
from .serializers import EnrollmentSerializer
from .permissions import IsInstructor

class CourseListView(APIView):
    def get_permissions(self):
        if self.request.method == "POST":
            return(IsAuthenticated(), IsInstructor())
        return[IsInstructor()]
    
    def get(self,request):
        courses = Course.objects.all()
        serializer = CourseSerializer (courses,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(instructor=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EnrollmentListView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,course_id):
        if request.user.role != "student":
            return Response(
                {"detail:Only student are allowed to enroll in courses"},
                status=status.HTTP_403_FORBIDDEN
            )
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response(
                {"detail":"Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if Enrollment.objects.filter(user=request.user,course=course,).exists():
            raise ValidationError("You are already enrolled in this course")
        
        enrollment = Enrollment.objects.create(
            user = request.user,
            course = course
        )

        serializer = EnrollmentSerializer(enrollment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
