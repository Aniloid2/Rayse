# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-26 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_artist_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='times_called',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
