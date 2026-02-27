from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import*

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('employee_dashboard')

    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('employee_dashboard')
    return render(request, 'admin/dashboard.html')

@login_required
def add_employee(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        designation = request.POST.get('designation')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Employee.objects.create(
            user=user,
            phone=phone,
            department=department,
            designation=designation
        )

        return redirect('employee_list')

    return render(request, 'admin/add_employee.html')

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'admin/employee_list.html', {'employees': employees})

@login_required
def employee_dashboard(request):
    return render(request, 'employee/dashboard.html')

