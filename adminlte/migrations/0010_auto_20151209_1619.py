# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0009_auto_20151209_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemconfig',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='\u914d\u7f6e\u540d\u79f0(\u82f1\u6587)'),
        ),
        migrations.AlterField(
            model_name='systemconfig',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u914d\u7f6e\u540d\u79f0(\u4e2d\u6587)'),
        ),
    ]
