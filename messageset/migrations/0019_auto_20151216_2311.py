# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0018_auto_20151216_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='date_removed',
        ),
        migrations.RemoveField(
            model_name='notificationcontent',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='notificationcontent',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='notificationcontent',
            name='date_removed',
        ),
        migrations.RemoveField(
            model_name='sitemail',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='sitemail',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='sitemail',
            name='date_removed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_removed',
        ),
        migrations.AddField(
            model_name='notification',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AddField(
            model_name='notification',
            name='deleted_at',
            field=models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4', null=True),
        ),
        migrations.AddField(
            model_name='notificationcontent',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AddField(
            model_name='notificationcontent',
            name='deleted_at',
            field=models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='notificationcontent',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4', null=True),
        ),
        migrations.AddField(
            model_name='sitemail',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AddField(
            model_name='sitemail',
            name='deleted_at',
            field=models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='sitemail',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4', null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AddField(
            model_name='task',
            name='deleted_at',
            field=models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4', null=True),
        ),
    ]
