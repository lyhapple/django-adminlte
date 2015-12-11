# coding=utf-8

from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group, User
from mptt.admin import MPTTModelAdmin
from .models import SystemConfig, LteUser, \
    LteGroup, Menu, Resource, Permission

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(LteUser)
class LteUserAdmin(admin.ModelAdmin):
    pass


@admin.register(LteGroup)
class LteGroupAdmin(GroupAdmin):
    pass


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass


@admin.register(SystemConfig)
class SystemConfigAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(MPTTModelAdmin):
    list_display_links = ('name', )
    list_display = ('pk', 'name', 'app_name',
                    'model_name', 'url', 'icon', 'order')
    ordering = ['order']
    pass


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    pass

