# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0002_auto_20151130_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='send_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u9001\u65f6\u95f4', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u5f00\u59cb\u65f6\u95f4', null=True),
        ),
    ]
