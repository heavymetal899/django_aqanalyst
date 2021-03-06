# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorecarddb', '0002_locations'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReasonsNoSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_name', models.CharField(choices=[('pi', 'Price Issue'), ('mr', 'Medical Referral'), ('to', 'Thinking It Over'), ('3p', '3rd Party Not Present'), ('so', 'Getting a Second Opinion'), ('dh', 'Denial of Hearing Loss'), ('ad', 'Annual DE'), ('cu', 'Current User Not Ready to Upgrade'), ('tr', 'Time Restraint'), ('va', 'VA Eligible'), ('vc', 'Vanity Concern')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ReferralSources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_source', models.CharField(choices=[('dm', 'Direct Mail'), ('in', 'Internet'), ('em', 'Event Marketing'), ('np', 'Newspaper'), ('na', 'Non-Advertising'), ('re', 'Referral'), ('tv', 'TV'), ('ra', 'Radio'), ('sp', 'SHARE Program'), ('wi', 'Walk-In')], max_length=2)),
            ],
        ),
    ]
