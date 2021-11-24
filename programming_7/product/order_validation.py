from certificate.models import Certificate
from rest_framework import serializers
from helping_func.date_functions import comparison
from helping_func.date_functions import ymd_to_dmy
from certificate.models import Certificate


def is_order(data, user):
    user_id = user.id
    certificates = Certificate.objects.filter(user_id=user_id)
    if user.orders_count == 0:
        raise serializers.ValidationError({'user': "аккаунт перевищив кількість замовлень"})
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
        if data['type'] == 'yellow' and last_certificate.type != 'green':
            raise serializers.ValidationError({'name': "після жовтого сертифікату має йти зелений"})
        if last_certificate.type == 'green' and data['type'] != 'yellow':
            raise serializers.ValidationError({'type': "спочатку має йти жовтий сертифікат, а потім зелений"})
    else:
        if data['type'] != 'yellow':
            raise serializers.ValidationError({'type': "спочатку має йти жовтий сертифікат, а потім зелений"})