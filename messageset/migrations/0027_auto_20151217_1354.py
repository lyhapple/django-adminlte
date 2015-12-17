# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0026_auto_20151217_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitemailsend',
            name='receive',
        ),
        migrations.RemoveField(
            model_name='sitemailsend',
            name='status',
        ),
    ]
