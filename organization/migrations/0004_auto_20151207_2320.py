# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20151207_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='user',
        ),
        migrations.AddField(
            model_name='staff',
            name='login_name',
            field=models.CharField(default=b'', help_text='\u521d\u59cb\u9ed8\u8ba4\u5bc6\u7801\u4e3a:123456', max_length=20, verbose_name='\u767b\u5f55\u7528\u6237\u540d'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.PositiveSmallIntegerField(default=0, null=True, verbose_name='\u804c\u52a1', blank=True, choices=[(0, '\u804c\u5de5'), (1, '\u7ecf\u7406'), (2, '\u526f\u603b\u88c1'), (3, '\u603b\u88c1')]),
        ),
    ]
