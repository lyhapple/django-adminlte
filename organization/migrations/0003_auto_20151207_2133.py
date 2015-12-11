# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20151205_1447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': '\u516c\u53f8', 'verbose_name_plural': '\u516c\u53f8'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': '\u90e8\u95e8', 'verbose_name_plural': '\u90e8\u95e8'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': '\u5458\u5de5', 'verbose_name_plural': '\u5458\u5de5'},
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, '\u804c\u5de5'), (1, '\u7ecf\u7406'), (2, '\u526f\u603b\u88c1'), (3, '\u603b\u88c1')], max_length=100, blank=True, null=True, verbose_name='\u804c\u52a1'),
        ),
    ]
