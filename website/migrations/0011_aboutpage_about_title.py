# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_aboutpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='about_title',
            field=models.CharField(default='About us', max_length=200),
        ),
    ]
