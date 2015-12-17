# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0008_auto_20151216_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationcontent',
            name='receivers',
            field=models.ManyToManyField(related_name='receivers', verbose_name='\u63a5\u6536\u4eba', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
