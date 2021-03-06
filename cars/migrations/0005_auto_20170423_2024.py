# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20170423_1928'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['name'], 'verbose_name': 'машина', 'verbose_name_plural': 'машины'},
        ),
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='cars/photo', verbose_name='фотография'),
        ),
    ]
