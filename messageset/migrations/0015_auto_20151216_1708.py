# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0014_auto_20151216_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationcontent',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb'), (99, '\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38(\u8fdb\u884c\u4e2d)'), (1, '\u5f02\u5e38'), (2, '\u5b8c\u6210'), (99, '\u5220\u9664')]),
        ),
    ]
