from django.db import models
from school.enums import CourseLevelEnum, EnrolmentPeriodEnum


class Student(models.Model):
    name = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    phone = models.CharField(max_length=11, default='')
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


class Enrolment(models.Model):
    period = models.CharField(
        max_length=10,
        choices=EnrolmentPeriodEnum.choices(),
        blank=False,
        null=False,
        default=EnrolmentPeriodEnum.MORNING
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
