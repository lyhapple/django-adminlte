# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0016_auto_20151216_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb'), (99, '\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='notificationcontent',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='notificationcontent',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='sitemail',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='sitemail',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb'), (2, '\u8349\u7a3f'), (3, '\u56de\u6536\u7ad9'), (99, '\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='deleted',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u5df2\u8f6f\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38(\u8fdb\u884c\u4e2d)'), (1, '\u5f02\u5e38'), (2, '\u5b8c\u6210'), (99, '\u5220\u9664')]),
        ),
    ]
