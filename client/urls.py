from rest_framework.routers import SimpleRouter
from client.views import ClientsViewSet

router = SimpleRouter()

router.register('clients', ClientsViewSet)

urlpatterns = [] + router.urls
