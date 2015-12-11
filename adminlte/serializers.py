# coding=utf-8
from rest_framework import serializers
from .models import Menu, SystemConfig, Resource, LteUser, LteGroup, Permission

__author__ = 'lyhapple'


class SystemConfigSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return '&nbsp;&nbsp;' * obj.level + obj.name

    class Meta:
        model = SystemConfig
        fields = SystemConfig.Config.list_display_fields
        read_only_fields = ('id', )


class MenuSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return '&nbsp;&nbsp;' * obj.level + obj.name

    class Meta:
        model = Menu
        fields = Menu.Config.list_display_fields
        read_only_fields = ('id', )


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = Resource.Config.list_display_fields
        read_only_fields = ('id', )


class LteUserSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()

    def get_groups(self, obj):
        if not obj.groups.exists():
            return '-'
        else:
            return obj.groups.all().values_list('name', flat=True)

    def get_is_active(self, obj):
        return u'是' if obj.is_active else u'否'

    class Meta:
        model = LteUser
        fields = LteUser.Config.list_display_fields
        read_only_fields = ('id', 'last_login')


class LteGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LteGroup
        fields = LteGroup.Config.list_display_fields
        read_only_fields = ('id', )


class PermissionSerializer(serializers.ModelSerializer):
    group = serializers.CharField(source='group.name')
    menus = serializers.SerializerMethodField()
    resources = serializers.SerializerMethodField()

    def get_menus(self, obj):
        if not obj.menus.exists():
            return '-'
        else:
            return obj.menus.all().values_list('name', flat=True)

    def get_resources(self, obj):
        if not obj.resources.exists():
            return '-'
        else:
            return obj.resources.all().values_list('name', flat=True)

    class Meta:
        model = Permission
        fields = Permission.Config.list_display_fields
        read_only_fields = ('id', )
