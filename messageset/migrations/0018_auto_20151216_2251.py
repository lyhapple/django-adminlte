# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0017_auto_20151216_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='notificationcontent',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='notificationcontent',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='notificationcontent',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='sitemail',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='sitemail',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='sitemail',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='task',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='task',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='task',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='notification',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='notification',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='notification',
            name='date_removed',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='notificationcontent',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='notificationcontent',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='notificationcontent',
            name='date_removed',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sitemail',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='sitemail',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='sitemail',
            name='date_removed',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='date_removed',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
