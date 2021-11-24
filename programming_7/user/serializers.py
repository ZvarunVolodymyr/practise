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
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'birth_date', 'orders_count')
        extra_kwargs = {'password': {'write_only': True}}

    def validator(self, data, **obj):
        return_ = validator_(self, data, validation)
        try:
            obj['User'].get(email=data['email'])
            raise serializers.ValidationError({'email': 'ця пошта вже зайнята'})
        except ObjectDoesNotExist:
            pass

        return return_


class ChangeOrdersCount(serializers.Serializer):
    class Meta:
        fields = ('orders_count')

    def validator(self, data):
        self.is_valid()
        print(data['orders_count'])
        print('@'*100)
        try:
            data['orders_count'] = int(data['orders_count'])
            if data['orders_count'] < 0:
                raise ValueError
        except Exception as error:
            raise serializers.ValidationError({'orders_count': error})
        return True


class TokenBlackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenBlackList
        fields = ('token', 'exp')

    def validator(self, data):
        data['exp'] = int(JWT_decode(data['token'])['exp'])
        return self.is_valid()

# 7295
# 5660