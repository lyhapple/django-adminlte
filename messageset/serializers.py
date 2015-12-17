# coding=utf-8
from rest_framework import serializers
from .models import Task, Notification, SiteMailReceive, SiteMailSend

__author__ = 'lyhapple'


class SiteMailReceiveSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username')
    status = serializers.SerializerMethodField()
    status_value = serializers.IntegerField(source='status')
    sender_avatar = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()

    def get_sender_avatar(self, obj):
        return obj.sender.staff_of.avatar.url

    class Meta:
        model = SiteMailReceive
        fields = SiteMailReceive.Config.list_display_fields + (
            'sender_avatar', 'status_value'
        )
        read_only_fields = (
            'id', 'send_time', 'sender_avatar', 'status_value'
        )


class SiteMailSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteMailSend
        fields = SiteMailSend.Config.list_display_fields
        read_only_fields = (
            'id', 'send_time'
        )


class NotificationSerializer(serializers.ModelSerializer):
    content = serializers.CharField(source='content.contents')
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Notification
        fields = (
            'id', 'title', 'content', 'status', 'send_time', 'read_time',
            'creator', 'created_at'
        )
        read_only_fields = (
            'id', 'created_at'
        )


class TaskSerializer(serializers.ModelSerializer):
    percent = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_percent(self, obj):
        return '%s%%' % obj.percent

    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'percent', 'start_app', 'status',
            'start_time', 'end_time',
            'creator', 'created_at'
        )
        read_only_fields = (
            'id', 'created_at', 'status'
        )