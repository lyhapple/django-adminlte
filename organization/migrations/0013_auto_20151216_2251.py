# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0012_auto_20151216_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='company',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='company',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='department',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='department',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='department',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='company',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='company',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='company',
            name='date_removed',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='department',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='department',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='department',
            name='date_removed',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='staff',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='staff',
            name='date_removed',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
