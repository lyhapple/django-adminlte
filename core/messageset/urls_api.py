# coding=utf-8
from django.conf.urls import url
from core.messageset import views_api

urlpatterns = [
    url(r'/sitemail/markall', views_api.sitemail_markall,
        name='sitemail_markall'),
]
