# Generated by Django 3.0.5 on 2021-02-03 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210203_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/profiles')),
                ('description', models.CharField(max_length=255)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Profile', verbose_name='Профиль')),
            ],
        ),
    ]