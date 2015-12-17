# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0012_auto_20151216_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='permission',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='resource',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='systemconfig',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='systemconfig',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')]),
        ),
    ]
