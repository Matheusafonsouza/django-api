from rest_framework.viewsets import ModelViewSet

from school.models import Enrolment, Student, Course
from school.serializers import EnrolmentSerializer, StudentSerializer, CourseSerializer


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


class EnrolmentsViewSet(ModelViewSet):
    """"
    View set for HTTP requests over Enrolment model
    """
    queryset = Enrolment.objects.all()
    serializer_class = EnrolmentSerializer
