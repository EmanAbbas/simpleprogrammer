# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20170425_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='video_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
