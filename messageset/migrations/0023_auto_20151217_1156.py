# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adminlte.constants
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messageset', '0022_auto_20151217_1044'),
    ]

    operations = [
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
                ('receivers', models.ManyToManyField(help_text='\u4e0d\u9009\u5219\u53d1\u9001\u7ed9\u5168\u4f53\u7528\u6237', related_name='+', verbose_name='\u63a5\u6536\u4eba', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'verbose_name': '\u7ad9\u5185\u90ae\u4ef6\u5185\u5bb9',
                'verbose_name_plural': '\u7ad9\u5185\u90ae\u4ef6\u5185\u5bb9',
            },
            bases=(models.Model, adminlte.constants.UsableStatus),
        ),
        migrations.CreateModel(
            name='SiteMailReceive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u4e3b\u9898')),
                ('status', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb'), (2, '\u8349\u7a3f'), (3, '\u56de\u6536\u7ad9'), (99, '\u5220\u9664')])),
                ('read_time', models.DateTimeField(null=True, verbose_name='\u8bfb\u53d6\u65f6\u95f4', blank=True)),
                ('content', models.ForeignKey(verbose_name='\u5185\u5bb9', to='messageset.SiteMailContent')),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('receiver', models.ForeignKey(related_name='+', verbose_name='\u6536\u4ef6\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('sender', models.ForeignKey(related_name='+', verbose_name='\u53d1\u4ef6\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u6536\u4ef6\u7bb1',
                'verbose_name_plural': '\u6536\u4ef6\u7bb1',
            },
            bases=(models.Model, adminlte.constants.MailStatus),
        ),
        migrations.CreateModel(
            name='SiteMailSend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u4e3b\u9898')),
                ('status', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb'), (2, '\u8349\u7a3f'), (3, '\u56de\u6536\u7ad9'), (99, '\u5220\u9664')])),
                ('content', models.ForeignKey(verbose_name='\u5185\u5bb9', to='messageset.SiteMailContent')),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('receiver', models.ForeignKey(related_name='+', verbose_name='\u6536\u4ef6\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('sender', models.ForeignKey(related_name='+', verbose_name='\u53d1\u4ef6\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u53d1\u4ef6\u7bb1',
                'verbose_name_plural': '\u53d1\u4ef6\u7bb1',
            },
            bases=(models.Model, adminlte.constants.MailStatus),
        ),
        migrations.RemoveField(
            model_name='sitemail',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='sitemail',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='sitemail',
            name='sender',
        ),
        migrations.AlterField(
            model_name='notificationcontent',
            name='receivers',
            field=models.ManyToManyField(help_text='\u4e0d\u9009\u5219\u53d1\u9001\u7ed9\u5168\u4f53\u7528\u6237', related_name='+', verbose_name='\u63a5\u6536\u4eba', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.DeleteModel(
            name='SiteMail',
        ),
    ]
