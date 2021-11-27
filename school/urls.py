from django.db.models import base
from rest_framework.routers import SimpleRouter
from school.views import CoursesViewSet, StudentsViewSet

router = SimpleRouter()
router.register('courses', CoursesViewSet)
router.register('students', StudentsViewSet)

urlpatterns = [] + router.urls
