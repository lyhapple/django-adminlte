# coding=utf-8
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from adminlte.views import IndexView


# 基础 url
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', login_required(IndexView.as_view())),

    url(r'^auth/', include("registration.urls", namespace="registration")),

    url(r'^jsreverse/$', 'django_js_reverse.views.urls_js', name='js_reverse'),
]

# ===================== 自定义url映射 开始====================================
# 自定义url必须放在通用url的前面，将通用url覆盖掉
# Page url
urlpatterns += [
]
# API url
urlpatterns += [
    url(r'^api/v1/messageset', include('messageset.urls_api',
                                       namespace='messageset_api')),
    # url(r'^api/v1/organization', include('organization.urls',
    #                                      namespace='organization_api')),
]

# ===================== 自定义url映射 结束 ==================================

# 通用URL映射，必须放在最后
urlpatterns += [
    # 通用页面URL映射，必须放在最后
    url(r'^page', include('adminlte.urls', namespace='adminlte')),
    url(r'^api/v1', include('adminlte.urls_api', namespace='adminlte_api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
