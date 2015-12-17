# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0011_auto_20151211_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AddField(
            model_name='permission',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AddField(
            model_name='permission',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')]),
        ),
        migrations.AddField(
            model_name='resource',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AddField(
            model_name='resource',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')]),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')]),
        ),
    ]
