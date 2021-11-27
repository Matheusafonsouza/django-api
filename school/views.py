from rest_framework.viewsets import ModelViewSet

from school.models import Student, Course
from school.serializers import StudentSerializer, CourseSerializer


class StudentsViewSet(ModelViewSet):
    """"
    View set for HTTP requests over Student model
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoursesViewSet(ModelViewSet):
    """"
    View set for HTTP requests over Course model
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
