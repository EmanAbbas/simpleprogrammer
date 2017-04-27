# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20170425_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='video',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_clip',
        ),
        migrations.AddField(
            model_name='article',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='video_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/thumbnails'),
        ),
        migrations.AddField(
            model_name='video',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
