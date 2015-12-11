# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0003_auto_20151207_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemconfig',
            name='title',
            field=models.CharField(help_text=b'\xe5\xb8\xae\xe5\x8a\xa9', max_length=255, verbose_name='\u914d\u7f6e\u540d\u79f0(\u4e2d\u6587)'),
        ),
    ]
