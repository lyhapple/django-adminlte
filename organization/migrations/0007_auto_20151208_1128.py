# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0006_auto_20151207_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='name',
            new_name='real_name',
        ),
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(related_name='staff_user', null=True, default=None, to=settings.AUTH_USER_MODEL, blank=True, verbose_name='\u7cfb\u7edf\u8d26\u53f7'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='avatar',
            field=models.ImageField(upload_to=b'adminlte/user_avatar', null=True, verbose_name='\u76f8\u7247'),
        ),
    ]
