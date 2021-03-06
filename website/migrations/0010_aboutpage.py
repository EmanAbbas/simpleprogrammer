# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20170430_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_text', models.TextField(max_length=1000)),
                ('about_image', stdimage.models.StdImageField(upload_to='uploads/images')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
