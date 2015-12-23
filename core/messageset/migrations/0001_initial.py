# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import core.adminlte.constants


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('title', models.CharField(default=b'', max_length=200, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('status', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb'), (99, '\u5220\u9664')])),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u9001\u65f6\u95f4', null=True)),
                ('read_time', models.DateTimeField(null=True, verbose_name='\u8bfb\u53d6\u65f6\u95f4', blank=True)),
            ],
            options={
                'verbose_name': '\u7cfb\u7edf\u901a\u77e5',
                'verbose_name_plural': '\u7cfb\u7edf\u901a\u77e5',
            },
            bases=(models.Model, core.adminlte.constants.ReadStatus),
        ),
        migrations.CreateModel(
            name='NotificationContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898')),
                ('contents', models.TextField(verbose_name='\u5185\u5bb9')),
                ('status', models.PositiveSmallIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')])),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('receivers', models.ManyToManyField(help_text='\u4e0d\u9009\u5219\u53d1\u9001\u7ed9\u5168\u4f53\u7528\u6237', related_name='notification_receivers', verbose_name='\u63a5\u6536\u4eba', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'verbose_name': '\u7cfb\u7edf\u901a\u77e5\u5185\u5bb9',
                'verbose_name_plural': '\u7cfb\u7edf\u901a\u77e5\u5185\u5bb9',
            },
            bases=(models.Model, core.adminlte.constants.UsableStatus),
        ),
        migrations.CreateModel(
            name='SiteMailContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898')),
                ('contents', models.TextField(verbose_name='\u5185\u5bb9')),
                ('status', models.PositiveSmallIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')])),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('receivers', models.ManyToManyField(help_text='\u4e0d\u9009\u5219\u53d1\u9001\u7ed9\u5168\u4f53\u7528\u6237', related_name='sitemail_receivers', verbose_name='\u63a5\u6536\u4eba', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'verbose_name': '\u7ad9\u5185\u90ae\u4ef6\u5185\u5bb9',
                'verbose_name_plural': '\u7ad9\u5185\u90ae\u4ef6\u5185\u5bb9',
            },
            bases=(models.Model, core.adminlte.constants.UsableStatus),
        ),
        migrations.CreateModel(
            name='SiteMailReceive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u4e3b\u9898')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u9001\u65f6\u95f4', null=True)),
                ('status', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb'), (2, '\u8349\u7a3f'), (3, '\u56de\u6536\u7ad9'), (99, '\u5220\u9664')])),
                ('read_time', models.DateTimeField(null=True, verbose_name='\u8bfb\u53d6\u65f6\u95f4', blank=True)),
                ('content', models.ForeignKey(verbose_name='\u5185\u5bb9', to='messageset.SiteMailContent')),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('receive', models.ForeignKey(related_name='+', verbose_name='\u6536\u4ef6\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('sender', models.ForeignKey(related_name='+', verbose_name='\u53d1\u4ef6\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u6536\u4ef6\u7bb1',
                'verbose_name_plural': '\u6536\u4ef6\u7bb1',
            },
            bases=(models.Model, core.adminlte.constants.MailStatus),
        ),
        migrations.CreateModel(
            name='SiteMailSend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u4e3b\u9898')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u9001\u65f6\u95f4', null=True)),
                ('status', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb'), (2, '\u8349\u7a3f'), (3, '\u56de\u6536\u7ad9'), (99, '\u5220\u9664')])),
                ('content', models.ForeignKey(verbose_name='\u5185\u5bb9', to='messageset.SiteMailContent')),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('sender', models.ForeignKey(related_name='+', verbose_name='\u53d1\u4ef6\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u53d1\u4ef6\u7bb1',
                'verbose_name_plural': '\u53d1\u4ef6\u7bb1',
            },
            bases=(models.Model, core.adminlte.constants.MailStatus),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('percent', models.PositiveIntegerField(default=0, verbose_name='\u8fdb\u5ea6')),
                ('start_app', models.CharField(max_length=255, null=True, verbose_name='\u53d1\u8d77app', blank=True)),
                ('status', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38(\u8fdb\u884c\u4e2d)'), (1, '\u5f02\u5e38'), (2, '\u5b8c\u6210'), (99, '\u5220\u9664')])),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='\u5f00\u59cb\u65f6\u95f4', null=True)),
                ('end_time', models.DateTimeField(null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u540e\u53f0\u4efb\u52a1',
                'verbose_name_plural': '\u540e\u53f0\u4efb\u52a1',
            },
            bases=(models.Model, core.adminlte.constants.TaskStatus),
        ),
        migrations.AddField(
            model_name='notification',
            name='content',
            field=models.ForeignKey(verbose_name='\u5185\u5bb9', blank=True, to='messageset.NotificationContent', null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='creator',
            field=models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='receive',
            field=models.ForeignKey(related_name='+', verbose_name='\u63a5\u6536\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
