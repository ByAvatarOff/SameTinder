# Generated by Django 3.0.5 on 2021-02-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_addcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='group',
            field=models.CharField(choices=[('Base', 'base'), ('Premium', 'premium'), ('VIP', 'vip')], default='base', max_length=100, null=True),
        ),
    ]
