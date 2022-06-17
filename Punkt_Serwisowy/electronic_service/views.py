from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from .models import *
from datetime import datetime
from django.contrib import messages

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
        return HttpResponse("You are not client / unknown error")
    else:
        return render(request, 'electronic_service/user_profile.html',
                      {'user_client': user_logged_in, 'service_request_list': s_r_l,
                       'service_request_hardware_list': s_r_h_l})


def profile_edit(request):
    try:
        user_logged_in = client.objects.get(login=username)
    except(client.DoesNotExist):
        pass

    username = request.user.username
    user_logged_in = client.objects.get(login=username)
    return render(request, 'electronic_service/user_profile_edit.html', {'user_client': user_logged_in})


def profile_edit_result(request):
    client_list = get_list_or_404(client)
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
        return HttpResponse("SOMETHING WENT WRONG KEK")



# def employee(request):
#     # return render(request, 'electronic_service/employee_main_page.html')
#     return render(request, 'electronic_service/employee_main_page.html')
