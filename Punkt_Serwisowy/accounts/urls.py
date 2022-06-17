from django.urls import path
from . import views

# from .views import SignUpView

app_name = "account"

urlpatterns = [
    path("signup/", views.register_client, name="signup"),
    path("signup/result", views.register_client_result, name="signup_result"),
]