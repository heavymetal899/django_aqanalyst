# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorecarddb', '0032_auto_20171111_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorecard',
            name='sale_made',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=3),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='third_party',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=3),
        ),
    ]