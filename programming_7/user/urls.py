from django.conf.urls import url
from user import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



urlpatterns = [
    url(r'^api/users$', views.view.as_view()),
    url(r'^api/login$', views.login_view.as_view()),
    url(r'^api/login/user$', views.login_get.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)$', views.detail_view.as_view())
]