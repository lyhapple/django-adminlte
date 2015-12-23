# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import core.adminlte.constants


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='\u83dc\u5355\u540d\u79f0')),
                ('icon', models.CharField(default=b'fa-circle-o', help_text='\u53c2\u8003:http://fontawesome.io', max_length=50, verbose_name='\u83dc\u5355\u56fe\u6807')),
                ('app_name', models.CharField(max_length=200, null=True, verbose_name='App\u540d\u79f0', blank=True)),
                ('model_name', models.CharField(help_text='\u6ce8\u610f\u5927\u5c0f\u5199', max_length=200, null=True, verbose_name='Model\u540d\u79f0', blank=True)),
                ('url', models.CharField(help_text='\u9009\u586b', max_length=200, null=True, verbose_name='\u5168\u8def\u5f84', blank=True)),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('status', models.PositiveSmallIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')])),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': '\u83dc\u5355',
                'verbose_name_plural': '\u83dc\u5355',
            },
            bases=(models.Model, core.adminlte.constants.UsableStatus),
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('status', models.PositiveSmallIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')])),
            ],
            options={
                'verbose_name': '\u6743\u9650',
                'verbose_name_plural': '\u6743\u9650',
            },
            bases=(models.Model, core.adminlte.constants.UsableStatus),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u8d44\u6e90\u540d\u79f0')),
                ('app_name', models.CharField(max_length=200, null=True, verbose_name='\u6240\u5c5e\u5e94\u7528', blank=True)),
                ('model_name', models.CharField(max_length=200, null=True, verbose_name='\u6240\u5c5e\u6a21\u578b', blank=True)),
                ('url', models.CharField(help_text='API\u5730\u5740', max_length=500, null=True, verbose_name='\u8d44\u6e90\u5730\u5740', blank=True)),
                ('note', models.CharField(max_length=500, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('status', models.PositiveSmallIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')])),
            ],
            options={
                'verbose_name': 'API\u8d44\u6e90',
                'verbose_name_plural': 'API\u8d44\u6e90',
            },
            bases=(models.Model, core.adminlte.constants.UsableStatus),
        ),
        migrations.CreateModel(
            name='SystemConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='\u914d\u7f6e\u540d\u79f0(\u82f1\u6587)')),
                ('title', models.CharField(max_length=255, verbose_name='\u914d\u7f6e\u540d\u79f0(\u4e2d\u6587)')),
                ('value', models.CharField(max_length=255, verbose_name='\u914d\u7f6e\u503c')),
                ('status', models.PositiveSmallIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')])),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'verbose_name': '\u7cfb\u7edf\u914d\u7f6e',
                'verbose_name_plural': '\u7cfb\u7edf\u914d\u7f6e',
            },
            bases=(models.Model, core.adminlte.constants.UsableStatus),
        ),
        migrations.CreateModel(
            name='LteGroup',
            fields=[
            ],
            options={
                'verbose_name': '\u89d2\u8272',
                'proxy': True,
                'verbose_name_plural': '\u89d2\u8272',
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='LteUser',
            fields=[
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'proxy': True,
                'verbose_name_plural': '\u7528\u6237',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='creator',
            field=models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name='\u7236\u914d\u7f6e\u9879', blank=True, to='adminlte.SystemConfig', null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='creator',
            field=models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='permission',
            name='creator',
            field=models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='permission',
            name='group',
            field=models.ForeignKey(related_name='group_permission', verbose_name='\u89d2\u8272', to='adminlte.LteGroup'),
        ),
        migrations.AddField(
            model_name='permission',
            name='menus',
            field=models.ManyToManyField(to='adminlte.Menu', verbose_name='\u83dc\u5355', blank=True),
        ),
        migrations.AddField(
            model_name='permission',
            name='resources',
            field=models.ManyToManyField(to='adminlte.Resource', verbose_name='\u8d44\u6e90', blank=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='creator',
            field=models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name='\u4e0a\u7ea7\u83dc\u5355', blank=True, to='adminlte.Menu', null=True),
        ),
    ]
