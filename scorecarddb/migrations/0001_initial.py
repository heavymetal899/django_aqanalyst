# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Practitioner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practitioner_first_name', models.CharField(max_length=30)),
                ('practitioner_last_name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['practitioner_last_name'],
            },
        ),
    ]
