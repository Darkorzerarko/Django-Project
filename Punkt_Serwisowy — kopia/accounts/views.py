from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.models import User
from electronic_service.models import client


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"

def register_client(request):
    # form = Register_new_client
    return render(request, 'registration/signup.html')


def register_client_result(request):
    pass1 = request.POST['F_password']
    pass2 = request.POST['F_password_2']
    if pass1 == pass2:

        new_user = client(
            name=request.POST['F_name'],
            surname=request.POST['F_surname'],
            login=request.POST['F_login'],
            email=request.POST['F_email'],
            phone_number=request.POST['F_phone_number'],
        )

        new_user.save()
        user = User.objects.create_user(username=request.POST['F_login'],
                                        email=request.POST['F_email'],
                                        password=request.POST['F_password'],
                                        first_name=request.POST['F_name'],
                                        last_name=request.POST['F_surname'])
        user.save()
        return render(request, 'registration/signup_result.html')
    else:
        return render(request, 'registration/signup.html', {
            'error_message': "You password is different!",
        })
