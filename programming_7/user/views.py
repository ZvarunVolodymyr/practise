from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from user.models import User
from user.serializers import UserSerializer
from helping_func import security
from certificate.models import Certificate
from user import swagger_info
from user.serializers import TokenBlackListSerializer
from helping_func.permission import IsSuperUserOrReadOnly

class view(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @swagger_info.users_post()
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.validator(data, User=User.objects, Certificate=Certificate.objects):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class detail_view(APIView):
    permission_classes = (IsSuperUserOrReadOnly,)
    @swagger_info.users_delete()
    def delete(self, request, pk):
        try:
            obj = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'message': 'аккаунту з таким ід не існує'}, status=status.HTTP_404_NOT_FOUND)
        if type(obj) == Response:
            return obj
        obj.delete()
        return Response({'message': 'Аккаунт успішно видалено'}, status=status.HTTP_204_NO_CONTENT)


class login_view(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @swagger_info.login_post()
    def post(self, request):
        data = request.data
        data['password'] = security.hash(data['password'])
        try:
            user = User.objects.get(email=data['email'], password=data['password'])
        except User.DoesNotExist:
            return Response({'message': 'неправильний логін або пароль'}, status=status.HTTP_400_BAD_REQUEST)
        token = security.JWT_encode({'email':data['email']})
        return Response({'token': token, 'messege': 'ви залогінились успішно'},
                        status=status.HTTP_200_OK)


class login_get(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_info.login_delete()
    def delete(self, request):
        data = {}
        token_str = request.headers['Authorization']
        token_str = token_str[token_str.find(' ') + 1:]
        data['token'] = token_str
        token = TokenBlackListSerializer(data=data)
        if token.validator(data):
            token.save()
            return Response({'message':'ви вийшли з аккаунту'}, status=status.HTTP_200_OK)
        return Response({'error': token.errors, 'message':'помилка виходу'}, status=status.HTTP_400_BAD_REQUEST)
