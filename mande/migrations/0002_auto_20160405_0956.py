# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-05 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mande', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_hours',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='job_req',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
