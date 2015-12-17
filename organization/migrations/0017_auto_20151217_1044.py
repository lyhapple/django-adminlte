# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0016_auto_20151217_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='company',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='department',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4'),
        ),
    ]
