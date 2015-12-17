# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0023_auto_20151217_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='receiver',
            new_name='receive',
        ),
        migrations.RenameField(
            model_name='sitemailreceive',
            old_name='receiver',
            new_name='receive',
        ),
        migrations.RenameField(
            model_name='sitemailsend',
            old_name='receiver',
            new_name='receive',
        ),
    ]
