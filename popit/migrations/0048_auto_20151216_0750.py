# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popit', '0047_auto_20151208_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persontranslation',
            name='summary',
            field=models.TextField(blank=True, verbose_name='summary'),
        ),
    ]