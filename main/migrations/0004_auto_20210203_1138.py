# Generated by Django 3.0.5 on 2021-02-03 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210203_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='nickname',
            new_name='user',
        ),
    ]
