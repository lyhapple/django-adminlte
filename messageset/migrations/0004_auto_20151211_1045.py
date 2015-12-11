# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0003_auto_20151130_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.CharField(max_length=200, verbose_name='\u4e3b\u9898'),
        ),
        migrations.AlterField(
            model_name='sitemail',
            name='receiver',
            field=models.ForeignKey(related_name='sitemail_receiver', verbose_name='\u6536\u4ef6\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='sitemail',
            name='sender',
            field=models.ForeignKey(related_name='sitemail_sender', verbose_name='\u53d1\u4ef6\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='sitemail',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb'), (2, '\u8349\u7a3f'), (3, '\u56de\u6536\u7ad9'), (99, '\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='sitemail',
            name='title',
            field=models.CharField(max_length=200, verbose_name='\u4e3b\u9898'),
        ),
    ]
