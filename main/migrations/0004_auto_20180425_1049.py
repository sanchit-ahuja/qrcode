# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180420_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='profshow',
        ),
        migrations.AddField(
            model_name='tickets',
            name='profshow',
            field=models.ManyToManyField(to='main.Profshow'),
        ),
    ]
