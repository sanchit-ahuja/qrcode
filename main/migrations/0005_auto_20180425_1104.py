# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180425_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='qrcode',
        ),
        migrations.AddField(
            model_name='student',
            name='qrcode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]