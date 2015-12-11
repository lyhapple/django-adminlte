# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0005_auto_20151208_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='menu',
        ),
        migrations.AddField(
            model_name='permission',
            name='menu',
            field=models.ManyToManyField(to='adminlte.Menu', null=True, verbose_name='\u83dc\u5355', blank=True),
        ),
        migrations.RemoveField(
            model_name='permission',
            name='resource',
        ),
        migrations.AddField(
            model_name='permission',
            name='resource',
            field=models.ManyToManyField(to='adminlte.Resource', null=True, verbose_name='\u8d44\u6e90', blank=True),
        ),
    ]
