# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170107_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='img'),
        ),
    ]
