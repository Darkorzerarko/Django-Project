from django.urls import path
from . import views

app_name = 'electronic_service'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/edit/result', views.profile_edit_result, name='profile_edit_result'),
    path('request_service/', views.make_request, name='make_request'),
    path('request_service/result', views.make_request_result, name='make_request_result'),

]
