import rest_framework.request

from django.utils.decorators import method_decorator
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from user.models import User
from user.serializers import UserSerializer, LoginSerializer
from certificate.serializers import CertificateSerializer
from user import security
from certificate.models import Certificate
from django.core.exceptions import ObjectDoesNotExist
from user import swagger_info


class view(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_info.users_post()
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.validator(data, User=User.objects, Certificate=Certificate.objects):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class detail_view(APIView):
    def get_by_id(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response({'message': 'аккаунту з таким ід не існує'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_info.users_delete()
    def delete(self, request, pk):
        obj = self.get_by_id(pk)
        if type(obj) == Response:
            return obj
        obj.delete()
        return Response({'message': 'Аккаунт успішно видалено'}, status=status.HTTP_204_NO_CONTENT)


class login_view(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_info.login_post()
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = LoginSerializer(data=data)
        if serializer.validator(data):
            data = serializer.data
            try:
                User.objects.get(email=data['email'], password=data['password'])
            except User.DoesNotExist:
                return Response({'message': 'неправильний логін або пароль'}, status=status.HTTP_400_BAD_REQUEST)

            security.JWT_encode({'email':data['email']}, 'token.txt')
            return Response({'messege': 'ви залогінились успішно. Токен, зберігся в token.txt'},
                            status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_info.login_get()
    def get(self, request):
        token = request.GET.get('token', None)
        if token is None:
           token = security.read_token()

        try:
            token = security.JWT_decode(token)
        except:
            token = None

        if token is None:
            return Response({'messege': 'ви не залогінені'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=token['email'])
            certificate = Certificate.objects.get(pk=user.id_of_certificate)
        except ObjectDoesNotExist:
            return Response({'message':'не існує сертифікат або аккаунта'}, status=status.HTTP_404_NOT_FOUND)
        print(certificate.__str__)
        user_serializer = UserSerializer(user)
        certificate_serializer = CertificateSerializer(certificate)
        return Response([user_serializer.data, certificate_serializer.data], status=status.HTTP_200_OK)

    @swagger_info.login_delete()
    def delete(self, request):
        security.remove_token()
        return Response({'message':'ви вийшли з аккаунту'}, status=status.HTTP_200_OK)

