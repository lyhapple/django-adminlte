# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0016_auto_20151217_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='date_removed',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='date_removed',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='date_removed',
        ),
        migrations.RemoveField(
            model_name='systemconfig',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='systemconfig',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='systemconfig',
            name='date_removed',
        ),
        migrations.AddField(
            model_name='menu',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 10, 42, 28, 157783), verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='menu',
            name='deleted_at',
            field=models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 10, 42, 28, 157825), verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='permission',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 10, 42, 28, 157783), verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='permission',
            name='deleted_at',
            field=models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='permission',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 10, 42, 28, 157825), verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='resource',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 10, 42, 28, 157783), verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='resource',
            name='deleted_at',
            field=models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 10, 42, 28, 157825), verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 10, 42, 28, 157783), verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='deleted_at',
            field=models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 10, 42, 28, 157825), verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4'),
        ),
    ]
