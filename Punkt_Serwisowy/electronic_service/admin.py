from django.contrib import admin
from .models import employee, client, service_request, hardware, repair_part, hardware_fault, specialization, employee_specialization

admin.site.register(employee)
admin.site.register(client)
admin.site.register(service_request)
admin.site.register(hardware)
admin.site.register(repair_part)
admin.site.register(hardware_fault)
admin.site.register(specialization)
admin.site.register(employee_specialization)
