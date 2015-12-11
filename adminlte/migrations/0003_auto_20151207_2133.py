# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '\u7528\u6237\u8d44\u6599', 'verbose_name_plural': '\u7528\u6237\u8d44\u6599'},
        ),
    ]
