# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import adminlte.constants


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messageset', '0005_notification_receiver'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4', null=True)),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u4e3b\u9898')),
                ('contents', models.TextField(verbose_name='\u5185\u5bb9')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u9001\u65f6\u95f4', null=True)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, adminlte.constants.ReadStatus),
        ),
        migrations.RemoveField(
            model_name='notification',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='send_time',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='title',
        ),
        migrations.AddField(
            model_name='notification',
            name='content',
            field=models.ForeignKey(verbose_name='\u5185\u5bb9', blank=True, to='messageset.NotificationContent', null=True),
        ),
    ]
