# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-01 21:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pttrack', '0007_auto_20181201_1447'),
        ('followup', '0002_simplehistory_add_change_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalfollowup',
            name='completion_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followup_generalfollowup_completed', to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='generalfollowup',
            name='completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generalfollowup',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 1, 21, 25, 37, 963506, tzinfo=utc), help_text=b'MM/DD/YYYY or YYYY-MM-DD'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalgeneralfollowup',
            name='completion_author',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='historicalgeneralfollowup',
            name='completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalgeneralfollowup',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 1, 21, 25, 47, 259016, tzinfo=utc), help_text=b'MM/DD/YYYY or YYYY-MM-DD'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='completion_author',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 1, 21, 25, 55, 194958, tzinfo=utc), help_text=b'MM/DD/YYYY or YYYY-MM-DD'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='completion_author',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 1, 21, 26, 3, 90703, tzinfo=utc), help_text=b'MM/DD/YYYY or YYYY-MM-DD'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='completion_author',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 1, 21, 26, 8, 562464, tzinfo=utc), help_text=b'MM/DD/YYYY or YYYY-MM-DD'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='completion_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followup_labfollowup_completed', to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 1, 21, 26, 12, 18409, tzinfo=utc), help_text=b'MM/DD/YYYY or YYYY-MM-DD'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='referralfollowup',
            name='completion_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followup_referralfollowup_completed', to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='referralfollowup',
            name='completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='referralfollowup',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 1, 21, 26, 20, 586113, tzinfo=utc), help_text=b'MM/DD/YYYY or YYYY-MM-DD'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaccinefollowup',
            name='completion_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followup_vaccinefollowup_completed', to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='vaccinefollowup',
            name='completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vaccinefollowup',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 1, 21, 26, 24, 666085, tzinfo=utc), help_text=b'MM/DD/YYYY or YYYY-MM-DD'),
            preserve_default=False,
        ),
    ]