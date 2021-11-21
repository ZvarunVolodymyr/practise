from rest_framework import serializers
from user.models import User
from helping_func.validation import validator_
from helping_func.validation_functions import validation
from django.core.exceptions import ObjectDoesNotExist
from user.models import TokenBlackList
from helping_func.security import JWT_decode


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'birth_date')
        extra_kwargs = {'password': {'write_only': True}}

    def validator(self, data, **obj):
        return_ = validator_(self, data, validation)
        try:
            obj['User'].get(email=data['email'])
            raise serializers.ValidationError({'email': 'ця пошта вже зайнята'})
        except ObjectDoesNotExist:
            pass
        try:
            obj['Certificate'].get(pk=data['id_of_certificate'])
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'id_of_certificate': 'немає сертифікати з таким ід'})

        return return_


class TokenBlackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenBlackList
        fields = ('token', 'exp')

    def validator(self, data):
        data['exp'] = int(JWT_decode(data['token'])['exp'])
        return self.is_valid()
