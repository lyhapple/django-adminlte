# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0006_auto_20151208_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='menu',
            field=models.ManyToManyField(to='adminlte.Menu', verbose_name='\u83dc\u5355', blank=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='resource',
            field=models.ManyToManyField(to='adminlte.Resource', verbose_name='\u8d44\u6e90', blank=True),
        ),
    ]
