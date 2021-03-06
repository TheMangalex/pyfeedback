# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0029_auto_20161227_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barcodeallowedstate',
            options={'verbose_name': 'Erlaubter Zustand', 'verbose_name_plural': 'Erlaubte Zustaende'},
        ),
        migrations.AlterField(
            model_name='barcodeallowedstate',
            name='allow_state',
            field=models.IntegerField(choices=[(100, 'Angelegt'), (600, 'Gedruckt'), (700, 'Versandt'), (800, 'B\xf6gen eingegangen'), (900, 'B\xf6gen gescannt'), (1000, 'Ergebnisse versandt')], null=True),
        ),
        migrations.AlterUniqueTogether(
            name='barcodeallowedstate',
            unique_together=set([('barcode_scanner', 'allow_state')]),
        ),
    ]
