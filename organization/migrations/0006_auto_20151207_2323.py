# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20151207_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='login_name',
            field=models.CharField(help_text='\u521d\u59cb\u9ed8\u8ba4\u5bc6\u7801\u4e3a:123456', unique=True, max_length=20, verbose_name='\u767b\u5f55\u7528\u6237\u540d'),
        ),
    ]
