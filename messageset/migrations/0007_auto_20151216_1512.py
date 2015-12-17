# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messageset', '0006_auto_20151216_1505'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notificationcontent',
            options={'verbose_name': '\u7cfb\u7edf\u901a\u77e5\u5185\u5bb9', 'verbose_name_plural': '\u7cfb\u7edf\u901a\u77e5\u5185\u5bb9'},
        ),
        migrations.RemoveField(
            model_name='notification',
            name='receiver',
        ),
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ManyToManyField(related_name='receivers', null=True, verbose_name='\u63a5\u6536\u4eba', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
