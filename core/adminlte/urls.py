# coding=utf-8
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from core.adminlte.views import CommonListPageView, \
    CommonCreatePageView, CommonUpdatePageView, CommonDeletePageView, \
    CommonDetailPageView


urlpatterns = [
    url(r'/403.html', TemplateView.as_view(template_name='adminlte/403.html'),
        name='http403'),

    url(r'/(?P<app_name>\w+)/(?P<model_name>\w+)/list$',
        login_required(CommonListPageView.as_view()),
        name='common_list_page'),

    url(r'/(?P<app_name>\w+)/(?P<model_name>\w+)/create$',
        login_required(CommonCreatePageView.as_view()),
        name='common_create_page'),

    url(r'/(?P<app_name>\w+)/(?P<model_name>\w+)/detail/(?P<pk>\d+)$',
        login_required(CommonDetailPageView.as_view()),
        name='common_detail_page'),

    url(r'/(?P<app_name>\w+)/(?P<model_name>\w+)/update/(?P<pk>\d+)$',
        login_required(CommonUpdatePageView.as_view()),
        name='common_update_page'),

    url(r'/(?P<app_name>\w+)/(?P<model_name>\w+)/delete$',
        login_required(CommonDeletePageView.as_view()),
        name='common_delete_page'),

    # url(r'/page/(?P<app_name>\w+)/(?P<model_name>\w+)/form.html$',
    # TemplateView.as_view(template_name='adminlte/system/config.html'),
    #     name='common_form'),
    #
    # url(r'/page/adminlte/SystemConfig.html$',
    #     TemplateView.as_view(template_name='adminlte/system/config.html'),
    #     name='systemconfig'),
    # url(r'/system/config/form.html$', SystemConfigFormView.as_view(),
    #     name='systemconfig_form'),
    #
    # url(r'/system/role.html$', SiteMailListView.as_view(),
    #     name='role'),
    # url(r'/system/auth.html$', SiteMailListView.as_view(),
    #     name='auth'),
    # url(r'/system/user.html$', SiteMailListView.as_view(),
    #     name='user'),
    #
    # url(r'/page/adminlte/SiteMail.html$', SiteMailListView.as_view(),
    #     name='sitemail'),
    # url(r'/notification.html$', NotificationListView.as_view(),
    #     name='notification'),
    # url(r'/task.html$', TaskListView.as_view(),
    #     name='task'),
]
