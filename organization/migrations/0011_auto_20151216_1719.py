# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0010_auto_20151208_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AddField(
            model_name='company',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')]),
        ),
        migrations.AddField(
            model_name='department',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AddField(
            model_name='department',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')]),
        ),
        migrations.AddField(
            model_name='staff',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AddField(
            model_name='staff',
            name='job_status',
            field=models.IntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(1, '\u5728\u804c'), (2, '\u79bb\u804c')]),
        ),
        migrations.AlterField(
            model_name='staff',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='\u6570\u636e\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')]),
        ),
    ]
