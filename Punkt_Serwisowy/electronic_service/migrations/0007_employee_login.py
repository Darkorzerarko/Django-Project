# Generated by Django 4.0.4 on 2022-06-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic_service', '0006_alter_service_request_date_of_completion'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='login',
            field=models.CharField(default='', max_length=64, unique=True),
        ),
    ]
