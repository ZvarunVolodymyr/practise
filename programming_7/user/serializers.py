from rest_framework import serializers
from user.models import User
import functools
from validation import validator_
from user.validation import validation
from django.core.exceptions import ObjectDoesNotExist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'id_of_certificate', 'first_name', 'last_name', 'email', 'password')
        write_only_fields = ["password"]

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


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        write_only_fields = ["password"]

    def validator(self, data):
        return validator_(self, data, validation)