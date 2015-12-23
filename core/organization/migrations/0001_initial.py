# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import django.utils.timezone
from django.conf import settings
import core.adminlte.constants


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('name', models.CharField(unique=True, max_length=200, verbose_name='\u516c\u53f8\u540d\u79f0')),
                ('status', models.PositiveSmallIntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')])),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='company_children', verbose_name='\u4e0a\u7ea7\u516c\u53f8', blank=True, to='organization.Company', null=True)),
            ],
            options={
                'verbose_name': '\u516c\u53f8',
                'verbose_name_plural': '\u516c\u53f8',
            },
            bases=(models.Model, core.adminlte.constants.UsableStatus),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='\u90e8\u95e8\u540d\u79f0')),
                ('status', models.PositiveSmallIntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')])),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('company', models.ForeignKey(related_name='departments', default=None, blank=True, to='organization.Company', null=True, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x85\xac\xe5\x8f\xb8')),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='department_children', verbose_name='\u4e0a\u7ea7\u90e8\u95e8', blank=True, to='organization.Department', null=True)),
            ],
            options={
                'verbose_name': '\u90e8\u95e8',
                'verbose_name_plural': '\u90e8\u95e8',
            },
            bases=(models.Model, core.adminlte.constants.UsableStatus),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('real_name', models.CharField(max_length=20, verbose_name='\u771f\u5b9e\u59d3\u540d')),
                ('sex', models.CharField(max_length=10, verbose_name='\u6027\u522b', choices=[(b'male', '\u7537'), (b'female', '\u5973')])),
                ('cellphone', models.CharField(max_length=11, verbose_name='\u624b\u673a')),
                ('birthday', models.DateField(null=True, verbose_name='\u751f\u65e5', blank=True)),
                ('qq', models.CharField(max_length=20, null=True, verbose_name='QQ', blank=True)),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='\u90ae\u7bb1', blank=True)),
                ('location', models.CharField(max_length=200, null=True, verbose_name='\u5730\u5740', blank=True)),
                ('avatar', models.ImageField(default=None, null=True, upload_to=b'adminlte/user_avatar', blank=True)),
                ('job_status', models.IntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(1, '\u5728\u804c'), (2, '\u79bb\u804c')])),
                ('status', models.PositiveSmallIntegerField(default=1, verbose_name='\u6570\u636e\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')])),
                ('position', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='\u804c\u4f4d', blank=True, choices=[(0, '\u804c\u5de5'), (1, '\u7ecf\u7406'), (2, '\u526f\u603b\u88c1'), (3, '\u603b\u88c1')])),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('department', models.ForeignKey(verbose_name='\u6240\u5728\u90e8\u95e8', to='organization.Department')),
                ('user', models.OneToOneField(related_name='staff_of', verbose_name='\u767b\u5f55\u8d26\u53f7', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u5458\u5de5',
                'verbose_name_plural': '\u5458\u5de5',
            },
            bases=(models.Model, core.adminlte.constants.UsableStatus),
        ),
    ]
