# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4', null=True)),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('name', models.CharField(unique=True, max_length=200, verbose_name='\u516c\u53f8\u540d\u79f0')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='company_children', verbose_name='\u4e0a\u7ea7\u516c\u53f8', blank=True, to='organization.Company', null=True)),
            ],
            options={
                'verbose_name': '\u516c\u53f8\u7ba1\u7406',
                'verbose_name_plural': '\u516c\u53f8\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4', null=True)),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='\u90e8\u95e8\u540d\u79f0')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='department_children', verbose_name='\u4e0a\u7ea7\u90e8\u95e8', blank=True, to='organization.Department', null=True)),
            ],
            options={
                'verbose_name': '\u90e8\u95e8\u7ba1\u7406',
                'verbose_name_plural': '\u90e8\u95e8\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4', null=True)),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('sex', models.CharField(max_length=10, verbose_name='\u6027\u522b', choices=[(b'male', '\u7537'), (b'female', '\u5973')])),
                ('cellphone', models.CharField(max_length=11, verbose_name='\u624b\u673a')),
                ('birthday', models.DateField(null=True, verbose_name='\u751f\u65e5', blank=True)),
                ('qq', models.CharField(max_length=20, null=True, verbose_name='QQ', blank=True)),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='\u90ae\u7bb1', blank=True)),
                ('location', models.CharField(max_length=200, null=True, verbose_name='\u5730\u5740', blank=True)),
                ('avatar', models.ImageField(upload_to=b'tmp', null=True, verbose_name='\u5934\u50cf', blank=True)),
                ('status', models.IntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(1, '\u5728\u804c'), (2, '\u79bb\u804c')])),
                ('position', models.CharField(max_length=100, null=True, verbose_name='\u804c\u52a1', blank=True)),
                ('company', models.ForeignKey(verbose_name='\u6240\u5728\u516c\u53f8', to='organization.Company')),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('department', models.ForeignKey(verbose_name='\u6240\u5728\u90e8\u95e8', to='organization.Department')),
                ('user', models.OneToOneField(related_name='staff_user', verbose_name='\u767b\u5f55\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u5458\u5de5\u7ba1\u7406',
                'verbose_name_plural': '\u5458\u5de5\u7ba1\u7406',
            },
        ),
    ]
