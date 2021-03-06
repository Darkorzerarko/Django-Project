# Generated by Django 4.0.4 on 2022-06-03 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ZIP_code',
            field=models.CharField(blank=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=23, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='street_number',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
