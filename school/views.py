from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from school.models import Enrolment, Student, Course
from school.serializers import (
    CourseStudentsSerializer, EnrolmentSerializer,
    StudentCoursesSerializer, StudentSerializer, CourseSerializer, StudentSerializerV2
)


class StudentsViewSet(ModelViewSet):
    """"
    View set for HTTP requests over Student model
    """
    queryset = Student.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        Defines the serializer class from the api version.
        :returns: Serializer class
        """
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer


class StudentCoursesListView(ListAPIView):
    """"
    View set for list student enrolments.
    """
    serializer_class = StudentCoursesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Enrolment.objects.filter(student__pk=self.kwargs['pk'])


class CoursesViewSet(ModelViewSet):
    """"
    View set for HTTP requests over Course model
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CourseStudentsListView(ListAPIView):
    """"
    View set for list course students.
    """
    serializer_class = CourseStudentsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Enrolment.objects.filter(course__pk=self.kwargs['pk'])


class EnrolmentsViewSet(ModelViewSet):
    """"
    View set for HTTP requests over Enrolment model
    """
    queryset = Enrolment.objects.all()
    serializer_class = EnrolmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
