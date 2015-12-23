# coding=utf-8

from django.conf.urls import url
from core.registration import views

urlpatterns = [
    # sessions
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    # register, 暂不开放注册
    # url(r'^register/$', views.RegisterView.as_view(), name='register'),
    # url(r'^register/success/$', views.RegisterSuccessView.as_view(),
    # name='register-success')

]