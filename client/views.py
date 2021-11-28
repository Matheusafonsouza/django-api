from rest_framework.viewsets import ModelViewSet

from client.models import Client
from client.serializers import ClientSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ClientsViewSet(ModelViewSet):
    """"
    View set for HTTP requests over client model.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name']
