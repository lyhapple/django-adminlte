# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemconfig',
            options={'verbose_name': '\u53c2\u6570\u914d\u7f6e', 'verbose_name_plural': '\u53c2\u6570\u914d\u7f6e'},
        ),
        migrations.AlterField(
            model_name='systemconfig',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='\u952e'),
        ),
        migrations.AlterField(
            model_name='systemconfig',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='systemconfig',
            name='value',
            field=models.CharField(max_length=255, verbose_name='\u503c'),
        ),
    ]
