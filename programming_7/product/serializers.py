from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from helping_func.date_functions import ymd_to_dmy
from certificate.models import Certificate
from product.models import Product
from helping_func.validation import validator_
from helping_func.validation_functions import validation
from helping_func.date_functions import comparison


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

    def validator(self, data, user_id):
        return_ = validator_(self, data, validation)
        try:
            product = Product.objects.get(name=data['name'])
            if product.count == 0:
                raise
        except Exception:
            raise serializers.ValidationError({'name': "немає продукту з таким іменем або він закінчився"})

        certificates = Certificate.objects.filter(user_id=user_id)
        if len(certificates) != 0:
            last_certificate = certificates[0]
            for certificate in certificates:
                print(certificate.id)
                if comparison(ymd_to_dmy(str(last_certificate.end_date)), ymd_to_dmy(str(certificate.end_date))):
                    last_certificate = certificate
            if comparison(ymd_to_dmy(data['date']), ymd_to_dmy(str(last_certificate.end_date))):
                raise serializers.ValidationError({'date': "дата пересікається з терміном іншого сертифікату"})
            if last_certificate.type == 'yellow' and last_certificate.vaccine != data['name']:
                raise serializers.ValidationError({'name': "2 доза має бути тією ж вакциною"})
            if last_certificate.type == 'green' and data['type'] != 'yellow':
                raise serializers.ValidationError({'type': "спочатку має йти жовтий сертифікат, а потім зелений"})
        else:
            if data['type'] != 'yellow':
                raise serializers.ValidationError({'type': "спочатку має йти жовтий сертифікат, а потім зелений"})

        return return_
