from rest_framework import serializers
from client.models import Client
from client.validators import (
    validate_cpf, validate_name, validate_phone, validate_rg
)


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

    def validate_rg(self, rg):
        """
        Method for validate rg conditions.
        :param rg: Client instance rg
        :returnts: The rg if validation is ok or raises a validation error
        """
        if len(rg) != 9:
            raise serializers.ValidationError('RG field must have 9 digits.')
        return rg

    def validate_phone(self, phone):
        """
        Method for validate phone conditions.
        :param phone: Client instance phone
        :returnts: The phone if validation is ok or raises a validation error
        """
        if len(phone) != 11:
            raise serializers.ValidationError(
                'Phone field must have 11 digits.')
        return phone

    def validate_name(self, name):
        """
        Method for validate name conditions.
        :param name: Client instance name
        :returnts: The name if validation is ok or raises a validation error
        """
        if not name.isalpha():
            raise serializers.ValidationError(
                'Name field must have only alpha characters.')
        return name

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
                dict(phone='Phone number must have 11 digits.'))
        if not validate_name(data['name']):
            raise serializers.ValidationError(
                dict(name='Name must have only apha characters.'))
        return data

    class Meta:
        model = Client
        fields = '__all__'
