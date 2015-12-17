# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0011_auto_20151216_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='department',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
    ]
