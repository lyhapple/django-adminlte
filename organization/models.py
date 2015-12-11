# coding=utf-8

from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from adminlte import constants
from adminlte.models import BaseModel, User


class AbstractPerson(BaseModel):
    real_name = models.CharField(verbose_name=u'真实姓名', max_length=20)
    sex = models.CharField(verbose_name=u'性别', max_length=10,
                           choices=constants.SEX)
    cellphone = models.CharField(verbose_name=u'手机', max_length=11)
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    qq = models.CharField(verbose_name=u'QQ', max_length=20, null=True,
                          blank=True)
    email = models.EmailField(verbose_name=u'邮箱', max_length=100, null=True,
                              blank=True)
    location = models.CharField(verbose_name=u'地址', max_length=200, null=True,
                                blank=True)
    avatar = models.ImageField(verbose_name=u'相片', null=True, blank=True,
                               upload_to='adminlte/user_avatar', default=None)

    class Meta:
        abstract = True


class Company(MPTTModel, BaseModel):
    name = models.CharField(max_length=200, unique=True,
                            verbose_name=u'公司名称')
    parent = TreeForeignKey('self', verbose_name=u'上级公司',
                            null=True, blank=True,
                            related_name='company_children',
                            )

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name_plural = verbose_name = u'公司'

    class Config:
        list_display_fields = ('name', 'parent', 'id')
        list_form_fields = list_display_fields


class Department(MPTTModel, BaseModel):
    company = models.ForeignKey(Company, verbose_name='所属公司',
                                related_name='departments', default=None,
                                null=True, blank=True)
    name = models.CharField(max_length=50, unique=True,
                            verbose_name=u'部门名称')
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='department_children',
                            verbose_name=u'上级部门')

    class Meta:
        verbose_name_plural = verbose_name = u'部门'

    class MPTTMeta:
        order_insertion_by = ['name']

    class Config:
        list_display_fields = ('company', 'parent', 'name', 'id')
        list_form_fields = list_display_fields

    def __unicode__(self):
        return u'[%s]%s' % (self.company, self.name)


class Staff(AbstractPerson):
    IN_JOB = 1
    OUT_JOB = 2
    STAFF_STATUS = (
        (IN_JOB, u'在职'),
        (OUT_JOB, u'离职'),
    )
    user = models.OneToOneField(User, verbose_name=u'登录账号',
                                related_name='staff_of')
    department = models.ForeignKey(Department, verbose_name=u'所在部门')
    status = models.IntegerField(verbose_name=u'状态',
                                 choices=STAFF_STATUS,
                                 default=IN_JOB)
    position = models.PositiveSmallIntegerField(
        verbose_name=u'职位',
        null=True, blank=True,
        choices=constants.Position.POSITIONS,
        default=constants.Position.STAFF
    )

    def __unicode__(self):
        return u'%s-%s' % (self.department, self.login_name)

    class Meta:
        verbose_name_plural = verbose_name = u'员工'

    class Config:
        list_display_fields = ('user', 'real_name', 'department', 'cellphone',
                               'status', 'position', 'id')
        list_form_fields = list_display_fields + ('avatar', )


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, verbose_name=u'用户')
#     avatar = models.ImageField(verbose_name=u'头像', null=True, blank=False,
#                                upload_to='adminlte/user_avatar')
#
#     class Meta:
#         verbose_name_plural = verbose_name = u'用户资料'
#
#     class Config:
#         list_display_fields = ('user', 'id')
#         list_form_fields = ('user', 'avatar', 'id')
#
#         @classmethod
#         def filter_queryset(cls, request, queryset):
#             return queryset.exclude(
#                 user=User.objects.filter(
#                     is_superuser=True, is_active=True
#                 ).first()
#             )
