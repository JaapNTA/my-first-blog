# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170107_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='media/img'),
        ),
    ]
