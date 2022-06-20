from django.urls import path
from . import views

app_name = 'electronic_service'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/delete', views.profile_delete, name='profile_delete'),
    path('profile/delete/result', views.profile_delete_result, name='profile_delete_result'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/edit/result', views.profile_edit_result, name='profile_edit_result'),
    path('request_service/', views.make_request, name='make_request'),
    path('request_service/result', views.make_request_result, name='make_request_result'),
    path('request_service/add_hardware_to_<int:request_id>', views.add_request_hardware, name='add_request_hardware'),

    path('employee/client_list', views.client_list_E_P, name='client_list'),
    path('employee/hardware_list', views.hardware_list_E_P, name='hardware_list'),
    path('employee/hardware_fault_list', views.hardware_fault_list_E_P, name='hardware_fault_list'),
    path('employee/service_request_list', views.request_list_E_P, name='service_request_list'),
    path('employee/spare_parts_list', views.spare_parts_list_E_P, name='spare_parts_list'),
    path('employee/profile', views.profile_E_P, name='employee_profile'),
    path('employee/profile/edit', views.profile_edit_E_P, name='employee_profile_edit'),
    path('employee/profile/edit/result', views.profile_edit_result_E_P, name='employee_profile_edit_result'),

]
