# coding=utf-8
from django.contrib.auth.models import User, Group, AbstractBaseUser, \
    AbstractUser
from django.core.urlresolvers import reverse

from django.db import models
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from core.adminlte.constants import UsableStatus, DICT_NULL_BLANK_TRUE


class BaseModel(models.Model):
    creator = models.ForeignKey(
        User,
        verbose_name=u"数据创建人",
        **DICT_NULL_BLANK_TRUE
    )
    created_at = models.DateTimeField(
        verbose_name=u"数据创建时间",
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        verbose_name=u"数据更新时间",
        default=timezone.now
    )
    deleted_at = models.DateTimeField(
        verbose_name=u"数据删除时间",
        **DICT_NULL_BLANK_TRUE
    )

    class Meta:
        abstract = True


class LteUser(User):
    class Meta:
        proxy = True
        app_label = 'adminlte'
        verbose_name_plural = verbose_name = u'用户'

    class Config:
        list_display_fields = (
            'username', 'groups', 'email',
            'is_active', 'last_login', 'id'
        )
        list_form_fields = (
            'username', 'password',
            'password',
            'groups', 'email', 'is_active', 'id'
        )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.set_password(self.password)
        return super(LteUser, self).save(
            force_insert=False,
            force_update=False,
            using=None, update_fields=None
        )


class LteGroup(Group):
    class Meta:
        proxy = True
        app_label = "adminlte"
        verbose_name_plural = verbose_name = u'角色'

    class Config:
        list_display_fields = (
            'name', 'id'
        )
        list_form_fields = list_display_fields


class SystemConfig(MPTTModel, BaseModel, UsableStatus):
    name = models.CharField(
        u"键", max_length=255, unique=True
    )
    value = models.CharField(
        u"值", max_length=255
    )
    title = models.CharField(
        u"描述", max_length=255
    )
    parent = TreeForeignKey(
        'self', verbose_name=u'父配置项',
        related_name='children', db_index=True,
        **DICT_NULL_BLANK_TRUE
    )
    status = models.PositiveSmallIntegerField(
        u'状态', choices=UsableStatus.STATUS,
        default=UsableStatus.USABLE, db_index=True
    )

    def __unicode__(self):
        return u"%s" % self.value

    def get_absolute_url(self):
        return reverse(
            'adminlte:common_detail_page',
            kwargs={
                'app_name': self._meta.app_label,
                'model_name': self._meta.model_name,
                'pk': self.id
            }
        )

    class Meta:
        verbose_name_plural = verbose_name = u"参数配置"

    class MPTTMeta:
        order_insertion_by = ['name']

    class Config:
        list_template_name = 'adminlte/systemconfig_list.html'
        list_display_fields = ('name', 'parent', 'value', 'title', 'id')
        list_form_fields = ('parent', 'name', 'value', 'title', 'id')
        search_fields = ('name', 'value', 'title')


class Menu(MPTTModel, BaseModel, UsableStatus):
    name = models.CharField(
        u'菜单名称', max_length=50, unique=True
    )
    icon = models.CharField(
        u'菜单图标', max_length=50, default='fa-circle-o',
        help_text=u'参考:http://fontawesome.io'
    )
    parent = TreeForeignKey(
        'self', verbose_name=u'上级菜单',
        related_name='children',
        db_index=True, **DICT_NULL_BLANK_TRUE
    )
    app_name = models.CharField(
        u'App名称', max_length=200, **DICT_NULL_BLANK_TRUE
    )
    model_name = models.CharField(
        u'Model名称', max_length=200,
        help_text=u'注意大小写',
        **DICT_NULL_BLANK_TRUE
    )
    url = models.CharField(
        u'全路径', max_length=200,
        help_text=u'选填', **DICT_NULL_BLANK_TRUE
    )
    order = models.PositiveSmallIntegerField(
        u'排序', default=0
    )
    status = models.PositiveSmallIntegerField(
        u'状态', choices=UsableStatus.STATUS,
        default=UsableStatus.USABLE, db_index=True
    )

    def __unicode__(self):
        return u'%s(%s)' % (self.name, self.order)

    def get_absolute_url(self):
        return reverse(
            'adminlte:common_detail_page',
            kwargs={
                'app_name': self._meta.app_label,
                'model_name': self._meta.model_name,
                'pk': self.id
            }
        )

    class Meta:
        verbose_name_plural = verbose_name = u'菜单'
        ordering = ('order', )

    class MPTTMeta:
        order_insertion_by = ['order']

    class Config:
        list_display_fields = (
            'name', 'app_name',
            'model_name', 'url', 'icon', 'order', 'id'
        )
        list_form_fields = ('parent',) + list_display_fields
        search_fields = (
            'name', 'app_name', 'model_name', 'icon'
        )

        @classmethod
        def filter_queryset(cls, request, queryset):
            return queryset.filter(status=Menu.USABLE)


class Resource(BaseModel, UsableStatus):
    name = models.CharField(
        u'资源名称', max_length=50
    )
    app_name = models.CharField(
        u'所属应用', max_length=200, **DICT_NULL_BLANK_TRUE
    )
    model_name = models.CharField(
        u'所属模型', max_length=200,
        **DICT_NULL_BLANK_TRUE
    )
    url = models.CharField(
        u'资源地址', max_length=500,
        help_text=u'API地址', **DICT_NULL_BLANK_TRUE
    )
    note = models.CharField(
        u'备注', max_length=500,
        **DICT_NULL_BLANK_TRUE
    )
    status = models.PositiveSmallIntegerField(
        u'状态', choices=UsableStatus.STATUS,
        default=UsableStatus.USABLE, db_index=True
    )

    def __unicode__(self):
        return u'%s(%s)' % (self.name, self.note)

    def get_absolute_url(self):
        return reverse(
            'adminlte:common_detail_page',
            kwargs={
                'app_name': self._meta.app_label,
                'model_name': self._meta.model_name,
                'pk': self.id
            }
        )

    class Meta:
        verbose_name_plural = verbose_name = u'API资源'

    class Config:
        list_display_fields = (
            'name', 'app_name', 'model_name', 'url', 'id'
        )
        list_form_fields = list_display_fields


class Permission(BaseModel, UsableStatus):
    group = models.ForeignKey(
        LteGroup, verbose_name=u'角色',
        related_name='group_permission'
    )
    menus = models.ManyToManyField(
        Menu, verbose_name=u'菜单',
        blank=True
    )
    resources = models.ManyToManyField(
        Resource, verbose_name=u'资源',
        blank=True
    )
    status = models.PositiveSmallIntegerField(
        u'状态', choices=UsableStatus.STATUS,
        default=UsableStatus.USABLE, db_index=True
    )

    def __unicode__(self):
        return self.group.name

    def get_absolute_url(self):
        return reverse(
            'adminlte:common_detail_page',
            kwargs={
                'app_name': self._meta.app_label,
                'model_name': self._meta.model_name,
                'pk': self.id
            }
        )

    class Meta:
        verbose_name_plural = verbose_name = u'权限'

    class Config:
        list_display_fields = (
            'group', 'menus', 'resources', 'id'
        )
        list_form_fields = list_display_fields
