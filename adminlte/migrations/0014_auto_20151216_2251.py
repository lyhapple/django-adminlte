# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0013_auto_20151216_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='systemconfig',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='systemconfig',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='systemconfig',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='menu',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='menu',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='menu',
            name='date_removed',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='permission',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='permission',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='permission',
            name='date_removed',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='resource',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='resource',
            name='date_removed',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='date_removed',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
