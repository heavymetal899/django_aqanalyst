# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 00:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scorecarddb', '0021_auto_20171111_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorecard',
            name='referral',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorecarddb.ReferralSource'),
        ),
    ]
