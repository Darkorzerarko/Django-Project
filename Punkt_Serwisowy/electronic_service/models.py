import datetime

from django.urls import reverse
from django.db import models
from django.utils import timezone


class employee(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    login = models.CharField(max_length=64, unique=True, default="")
    ZIP_code = models.CharField(max_length=7)
    city = models.CharField(max_length=32)
    street_number = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=23, unique=True)

    def __str__(self):
        return str(
            str(self.name) + " " + str(self.surname) + " Tel: " + str(self.phone_number)
        )


class client(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    login = models.CharField(max_length=64, unique=True, default="")
    email = models.EmailField(unique=True, blank=False, default="")
    phone_number = models.CharField(max_length=23, unique=True, blank=True)

    def __str__(self):
        return str(
            str(self.name) + " " + str(self.surname) + " Tel: " + str(self.phone_number) + " E-mail: " + str(self.email)

        )

    def get_login(self):
        return self.login

    def get_email(self):
        return self.email



class service_request(models.Model):
    client_id = models.ForeignKey(client, on_delete=models.CASCADE)
    ZIP_code = models.CharField(max_length=7, blank=True)
    city = models.CharField(max_length=32, blank=True)
    street_number = models.CharField(max_length=64, blank=True)
    date_of_request = models.DateTimeField('Date of service request')
    date_of_completion = models.DateTimeField('Date of service request completed', blank=True, null=True)

    def __str__(self):
        return str(self.client_id)

    def get_date_to_client(self):
        return self.date_of_request


class hardware(models.Model):
    request_id = models.ForeignKey(service_request, on_delete=models.CASCADE)
    brand = models.CharField(max_length=32, blank=True)
    model = models.CharField(max_length=32)
    serial_number = models.CharField(max_length=64)
    client_description = models.CharField(max_length=1024)
    warranty = models.BooleanField

    def __str__(self):
        return str(
            str(self.brand) + " " + str(self.model)
        )
    def get_brand(self):
        return self.brand


class repair_part(models.Model):
    brand = models.CharField(max_length=32)
    producer_num = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField(null=True)

    def __str__(self):
        return str(
            str(self.brand) + " " + str(self.description)
        )


class hardware_fault(models.Model):
    hardware_id = models.ForeignKey(hardware, on_delete=models.CASCADE)
    repair_part_id = models.ForeignKey(repair_part, on_delete=models.CASCADE, blank=True, null=True)
    employee_id = models.ForeignKey(employee, on_delete=models.CASCADE, blank=True)
    professional_description = models.CharField(max_length=512)
    repair_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(
            str(self.hardware_id) + ": " + str(self.professional_description)
        )


class specialization(models.Model):
    name = models.CharField(max_length=64)
    hourly_wage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(
            str(self.name) + " " + str(self.hourly_wage)
        )


class employee_specialization(models.Model):
    employee_id = models.ForeignKey(employee, on_delete=models.CASCADE)
    specialization_id = models.ForeignKey(specialization, on_delete=models.CASCADE)

    def __str__(self):
        return str(
            str(self.employee_id) + " " + str(self.specialization_id)
        )