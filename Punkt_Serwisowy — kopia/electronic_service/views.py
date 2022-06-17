from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from .models import *
from datetime import datetime

def index(request):


    return render(request, 'electronic_service/indexcopy.html')


def profile(request):
    username = None
    try:
        username = request.user.username
        user_logged_in = client.objects.get(login=username)
        s_r_l = service_request.objects.filter(client_id=user_logged_in.id)


    except(client.DoesNotExist):
        return HttpResponse("You are not client!")
    else:
        return render(request, 'electronic_service/user_profile.html', {'user_client': user_logged_in, 'service_request_list': s_r_l})


def profile_edit(request):
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

        # return render(request, 'electronic_service/indexcopy.html')
        return redirect(reverse('electronic_service:profile'))
    else:
            return render(request, 'electronic_service/user_profile_edit.html', {
                'error_message': "Login is in use, try something different!",
                'user_client': curent_client,
            })

def make_request(request):
    username = request.user.username
    user_logged_in = client.objects.get(login=username)


    return render(request, 'electronic_service/make_request.html', {'user_client': user_logged_in})

def make_request_result(request):
    curent_user = request.user
    curent_client = client.objects.get(login=curent_user.username)
    new_reqest=service_request(
        client_id=curent_client,
        street_number=request.POST['F_street_number'],
        city=request.POST['F_city'],
        ZIP_code=request.POST['F_ZIP_code'],
        date_of_request=datetime.now(),
    )

    new_reqest.save()





    return HttpResponse("XD")



