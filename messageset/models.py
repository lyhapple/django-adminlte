# coding=utf-8
import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from adminlte.constants import ReadStatus, TaskStatus, MailStatus, \
    UsableStatus, \
    DICT_NULL_BLANK_TRUE
from adminlte.models import BaseModel


class SiteMail(BaseModel, MailStatus):
    title = models.CharField(
        verbose_name=u'主题', max_length=200
    )
    contents = models.TextField(verbose_name=u'内容')
    sender = models.ForeignKey(
        User,
        related_name='sitemail_sender',
        verbose_name=u'发件人', **DICT_NULL_BLANK_TRUE
    )
    receiver = models.ForeignKey(
        User, related_name='sitemail_receiver',
        verbose_name=u'收件人',
        **DICT_NULL_BLANK_TRUE
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=u'读取状态',
        choices=MailStatus.STATUS,
        default=MailStatus.UNREAD,
        db_index=True
    )
    send_time = models.DateTimeField(
        verbose_name=u'发送时间', auto_now_add=True, **DICT_NULL_BLANK_TRUE
    )
    read_time = models.DateTimeField(
        verbose_name=u'读取时间', **DICT_NULL_BLANK_TRUE
    )

    def __unicode__(self):
        return u'<站内邮件-%s-%s>' % (self.pk, self.title)

    class Meta:
        verbose_name_plural = verbose_name = u'站内邮件'

    class Config:
        list_template_name = 'messageset/sitemail_list.html'
        form_template_name = 'messageset/sitemail_form.html'
        list_display_fields = (
            'title', 'sender', 'receiver',
            'status', 'send_time', 'id'
        )
        list_form_fields = (
            'title', 'sender', 'receiver', 'contents'
        )
        filter_fields = ('status', )
        search_fields = ()

        @classmethod
        def filter_queryset(cls, request, queryset):
            if 'receiver' in request.query_params \
                    or 'sender' in request.query_params \
                    or 'trash' in request.query_params:
                receive = request.query_params.get('receive', None)
                if receive:
                    queryset = queryset.filter(receiver=request.user).exclude(
                        status=SiteMail.DELETED
                    )

                sender = request.query_params.get('sender', None)
                if sender:
                    queryset = queryset.filter(sender=request.user).exclude(
                        status=SiteMail.DELETED
                    )
                trash = request.query_params.get('trash', None)
                if trash:
                    queryset = queryset.filter(
                        Q(status=SiteMail.DELETED),
                        Q(sender=request.user) | Q(receiver=request.user)
                    )
            else:
                queryset = SiteMail.objects.none()
            return queryset

        @classmethod
        def get_object_hook(cls, request, obj):
            obj.status = ReadStatus.READ
            if not obj.read_time:
                obj.read_time = datetime.datetime.now()
            obj.save()


class NotificationContent(BaseModel, UsableStatus):
    title = models.CharField(
        verbose_name=u'标题', max_length=200
    )
    contents = models.TextField(verbose_name=u'内容')
    receivers = models.ManyToManyField(
        User, blank=True,
        related_name='receivers',
        verbose_name=u'接收人',
        help_text=u'不选则发送给全体用户'
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=u'状态',
        choices=UsableStatus.STATUS,
        default=UsableStatus.USABLE,
        db_index=True
    )

    class Meta:
        verbose_name_plural = verbose_name = u'系统通知内容'

    def __unicode__(self):
        return self.title


class Notification(BaseModel, ReadStatus):
    title = models.CharField(
        verbose_name=u'标题', max_length=200,
        default='', **DICT_NULL_BLANK_TRUE
    )
    content = models.ForeignKey(
        NotificationContent, verbose_name=u'内容', **DICT_NULL_BLANK_TRUE
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=u'读取状态',
        choices=ReadStatus.STATUS,
        default=ReadStatus.UNREAD,
        db_index=True
    )
    send_time = models.DateTimeField(
        verbose_name=u'发送时间', auto_now_add=True, **DICT_NULL_BLANK_TRUE
    )
    read_time = models.DateTimeField(
        verbose_name=u'读取时间', **DICT_NULL_BLANK_TRUE
    )
    receiver = models.ForeignKey(
        User,
        related_name='+',
        verbose_name=u'接收人',
        **DICT_NULL_BLANK_TRUE
    )

    def __unicode__(self):
        return u'<系统通知-%s-%s>' % (self.pk, self.content.title)

    class Meta:
        verbose_name_plural = verbose_name = u'系统通知'

    class Config:
        list_template_name = 'messageset/notification_list.html'
        list_display_fields = (
            'title', 'status', 'send_time', 'id'
        )
        list_form_fields = (
            'title', 'content.contents', 'send_time'
        )
        filter_fields = ('status',)
        search_fields = ('title',)

        @classmethod
        def filter_queryset(cls, request, queryset):
            return queryset.exclude(status=Notification.DELETED).filter(
                receiver=request.user
            )

        @classmethod
        def get_object_hook(cls, request, obj):
            obj.status = ReadStatus.READ
            if not obj.read_time:
                obj.read_time = datetime.datetime.now()
            obj.save()


@receiver(post_save, sender=NotificationContent)
def create_notification_datas(sender, instance, **kwargs):
    """
    保存系统通知时，给所选用户发送通知，
    目前是向Notification表添加数据
    这里将来可以替换为异步消息队列
    :param sender:
    :param instance:
    :param kwargs:
    """
    for user in instance.receivers.all():
        exists = Notification.objects.filter(
            receiver=user, content=instance
        ).exists()
        if not exists:
            nf = Notification()
            nf.title = instance.title
            nf.content = instance
            nf.receiver = user
            nf.creator = instance.creator
            nf.status = Notification.UNREAD
            nf.save()


class Task(BaseModel, TaskStatus):
    name = models.CharField(
        verbose_name=u'任务名称', max_length=200
    )
    percent = models.PositiveIntegerField(
        verbose_name=u'进度', default=0
    )
    start_app = models.CharField(
        verbose_name=u'发起app', max_length=255, **DICT_NULL_BLANK_TRUE
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=u'状态',
        choices=TaskStatus.TASK_STATUS,
        default=TaskStatus.NORMAL,
        db_index=True
    )
    start_time = models.DateTimeField(
        verbose_name=u'开始时间', auto_now_add=True, **DICT_NULL_BLANK_TRUE
    )
    end_time = models.DateTimeField(
        verbose_name=u'结束时间', **DICT_NULL_BLANK_TRUE
    )

    def __unicode__(self):
        return u'<后台任务-%s-%s>' % (self.pk, self.name)

    class Meta:
        verbose_name_plural = verbose_name = u'后台任务'

    class Config:
        # 列表页模板
        list_template_name = 'messageset/task_list.html'
        # 列表页展现的字段
        list_display_fields = (
            'name', 'percent', 'start_app', 'status',
            'start_time', 'end_time', 'id'
        )
        # 表单页需要填写的字段
        list_form_fields = (
            'name', 'percent', 'start_app', 'status'
        )
        # 数据过滤
        filter_fields = ('status', )
        # 模糊搜索
        search_fields = ('name', 'start_app')

        @classmethod
        def filter_queryset(cls, request, queryset):
            return queryset.filter(creator=request.user).exclude(
                status=TaskStatus.DELETED
            )
