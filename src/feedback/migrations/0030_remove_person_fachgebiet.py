# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 12:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0029_auto_20161227_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='fachgebiet',
        ),
    ]
