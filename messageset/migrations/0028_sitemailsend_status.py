# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0027_auto_20151217_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitemailsend',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb'), (2, '\u8349\u7a3f'), (3, '\u56de\u6536\u7ad9'), (99, '\u5220\u9664')]),
        ),
    ]
