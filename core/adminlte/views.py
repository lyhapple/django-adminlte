# coding=utf-8
from django.contrib.auth import views

from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, \
    UpdateView, DeleteView, TemplateView, DetailView
from core.adminlte import constants
from core.adminlte.models import SystemConfig
from core.organization.models import Staff

__author__ = 'lyhapple'


def get_app_model_name(kwargs):
    """
    获取url的app_name与model_name
    :param kwargs:
    :return: 返回获取到的内容
    """
    app_name = kwargs.get('app_name').lower()                                                                           #获取get url 信息
    model_name = kwargs.get('model_name').lower()
    return app_name, model_name


def get_model_content_type(app_name, model_name):
    """
    封装 model 获取类型
    :param app_name: app名称
    :param model_name:mode名称
    :return:
    """
    return ContentType.objects.get(app_label=app_name, model=model_name)


def get_system_config_value(key_name):
    try:
        return SystemConfig.objects.get(name=key_name).value
    except:
        return u'未找到 %s 系统配置项' % key_name


class CommonPageViewMixin(object):
    """
    常见 变量引入
    """
    def get_context_data(self, **kwargs):
        """
        重构get context_data
        """
        context = super(CommonPageViewMixin, self).get_context_data(**kwargs)
        default_dashboard_title = constants.DEFAULT_DASHBOARD_TITLE
        if hasattr(self, 'model'):
            page_title = self.model._meta.verbose_name
        else:
            page_title = default_dashboard_title

        common_dict = {
            'default_dashboard_title': default_dashboard_title,
            'page_title': page_title,
            'page_model': getattr(self, 'model', ''),
            'page_app_name': getattr(self, 'app_name', ''),
            'page_model_name': getattr(self, 'model_name', ''),
            'page_system_name': get_system_config_value('system_name'),
            'page_system_subhead': get_system_config_value('system_subhead')
        }
        context.update(common_dict)
        return context


class IndexView(CommonPageViewMixin, TemplateView):
    """
    默认首页
    """
    template_name = "adminlte/index.html" #页面地址

    def get_context_data(self, **kwargs):
        """
        get 请求返回结果
        """
        context = super(IndexView, self).get_context_data(**kwargs)
        #TODO 下面的方法.可以所称统一类 进行调用
        staff_count = Staff.objects.filter(status=Staff.IN_JOB).count()              #返回员工信息
        context['staff_count'] = staff_count
        return context


class ChangePasswordView(CommonPageViewMixin, TemplateView):
    """
    修改 密码方法.
    """
    def post(self, request, **kwargs):
        self.request = request
        context = super(ChangePasswordView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def render_to_response(self, context, **response_kwargs):
        """
        get 请求时 返回内容
        :param context:基础信息
        :param response_kwargs:
        :return:
        """
        context['page_title'] = u'修改密码'
        template_response = views.password_change(
            self.request,
            template_name='adminlte/change-password.html',
            extra_context=context
        )
        return template_response


class ChangePasswordDoneView(CommonPageViewMixin, TemplateView):
    template_name = 'adminlte/change-password-done.html'


class CommonListPageView(CommonPageViewMixin, ListView):
    """
    列表
    """
    template_name = 'adminlte/common_list.html'

    def get(self, request, *args, **kwargs):
        self.app_name, self.model_name = get_app_model_name(kwargs)                                                     #获取具体的执行方法名
        model_type = get_model_content_type(self.app_name, self.model_name)                                             #封装获取类信息
        self.model = model_type.model_class()                                                                           #返回具体的模型内容
        if hasattr(self.model.Config, 'list_template_name'):                                                            #检测返回具体的页面template_name地址
            self.template_name = self.model.Config.list_template_name
        return super(CommonListPageView, self).get(request, *args, **kwargs)                                            #初始化默认的get方法

    def get_context_data(self, **kwargs):
        """
        get方法时
        :param kwargs:
        :return:
        """
        context = super(CommonListPageView, self).get_context_data(**kwargs)                                            #重载此方法
        titles, fields = self.get_table_titles()
        context['table_titles'] = titles                                                                                #列表_抬头
        context['table_fields'] = list(fields)                                                                          #列表具体内容
        return context                                                                                                  #返回全部信息

    def get_table_titles(self):
        """
        获取 任务列表.与任务抬头
        :return:
        """
        show_fields = self.model.Config.list_display_fields
        meta_fields = self.model._meta.fields
        meta_names = [mf.name for mf in meta_fields]
        titles = []
        for name in show_fields:
            if name not in meta_names:
                t = getattr(self.model, name).field.verbose_name
                titles.append(t)
            for mf in meta_fields:
                if mf.name == name:
                    titles.append(mf.verbose_name)
        return titles, show_fields


class CommonFormPageMixin(CommonPageViewMixin):
    template_name = 'adminlte/common_form.html'

    def set_form_page_attributes(self, *args, **kwargs):
        self.app_name, self.model_name = get_app_model_name(kwargs)
        model_type = get_model_content_type(self.app_name, self.model_name)
        self.model = model_type.model_class()
        self.fields = getattr(self.model.Config, 'list_form_fields', ())
        if hasattr(self.model.Config, 'success_url'):
            self.success_url = self.model.Config.success_url
        else:
            self.success_url = reverse(
                'adminlte:common_list_page',
                kwargs={
                    'app_name': self.app_name,
                    'model_name': self.model_name
                }
            )
        if hasattr(self.model.Config, 'form_template_name'):
            self.template_name = getattr(self.model.Config,
                                         'form_template_name')


class CommonCreatePageView(CommonFormPageMixin, CreateView):
    def get(self, request, *args, **kwargs):
        self.object = None
        self.set_form_page_attributes(*args, **kwargs)
        resp = super(CommonCreatePageView, self).get(request, *args, **kwargs)
        return resp

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(CommonCreatePageView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.set_form_page_attributes(*args, **kwargs)
        return super(CommonCreatePageView, self).post(request, *args, **kwargs)


class CommonDetailPageView(CommonPageViewMixin, DetailView):
    template_name = 'adminlte/common_detail.html'

    def get(self, request, *args, **kwargs):
        self.app_name, self.model_name = get_app_model_name(kwargs)
        model_type = get_model_content_type(self.app_name, self.model_name)
        self.model = model_type.model_class()
        if hasattr(self.model.Config, 'detail_template_name'):
            self.template_name = self.model.Config.detail_template_name
        return super(CommonDetailPageView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        obj = super(CommonDetailPageView, self).get_object(queryset)
        if hasattr(self.model.Config, 'get_object_hook'):
            self.model.Config.get_object_hook(self.request, obj)
        return obj


class CommonUpdatePageView(CommonFormPageMixin, UpdateView):
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        self.set_form_page_attributes(*self.args, **self.kwargs)
        return self.model.objects.filter(pk=pk)


class CommonDeletePageView(CommonFormPageMixin, DeleteView):
    def delete(self, request, *args, **kwargs):
        ret = {'message':'','status':False}
        try:
            objects = self.get_object()
            for obj in objects:
                obj.delete()
            ret['status'] = True
            ret['message'] = u'删除成功'
        except Exception as e :
            ret['message'] = u'%s'%e
        return JsonResponse(ret, status=200)

    def get_queryset(self):
        self.set_form_page_attributes(*self.args, **self.kwargs)
        return self.model.objects.all()

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.request.POST.get('pk')
        pk = pk.split(',')
        return queryset.filter(pk__in=pk)