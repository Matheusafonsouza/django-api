from rest_framework import serializers
from school.models import Enrolment, Student, Course


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer class for do and undo serialization over the student model.
    """
    class Meta:
        model = Student
        fields = '__all__'


class StudentCoursesSerializer(serializers.ModelSerializer):
    """
    Serializer class for list all courses for a student instance.
    """
    course = serializers.ReadOnlyField(source='course.description')

    class Meta:
        model = Enrolment
        fields = ('course', 'period')


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer class for do and undo serialization over the course model.
    """
    class Meta:
        model = Course
        fields = '__all__'


class CourseStudentsSerializer(serializers.ModelSerializer):
    """
    Serializer class for list all students for a course instance.
    """
    student = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Enrolment
        fields = ('student', 'period')


class EnrolmentSerializer(serializers.ModelSerializer):
    """
    Serializer class for do and undo serialization over the enrolment model.
    """
    course = serializers.ReadOnlyField(source='course.description')
    student = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Enrolment
        fields = '__all__'
