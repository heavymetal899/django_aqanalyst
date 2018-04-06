# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 00:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scorecarddb', '0020_auto_20171111_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorecard',
            name='reason',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='scorecarddb.ReasonNoSale'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='referral',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorecarddb.ReferralSource'),
        ),
    ]