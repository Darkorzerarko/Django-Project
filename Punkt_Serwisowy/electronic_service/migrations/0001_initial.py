# Generated by Django 4.0.4 on 2022-06-01 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('login', models.CharField(default='', max_length=64, unique=True)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('password', models.CharField(default='', max_length=128)),
                ('firm_name', models.CharField(blank=True, max_length=64)),
                ('firm_NIP_REGON', models.CharField(blank=True, max_length=10)),
                ('ZIP_code', models.CharField(max_length=7)),
                ('city', models.CharField(max_length=32)),
                ('street_number', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=23, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('ZIP_code', models.CharField(max_length=7)),
                ('city', models.CharField(max_length=32)),
                ('street_number', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=23, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=32)),
                ('model', models.CharField(max_length=32)),
                ('serial_number', models.CharField(max_length=64)),
                ('client_description', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='repair_part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=32)),
                ('producer_num', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('hourly_wage', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='service_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_request', models.DateTimeField(verbose_name='Date of service request')),
                ('date_of_completion', models.DateTimeField(blank=True, verbose_name='Date of service request completed')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic_service.client')),
            ],
        ),
        migrations.CreateModel(
            name='hardware_fault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professional_description', models.CharField(max_length=512)),
                ('repair_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('employee_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='electronic_service.employee')),
                ('hardware_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic_service.hardware')),
                ('repair_part_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='electronic_service.repair_part')),
            ],
        ),
        migrations.AddField(
            model_name='hardware',
            name='request_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic_service.service_request'),
        ),
        migrations.CreateModel(
            name='employee_specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic_service.employee')),
                ('specialization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic_service.specialization')),
            ],
        ),
    ]