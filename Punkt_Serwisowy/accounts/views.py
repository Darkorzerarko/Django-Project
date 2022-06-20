from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.models import User
from electronic_service.models import *
from django.http import HttpResponse


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

        var1 = False
        var2 = False
        var3 = False
        client_list = client.objects.all()

        for c in client_list:
            if c.login == request.POST['F_login']:
                var1 = True
            elif c.email == request.POST['F_email']:
                var2 = True
            elif c.phone_number == request.POST['F_phone_number']:
                var3 = True
            else:
                pass

        if not var1 and not var2 and not var3:

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

        elif var1:
            if var2:
                if var3:
                    return render(request, 'registration/signup.html', {
                        'error_message': "Username, email address and phone number are in use, please try something else",
                    })
                else:
                    return render(request, 'registration/signup.html', {
                        'error_message': "Username and email address are in use, please try something else",
                    })
            else:
                return render(request, 'registration/signup.html', {
                    'error_message': "Username is in use, please try something else",
                })
        elif var2:
            if var3:
                return render(request, 'registration/signup.html', {
                    'error_message': "Email address and phone number are in use, please try something else",
                })
            else:
                return render(request, 'registration/signup.html', {
                    'error_message': "Phone number is in use, please try something else",
                })
        else:
            return HttpResponse("Unknown Error ¯\_( ͡° ͜ʖ ͡°)_/¯")
    else:
        return render(request, 'registration/signup.html', {
            'error_message': "You password is different!",
        })
