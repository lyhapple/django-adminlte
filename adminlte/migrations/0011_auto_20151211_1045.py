# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0010_auto_20151209_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='group',
            field=models.ForeignKey(related_name='group_permission', verbose_name='\u89d2\u8272', to='adminlte.LteGroup'),
        ),
    ]
