# coding=utf-8
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from core.adminlte.views import IndexView, ChangePasswordView, \
    ChangePasswordDoneView


# 基础 url
urlpatterns = [
    url('^page/change-password/$', ChangePasswordView.as_view(),
        name='change_password'),                                                                                        #修改密码方法
    url('^page/change-password-done/$', ChangePasswordDoneView.as_view(),
        name='password_change_done'),                                                                                   #修改密码成功方法

    url(r'^admin/', include(admin.site.urls)),                                                                          #调用系统后台

    url(r'^$', login_required(IndexView.as_view()), name='index'),                                                      #检查是否登录.没登录 跳转到登录页面

    url(r'^auth/', include("core.registration.urls",
                           namespace="registration")),                                                                  #登录.注册相关

    url(r'^jsreverse/$', 'django_js_reverse.views.urls_js', name='js_reverse'),                                         #django js压缩相关
]

# ===================== 自定义url映射 开始====================================
# 自定义url必须放在通用url的前面，将通用url覆盖掉
# Page url
urlpatterns += [
]
# API url
urlpatterns += [
    url(r'^api/v1/messageset', include('core.messageset.urls_api',
                                       namespace='messageset_api')),
    # url(r'^api/v1/organization', include('organization.urls',
    # namespace='organization_api')),
]

# ===================== 自定义url映射 结束 ==================================

# 通用URL映射，必须放在最后
urlpatterns += [
    # 通用页面URL映射，必须放在最后
    url(r'^page', include('core.adminlte.urls', namespace='adminlte')),
    url(r'^api/v1', include('core.adminlte.urls_api',
                            namespace='adminlte_api')),
]

if settings.DEBUG: #如果 开启 DEBUG 模式.会默认加载相关的目录信息
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
