from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from school.models import Enrolment, Student, Course
from school.serializers import (
    CourseStudentsSerializer, EnrolmentSerializer,
    StudentCoursesSerializer, StudentSerializer, CourseSerializer,
    StudentSerializerV2
)


class StudentsViewSet(ModelViewSet):
    """"
    View set for HTTP requests over Student model
    """
    queryset = Student.objects.all()

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

    def get_queryset(self):
        return Enrolment.objects.filter(student__pk=self.kwargs['pk'])


class CoursesViewSet(ModelViewSet):
    """"
    View set for HTTP requests over Course model
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(
                serializer.data, status=status.HTTP_201_CREATED)
            pk = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + pk
            return response


class CourseStudentsListView(ListAPIView):
    """"
    View set for list course students.
    """
    serializer_class = CourseStudentsSerializer

    def get_queryset(self):
        return Enrolment.objects.filter(course__pk=self.kwargs['pk'])


class EnrolmentsViewSet(ModelViewSet):
    """"
    View set for HTTP requests over Enrolment model
    """
    queryset = Enrolment.objects.all()
    serializer_class = EnrolmentSerializer
    http_method_names = ['get', 'post', 'put', 'path']

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        print(args, kwargs)
        return super(EnrolmentsViewSet, self).dispatch(*args, **kwargs)
