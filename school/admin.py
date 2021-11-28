from django.contrib import admin
from school.models import Enrolment, Student, Course


class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


class Courses(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'level')
    list_display_links = ('id', 'code')
    search_fields = ('code',)
    list_per_page = 20


class Enrolments(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id',)
    search_fields = ('period',)
    list_per_page = 20


admin.site.register(Enrolment, Enrolments)
admin.site.register(Student, Students)
admin.site.register(Course, Courses)
