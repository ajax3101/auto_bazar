# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('price', models.ImageField(upload_to='', verbose_name='цена')),
                ('description', models.TextField(verbose_name='описание')),
            ],
        ),
    ]
