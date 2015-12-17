# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0024_auto_20151217_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationcontent',
            name='receivers',
            field=models.ManyToManyField(help_text='\u4e0d\u9009\u5219\u53d1\u9001\u7ed9\u5168\u4f53\u7528\u6237', related_name='notification_receivers', verbose_name='\u63a5\u6536\u4eba', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='sitemailcontent',
            name='receivers',
            field=models.ManyToManyField(help_text='\u4e0d\u9009\u5219\u53d1\u9001\u7ed9\u5168\u4f53\u7528\u6237', related_name='sitemail_receivers', verbose_name='\u63a5\u6536\u4eba', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
