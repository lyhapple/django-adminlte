# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0008_auto_20151208_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemconfig',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name='\u7236\u914d\u7f6e\u9879', blank=True, to='adminlte.SystemConfig', null=True),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='tree_id',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='app_name',
            field=models.CharField(max_length=200, null=True, verbose_name='\u6240\u5c5e\u5e94\u7528', blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='model_name',
            field=models.CharField(max_length=200, null=True, verbose_name='\u6240\u5c5e\u6a21\u578b', blank=True),
        ),
    ]
