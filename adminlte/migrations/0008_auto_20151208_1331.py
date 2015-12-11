# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0007_auto_20151208_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permission',
            old_name='menu',
            new_name='menus',
        ),
        migrations.RenameField(
            model_name='permission',
            old_name='resource',
            new_name='resources',
        ),
    ]
