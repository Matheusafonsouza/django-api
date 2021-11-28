from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from school.models import Enrolment, Student, Course
from school.serializers import EnrolmentSerializer, StudentCoursesSerializer, StudentSerializer, CourseSerializer


class StudentsViewSet(ModelViewSet):
    """"
    View set for HTTP requests over Student model
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCoursesListView(ListAPIView):
    """"
    View set for list student enrolments.
    """
    serializer_class = StudentCoursesSerializer

    def get_queryset(self):
        return Enrolment.objects.filter(student__pk=self.kwargs['pk'])


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
