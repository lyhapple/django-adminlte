# coding=utf-8

from django.contrib import admin
from .models import (SiteMailSend, Notification, Task, NotificationContent,
                     SiteMailContent, SiteMailReceive)


@admin.register(SiteMailContent)
class SiteMailContentAdmin(admin.ModelAdmin):
    pass


@admin.register(SiteMailSend)
class SiteMailSendAdmin(admin.ModelAdmin):
    pass


@admin.register(SiteMailReceive)
class SiteMailReceiveAdmin(admin.ModelAdmin):
    pass


@admin.register(NotificationContent)
class NotificationContentAdmin(admin.ModelAdmin):
    pass


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

