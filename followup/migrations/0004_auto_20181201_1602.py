# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-01 22:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followup', '0003_auto_20181201_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalfollowup',
            name='completion_author',
        ),
        migrations.RemoveField(
            model_name='generalfollowup',
            name='completion_date',
        ),
        migrations.RemoveField(
            model_name='generalfollowup',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='historicalgeneralfollowup',
            name='completion_author',
        ),
        migrations.RemoveField(
            model_name='historicalgeneralfollowup',
            name='completion_date',
        ),
        migrations.RemoveField(
            model_name='historicalgeneralfollowup',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='historicallabfollowup',
            name='completion_author',
        ),
        migrations.RemoveField(
            model_name='historicallabfollowup',
            name='completion_date',
        ),
        migrations.RemoveField(
            model_name='historicallabfollowup',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='historicalreferralfollowup',
            name='completion_author',
        ),
        migrations.RemoveField(
            model_name='historicalreferralfollowup',
            name='completion_date',
        ),
        migrations.RemoveField(
            model_name='historicalreferralfollowup',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='historicalvaccinefollowup',
            name='completion_author',
        ),
        migrations.RemoveField(
            model_name='historicalvaccinefollowup',
            name='completion_date',
        ),
        migrations.RemoveField(
            model_name='historicalvaccinefollowup',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='labfollowup',
            name='completion_author',
        ),
        migrations.RemoveField(
            model_name='labfollowup',
            name='completion_date',
        ),
        migrations.RemoveField(
            model_name='labfollowup',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='referralfollowup',
            name='completion_author',
        ),
        migrations.RemoveField(
            model_name='referralfollowup',
            name='completion_date',
        ),
        migrations.RemoveField(
            model_name='referralfollowup',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='vaccinefollowup',
            name='completion_author',
        ),
        migrations.RemoveField(
            model_name='vaccinefollowup',
            name='completion_date',
        ),
        migrations.RemoveField(
            model_name='vaccinefollowup',
            name='due_date',
        ),
    ]