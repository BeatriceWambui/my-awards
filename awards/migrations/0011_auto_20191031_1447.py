# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-31 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0010_auto_20191025_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletterrecipients',
            name='name',
            field=models.CharField(default='hello', max_length=30),
        ),
    ]