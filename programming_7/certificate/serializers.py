from rest_framework import serializers
from certificate.models import Certificate
from certificate.validation import vaccine_validation
import functools
from validation import validator_

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'username', 'birth_date', 'start_date', 'end_date', 'international_passport', 'vaccine')

    def validator(self, data):
        return validator_(self, data, vaccine_validation)
