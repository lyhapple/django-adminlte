# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_auto_20151208_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='avatar',
            field=models.ImageField(default=None, upload_to=b'adminlte/user_avatar', null=True, verbose_name='\u76f8\u7247', blank=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(related_name='staff_of', null=True, default=None, to=settings.AUTH_USER_MODEL, blank=True, verbose_name='\u7cfb\u7edf\u8d26\u53f7'),
        ),
    ]
