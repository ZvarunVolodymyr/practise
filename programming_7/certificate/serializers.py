from rest_framework import serializers
from certificate.models import Certificate
from helping_func.validation_functions import validation
import functools
# from validation import validator_

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'type', 'username', 'birth_date', 'start_date', 'end_date', 'international_passport', 'vaccine'
                  , 'user_id')

    def validator(self, data):
        is_valid_ = functools.partial(validation, data=data)
        errors = {}

        self.is_valid()
        for i in self.errors.items():
            errors[i[0]] = i[1][0]

        for i in data.keys():
            try:
                data[i] = is_valid_(i)
            except Exception as error:
                data[i] = None
                errors[i] = error

        if len(errors) != 0:
            raise serializers.ValidationError(errors)
        return data
