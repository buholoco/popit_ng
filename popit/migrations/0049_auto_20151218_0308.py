# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popit', '0048_auto_20151216_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttranslation',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='role'),
        ),
    ]