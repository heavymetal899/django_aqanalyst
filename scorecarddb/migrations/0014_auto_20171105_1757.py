# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorecarddb', '0013_auto_20171105_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorecard',
            name='open_state_comment',
            field=models.TextField(blank=True),
        ),
    ]