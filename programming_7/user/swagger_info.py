from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from certificate.serializers import CertificateSerializer

properties = {
                "id": openapi.Schema(description='id of user', type=openapi.TYPE_INTEGER),
                'id_of_certificate': openapi.Schema(description='id of user certificate', type=openapi.TYPE_STRING),
                'first_name': openapi.Schema(description='first name', type=openapi.FORMAT_DATE),
                'last_name': openapi.Schema(description='last name', type=openapi.FORMAT_DATE),
                'email': openapi.Schema(description='email', type=openapi.FORMAT_DATE),
                'password': openapi.Schema(description='password([A-Z, a-z, 0-9] format)', type=openapi.TYPE_STRING),
            }
example = {
                "id_of_certificate": "25",
                "first_name": "name",
                "last_name": "name",
                "email": "name13@mail.ua",
                "password": "Admin123"
            }
example_certificate = {
                'username': 'name',
                "birth_date": "2001-1-1",
                "start_date": "2001-5-1",
                "end_date": "2001-6-1",
                "international_passport": "aa000000",
                "vaccine": "pfizer"
            }


def users_post():
    return swagger_auto_schema(
        operation_description="sign up",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['id', 'id_of_certificate', 'first_name', 'last_name', 'email', 'password'],
            properties=properties,
            example=example),
            responses={
                201: openapi.Response(
                    description="user added successful",
                    examples={
                        'application/json': {
                            'message': 'акаунт зареєстровано',
                            'status': '201'}
                    }
                ),
                400: openapi.Response(
                    description="user invalid",
                    examples={
                        'application/json': {
                            'message': "ab1 : не є ім'ям",
                            'status': '400'}
                    }
                )
            }
    )


def users_delete():
    return swagger_auto_schema(
        operation_description="delete user by id",
        responses={
            204: openapi.Response(
                description="certificate deleted",
                examples={
                    'application/json': {
                        'message': 'Аккаунт успішно видалено',
                        'status': '204'}
            }
            ),
            404: openapi.Response(
                description="invalid id",
                examples={
                    'application/json': {
                        'message': "аккаунту з таким ід не існує",
                        'status': '404'}
                }
            )
        }
    )


def login_get():
    return swagger_auto_schema(
        operation_description="get info user and certificate",
        responses={
                    200: openapi.Response(
                        description="success",
                        examples={
                            'application/json': {
                                'message': str(example) + ',' + str(example_certificate),
                                'status': '200'}
                        }
                    ),
                    400: openapi.Response(
                        description="isn't login",
                        examples={
                            'application/json': {
                                'message': "ви не залогінені",
                                'status': '404'}
                        }
                    ),
                    404: openapi.Response(
                        description="invalid certificate or user",
                        examples={
                            'application/json': {
                                'message': "не існує сертифікат або акканунта",
                                'status': '404'}
                        }
            )
        }
    )


def login_delete():
    return swagger_auto_schema(
        operation_description="log out",
        responses={
            204: openapi.Response(
                description="log outed",
                examples={
                    'application/json': {
                        'message': 'ви вийшли з аккаунту',
                        'status': '200'}
            }
            )
        }
    )

def login_post():
    return swagger_auto_schema(
        operation_description="log in",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password'],
            properties={'email': openapi.Schema(description='email', type=openapi.FORMAT_DATE),
                'password': openapi.Schema(description='password([A-Z, a-z, 0-9] format)', type=openapi.TYPE_STRING),},
            example={"email": "name13@mail.ua",
                "password": "Admin123"}),
            responses={
                200: openapi.Response(
                    description="log in success",
                    examples={
                        'application/json': {
                            'message': 'ви залогінились успішно. Токен, зберігся в token.txt',
                            'status': '200'}
                    }
                ),
                400: openapi.Response(
                    description="log in fail",
                    examples={
                        'application/json': {
                            'message': "неправильний логін або пароль",
                            'status': '400'}
                    }
                )
            }
    )