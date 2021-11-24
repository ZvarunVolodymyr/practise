from django.conf.urls import url
from product import views
from product import orders_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



urlpatterns = [
    url(r'^api/products$', views.view.as_view()),
    url(r'^api/orders$', orders_views.view.as_view()),
    # url(r'^api/products/(?P<pk>[0-9]+)$', views.detail.as_view())

]