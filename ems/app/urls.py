from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),

    path('admin-dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('add-employee/',views.add_employee,name='add_employee'),
    path('employees/',views.employee_list,name='employee_list'),


    # path('admin/edit/<int:id>/',views.edit_employee, name='edit_employee'),
    # path('admin/delete/<int:id>/',views.delete_employee,name='delete_employee'),
    # path('admin/assign-work/',views.assign_work, name='assign_work'),

    path('employee/dashboard/', views.employee_dashboard, name='employee_dashboard'),
]