# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-22 19:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='timesamp',
            new_name='timestamp',
        ),
    ]
