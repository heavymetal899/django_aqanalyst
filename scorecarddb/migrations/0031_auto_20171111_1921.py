# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorecarddb', '0030_auto_20171111_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorecard',
            name='open_state_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, help_text='3) Direct Questions, Anatomy, Test, Recommendation, Seeks Acknowledgement', verbose_name='Opening Statement'),
        ),
    ]
