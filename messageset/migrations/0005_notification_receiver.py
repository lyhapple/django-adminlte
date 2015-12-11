# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messageset', '0004_auto_20151211_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(related_name='notification_receiver', verbose_name='\u63a5\u6536\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
