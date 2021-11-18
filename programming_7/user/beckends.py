import jwt

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import authentication, exceptions
from user.security import JWT_decode
from user.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Bearer'

    def authenticate(self, request):
        request.user = None
        header = authentication.get_authorization_header(request).split()
        prefix = self.authentication_header_prefix.lower()
        if not header or len(header) == 1 or len(header) > 2:
            return None

        prefix = header[0].decode('utf-8')
        token = header[1].decode('utf-8')

        if prefix.lower() != prefix.lower():
            return None
        token = JWT_decode(token)
        try:
            user = User.objects.get(email=token['email'])
        except ObjectDoesNotExist:
            raise exceptions.AuthenticationFailed('не існує сертифікат або аккаунта')
        return user, token
