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

    class Meta:
        model = Client
        fields = '__all__'
