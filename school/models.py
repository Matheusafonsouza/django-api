from django.db import models
from school.enums import CourseLevelEnum


class Student(models.Model):
    name = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Course(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(
        max_length=10,
        choices=CourseLevelEnum.choices(),
        blank=False,
        null=False,
        default=CourseLevelEnum.EASY
    )

    def __str__(self):
        return self.description
