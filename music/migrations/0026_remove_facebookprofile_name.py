# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-24 12:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0025_auto_20161223_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebookprofile',
            name='name',
        ),
    ]
