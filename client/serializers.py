from rest_framework import serializers
from client.models import Client
from client.validators import (
    validate_cpf, validate_name, validate_phone, validate_rg
)


class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer class for do and undo serialization over the client model.
    """

    def validate(self, data):
        """
        Validate the client instance.
        :param data: Client instance data fields
        :retunrs: Data if validation is ok or raises a validation exception
        """
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError(
                dict(cpf='CPF must have 11 digits.'))
        if not validate_rg(data['rg']):
            raise serializers.ValidationError(
                dict(rg='RG must have 9 digits.'))
        if not validate_phone(data['phone']):
            raise serializers.ValidationError(
                dict(phone='Phone number must obey this pattern: 61 99999-9999.'))
        if not validate_name(data['name']):
            raise serializers.ValidationError(
                dict(name='Name must have only apha characters.'))
        return data

    class Meta:
        model = Client
        fields = '__all__'
