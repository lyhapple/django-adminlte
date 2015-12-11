# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adminlte.constants
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4', null=True)),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898')),
                ('contents', models.TextField(verbose_name='\u5185\u5bb9')),
                ('status', models.PositiveSmallIntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb'), (99, '\u5220\u9664')])),
                ('send_time', models.DateTimeField(null=True, verbose_name='\u53d1\u9001\u65f6\u95f4', blank=True)),
                ('read_time', models.DateTimeField(null=True, verbose_name='\u8bfb\u53d6\u65f6\u95f4', blank=True)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u7cfb\u7edf\u901a\u77e5',
                'verbose_name_plural': '\u7cfb\u7edf\u901a\u77e5',
            },
            bases=(models.Model, adminlte.constants.ReadStatus),
        ),
        migrations.CreateModel(
            name='SiteMail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4', null=True)),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898')),
                ('contents', models.TextField(verbose_name='\u5185\u5bb9')),
                ('status', models.PositiveSmallIntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb'), (99, '\u5220\u9664')])),
                ('send_time', models.DateTimeField(null=True, verbose_name='\u53d1\u9001\u65f6\u95f4', blank=True)),
                ('read_time', models.DateTimeField(null=True, verbose_name='\u8bfb\u53d6\u65f6\u95f4', blank=True)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('receiver', models.ForeignKey(related_name='sitemail_receiver', verbose_name='\u63a5\u6536\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('sender', models.ForeignKey(related_name='sitemail_sender', verbose_name='\u53d1\u9001\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u7ad9\u5185\u90ae\u4ef6',
                'verbose_name_plural': '\u7ad9\u5185\u90ae\u4ef6',
            },
            bases=(models.Model, adminlte.constants.ReadStatus),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4', null=True)),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('percent', models.PositiveIntegerField(default=0, verbose_name='\u8fdb\u5ea6')),
                ('start_app', models.CharField(max_length=255, null=True, verbose_name='\u53d1\u8d77app', blank=True)),
                ('status', models.PositiveSmallIntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38(\u8fdb\u884c\u4e2d)'), (1, '\u5f02\u5e38'), (2, '\u5b8c\u6210'), (9, '\u5220\u9664')])),
                ('start_time', models.DateTimeField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4', blank=True)),
                ('end_time', models.DateTimeField(null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u540e\u53f0\u4efb\u52a1',
                'verbose_name_plural': '\u540e\u53f0\u4efb\u52a1',
            },
        ),
    ]
