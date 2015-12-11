# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0009_auto_20151208_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.PositiveSmallIntegerField(default=0, null=True, verbose_name='\u804c\u4f4d', blank=True, choices=[(0, '\u804c\u5de5'), (1, '\u7ecf\u7406'), (2, '\u526f\u603b\u88c1'), (3, '\u603b\u88c1')]),
        ),
        migrations.AlterField(
            model_name='staff',
            name='real_name',
            field=models.CharField(max_length=20, verbose_name='\u771f\u5b9e\u59d3\u540d'),
        ),
    ]
