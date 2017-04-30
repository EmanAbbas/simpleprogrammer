# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='uploads/videos'),
        ),
        migrations.AddField(
            model_name='resource',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='uploads/images'),
        ),
    ]