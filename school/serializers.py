from rest_framework import serializers
from school.models import Student, Course


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer class for do and undo serialization over the student model.
    """
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer class for do and undo serialization over the course model.
    """
    class Meta:
        model = Course
        fields = '__all__'
