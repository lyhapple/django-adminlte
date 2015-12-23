# coding=utf-8
from django.conf.urls import url
from core.adminlte.views_api import CommonListAPIView

urlpatterns = [
    url(r'/(?P<app_name>\w+)/(?P<model_name>\w+)',
        CommonListAPIView.as_view(),
        name='common_list_api'),
]
