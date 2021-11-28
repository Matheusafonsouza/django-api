from rest_framework import serializers
from client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer class for do and undo serialization over the client model.
    """
    class Meta:
        model = Client
        fields = '__all__'
