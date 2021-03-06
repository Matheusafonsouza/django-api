from rest_framework.routers import SimpleRouter
from school.views import CourseStudentsListView, CoursesViewSet, EnrolmentsViewSet, StudentCoursesListView, StudentsViewSet
from django.urls import path

router = SimpleRouter()

router.register('courses', CoursesViewSet)
router.register('students', StudentsViewSet)
router.register('enrolments', EnrolmentsViewSet)

urlpatterns = [
    path('students/<int:pk>/enrolments', StudentCoursesListView.as_view()),
    path('courses/<int:pk>/students', CourseStudentsListView.as_view())
] + router.urls
