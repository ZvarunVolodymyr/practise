from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from helping_func.date_functions import ymd_to_dmy
from certificate.models import Certificate
from product.models import Product
from helping_func.validation import validator_
from helping_func.validation_functions import validation
from helping_func.date_functions import comparison
from product.order_validation import is_order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'count')

    def validator(self, data):
        return_ = validator_(self, data, validation)
        try:
            Product.objects.get(name=data['name'])
            raise serializers.ValidationError({'name': "продукт з таким ім'м вже існує"})
        except ObjectDoesNotExist:
            pass
        return return_


class OrderSerializer(serializers.Serializer):
    class Meta:
        fields = ('name', 'date', 'type', 'international_passport')

    def validator(self, data, user):

        return_ = validator_(self, data, validation)
        try:
            product = Product.objects.get(name=data['name'])
            if product.count == 0:
                raise
        except Exception:
            raise serializers.ValidationError({'name': "немає продукту з таким іменем або він закінчився"})

        is_order(data, user)

        return return_
