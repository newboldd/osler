# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-01 20:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='followuprequest',
            options={'ordering': ['-written_datetime', '-last_modified']},
        ),
        migrations.AlterModelOptions(
            name='patientcontact',
            options={'ordering': ['-written_datetime', '-last_modified']},
        ),
        migrations.AlterModelOptions(
            name='referral',
            options={'ordering': ['-written_datetime', '-last_modified']},
        ),
    ]