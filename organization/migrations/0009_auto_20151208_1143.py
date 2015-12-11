# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0008_auto_20151208_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='login_name',
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(related_name='staff_of', verbose_name='\u767b\u5f55\u8d26\u53f7', to=settings.AUTH_USER_MODEL),
        ),
    ]
