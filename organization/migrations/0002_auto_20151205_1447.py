# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='company',
        ),
        migrations.AddField(
            model_name='department',
            name='company',
            field=models.ForeignKey(related_name='departments', default=None, blank=True, to='organization.Company', null=True, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x85\xac\xe5\x8f\xb8'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(related_name='staff_users', verbose_name='\u767b\u5f55\u7528\u6237', to=settings.AUTH_USER_MODEL),
        ),
    ]
