from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from .models import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User

# OLD VERSION NOT RECOMMEND TO USE IN FUTURE PROJECTS:
# def index(request):
#     client_list = client.objects.all()
#     client_list_logins = []
#     for c in client_list:
#         client_list_logins.append(c.get_login())
#         print(client_list_logins)
#
#     return render(request, 'electronic_service/indexcopy.html', {"client_list": client_list_logins})

def index(request):
    username = request.user.username
    try:
        user_logged_in = client.objects.get(login=username)
    except(client.DoesNotExist):
        try:
            employee_logged_in = employee.objects.get(login=username)
        except(employee.DoesNotExist):
            return render(request, 'electronic_service/index.html')

        else:
            return render(request, 'electronic_service/employee_main_page.html')
    else:
        return render(request, 'electronic_service/index.html')


def profile(request):
    username = request.user.username
    try:
        user_logged_in = client.objects.get(login=username)
        s_r_l = service_request.objects.filter(client_id=user_logged_in.id)
        s_r_h_l = hardware.objects.all()

    except(client.DoesNotExist):
        return HttpResponse("Unknown Error ¯\_( ͡° ͜ʖ ͡°)_/¯")
    else:
        return render(request, 'electronic_service/user_profile.html',
                      {'user_client': user_logged_in, 'service_request_list': s_r_l,
                       'service_request_hardware_list': s_r_h_l})


def profile_edit(request):
    username = request.user.username
    try:
        user_logged_in = client.objects.get(login=username)
        return render(request, 'electronic_service/user_profile_edit.html', {'user_client': user_logged_in})
    except(client.DoesNotExist):
        return HttpResponse("Employee page edit")


def profile_edit_result(request):
    client_list = client.objects.all()
    new_login = request.POST["F_login"]
    curent_user = request.user
    curent_client = client.objects.get(login=curent_user.username)

    var = False

    for c in client_list:
        if c.login == new_login and new_login != curent_user.username:
            var = True

    if not var:
        curent_client.name = request.POST['F_name']
        curent_client.surname = request.POST['F_surname']
        curent_client.login = request.POST['F_login']
        curent_client.email = request.POST['F_email']
        curent_client.phone_number = request.POST['F_phone_number']
        curent_client.save()

        curent_user.username = request.POST['F_login']
        curent_user.email = request.POST['F_email']
        curent_user.first_name = request.POST['F_name']
        curent_user.last_name = request.POST['F_surname']
        curent_user.save()

        return redirect(reverse('electronic_service:profile'))
    else:
        return render(request, 'electronic_service/user_profile_edit.html', {
            'error_message': "Login is in use, try something different!",
            'user_client': curent_client,
        })

def profile_delete(request):
    username = request.user.username
    try:
        user_logged_in = client.objects.get(login=username)
        service_request_list = service_request.objects.filter(client_id=user_logged_in)
        return render(request, 'electronic_service/user_profile_delete.html', {'user_client': user_logged_in, 'services_list': service_request_list})
    except(client.DoesNotExist):
        return HttpResponse("Unknown error")

def profile_delete_result(request):
    username = request.user.username
    try:
        client_logged_in = client.objects.get(login=username)
        user_logged_in = User.objects.get(username=username)
        client_logged_in.delete()
        user_logged_in.delete()
        return render(request, "electronic_service/user_profile_delete_result.html")
    except(client.DoesNotExist or User.DoesNotExist):
        return HttpResponse("Unknown error")

def make_request(request):
    try:
        username = request.user.username
        user_logged_in = client.objects.get(login=username)

    except(client.DoesNotExist):
        messages.success(request, "First login as client")
        return redirect(reverse('login'))
    else:
        return render(request, 'electronic_service/make_request.html', {'user_client': user_logged_in})


def make_request_result(request):
    curent_user = request.user
    curent_client = client.objects.get(login=curent_user.username)
    new_request = service_request(
        client_id=curent_client,
        street_number=request.POST['F_street_number'],
        city=request.POST['F_city'],
        ZIP_code=request.POST['F_ZIP_code'],
        date_of_request=datetime.now(),
    )
    new_request.save()
    return render(request, 'electronic_service/add_request_hardware.html', {'new_request': new_request})


def add_request_hardware(request, request_id):
    curent_request = service_request.objects.get(pk=request_id)
    new_hardware = hardware(
        request_id=curent_request,
        brand=request.POST['F_brand'],
        model=request.POST['F_model'],
        serial_number=request.POST['F_serial_number'],
        client_description=request.POST['F_fault_description'],
    )
    new_hardware.save()

    if 'Continue' in request.POST:
        return render(request, 'electronic_service/add_request_hardware.html', {'new_request': curent_request})
    elif 'That is all' in request.POST:
        return redirect(reverse('electronic_service:profile'))
    else:
        return HttpResponse("Unknown Error ¯\_( ͡° ͜ʖ ͡°)_/¯")


def client_list_E_P(request):
    client_list = client.objects.all()
    return render(request, 'electronic_service/client_list_E_P.html', {'client_list': client_list})


def hardware_list_E_P(request):
    hardware_list = hardware.objects.all()
    return render(request, 'electronic_service/hardware_list_E_P.html', {'hardware_list': hardware_list})

def hardware_fault_list_E_P(request):
    hardware_list = hardware_fault.objects.all()
    return render(request, 'electronic_service/hardware_fault_list_E_P.html', {'hardware_list': hardware_list})

def request_list_E_P(request):
    request_list = service_request.objects.all()
    return render(request, 'electronic_service/service_request_list_E_P.html', {'request_list': request_list})

def spare_parts_list_E_P(request):
    spare_parts_list = repair_part.objects.all()
    return render(request, 'electronic_service/spare_parts_list_E_P.html', {"spare_parts_list": spare_parts_list})


def profile_E_P(request):
    username = request.user.username
    try:
        user_logged_in = employee.objects.get(login=username)
    #     Specialization information needs to be added

    except(employee.DoesNotExist):
        return HttpResponse("Unknown Error ¯\_( ͡° ͜ʖ ͡°)_/¯")
    else:
        return render(request, 'electronic_service/employee_profile.html',
                      {'user_employee': user_logged_in})


def profile_edit_E_P(request):
    username = request.user.username
    try:
        user_logged_in = employee.objects.get(login=username)
        return render(request, 'electronic_service/employyee_profile_edit.html', {'user_employee': user_logged_in})
    except(employee.DoesNotExist):
        return HttpResponse("Unknown Error ¯\_( ͡° ͜ʖ ͡°)_/¯")


def profile_edit_result_E_P(request):
    client_list = employee.objects.all()
    new_login = request.POST["F_login"]
    curent_user = request.user
    curent_employee = employee.objects.get(login=curent_user.username)

    var = False

    for c in client_list:
        if c.login == new_login and new_login != curent_user.username:
            var = True

    if not var:
        curent_employee.name = request.POST['F_name']
        curent_employee.surname = request.POST['F_surname']
        curent_employee.login = request.POST['F_login']
        curent_employee.email = request.POST['F_email']
        curent_employee.phone_number = request.POST['F_phone_number']
        curent_employee.save()

        curent_user.username = request.POST['F_login']
        curent_user.email = request.POST['F_email']
        curent_user.first_name = request.POST['F_name']
        curent_user.last_name = request.POST['F_surname']
        curent_user.save()

        return redirect(reverse('electronic_service:employee_profile'))
    else:
        return render(request, 'electronic_service/employee_profile_edit.html', {
            'error_message': "Login is in use, try something different!",
            'user_client': curent_employee,
        })
