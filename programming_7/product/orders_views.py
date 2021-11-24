from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView

from helping_func.date_functions import ymd_to_dmy, date_plus_date, dmy_to_ymd
from certificate.models import Certificate
from certificate.serializers import CertificateSerializer
from product.models import Product
from product.serializers import ProductSerializer, OrderSerializer
from user.models import User
from user.serializers import UserSerializer


class view(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)
        user = request.user
        if serializer.validator(data, user):
            new_certificate_data = \
            {
                'type': data['type'],
                'username': user.first_name + '_' + user.last_name,
                "birth_date": user.birth_date,
                "start_date": data['date'],
                "end_date": dmy_to_ymd(date_plus_date(ymd_to_dmy(data['date']),
                                                      '0.0.1' if data['type'] == 'green' else '0.6.0')),
                "international_passport": data['international_passport'],
                "vaccine": data['name'],
                "user_id": user.id
            }
            product = Product.objects.get(name=data['name'])
            new_product_data = \
                {
                    'name': data['name'],
                    'count': product.count - 1
                }
            user = User.objects.get(pk=user.id)
            new_user_data = UserSerializer(user).data
            new_user_data['orders_count'] = user.orders_count - 1
            new_user_data['password'] = user.password
            new_user_serializer = UserSerializer(user, data=new_user_data)
            new_certificate_serializer = CertificateSerializer(data=new_certificate_data)
            new_product_serializer = ProductSerializer(product, data=new_product_data)

            if new_certificate_serializer.is_valid() and new_product_serializer.is_valid() and \
                    new_user_serializer.is_valid():
                new_certificate_serializer.save()
                new_product_serializer.save()
                new_user_serializer.save()
                return Response(new_certificate_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.user
        certificates = Certificate.objects.filter(user_id=str(user.id))
        answer = []
        for certificate in certificates:
            serializer = CertificateSerializer(certificate)
            answer.append(serializer.data)
        return Response(answer, status=status.HTTP_200_OK)



