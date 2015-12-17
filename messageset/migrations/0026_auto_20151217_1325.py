# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0025_auto_20151217_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitemailreceive',
            name='send_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u9001\u65f6\u95f4', null=True),
        ),
        migrations.AddField(
            model_name='sitemailsend',
            name='send_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u9001\u65f6\u95f4', null=True),
        ),
    ]
