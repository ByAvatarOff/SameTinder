# Generated by Django 3.0.5 on 2021-02-06 15:24

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_profile_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='geo_location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]