# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0013_notification_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationcontent',
            name='send_time',
        ),
        migrations.AddField(
            model_name='notification',
            name='send_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u9001\u65f6\u95f4', null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='title',
            field=models.CharField(default=b'', max_length=200, null=True, verbose_name='\u6807\u9898', blank=True),
        ),
        migrations.AlterField(
            model_name='notificationcontent',
            name='title',
            field=models.CharField(max_length=200, verbose_name='\u6807\u9898'),
        ),
    ]
