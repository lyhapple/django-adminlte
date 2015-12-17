# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0012_auto_20151216_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='content',
            field=models.ForeignKey(verbose_name='\u5185\u5bb9', blank=True, to='messageset.NotificationContent', null=True),
        ),
    ]
