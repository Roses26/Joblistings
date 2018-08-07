'''
CRUD: 
Create/Add/Insert a new record
Retrieve/Fetch/Get record
Update an existing record
Delete an existing record
    
'''
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import employeePage
from .forms import employeePageForm, SignupForm, LoginForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SignupForm(None)

    return render(request, 'registration.html', {'form': form})

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request,username=uname, password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('employee_home')
   
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def dashboard(request):
    return render(request,'dashboard.html')

#@login_required
def employee_home(request):
    emps = employeePage.objects.all()

    return render(request, 'index.html', {'emps': emps})

def employee_create(request):
    form = employeePageForm(request.POST or None)
    

    if request.method== 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request, 'copy_form.html', {'form': form})

def employee_update(request, emp_id):
    #emp = employeePage.objects.get(id=emp_id)
    emp = get_object_or_404(employeePage,id=emp_id)
    form = employeePageForm(request.POST or None, instance=emp)

    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'form.html', {'form': form, 'emp': emp}) 

def employee_detail(request, emp_id):
    emp = get_object_or_404(employeePage, id=emp_id)
        
    return render(request, 'detail.html', {'emp': emp}) 

def employee_delete(request, emp_id):
    emp = employeePage.objects.get(id=emp_id)

    if request.method == 'POST':
        emp.delete()
        return redirect('home')
    
    return render(request, 'confirm_delete.html', {'emp': emp})
