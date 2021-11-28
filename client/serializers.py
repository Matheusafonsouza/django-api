from rest_framework import serializers
from client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer class for do and undo serialization over the client model.
    """

    def validate_cpf(self, cpf):
        """
        Method for validate cpf conditions.
        :param cpf: Client instance cpf
        :returnts: The cpf if validation is ok or raises a validation error
        """
        if len(cpf) != 11:
            raise serializers.ValidationError('CPF field must have 11 digits.')
        return cpf

    class Meta:
        model = Client
        fields = '__all__'
