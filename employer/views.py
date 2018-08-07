
'''
CRUD: 
Create/Add/Insert a new record
Retrieve/Fetch/Get record
Update an existing record
Delete an existing record
    
'''
from django.shortcuts import render, redirect, get_object_or_404

from .models import employer
from .employer_form import employer_form
# Create your views here.
def employer_home(request):
    emps = employer.objects.all()

    return render(request, 'EmployerIndex.html', {'emps': emps})

def employer_create(request):
    
    if request.method == 'POST':
        form = employer_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = employer_form(None)
        
    return render(request, 'Copy_employerForm.html', {'form': form})

def employer_update(request, emp_id):
    #emp = Employer.objects.get(id=emp_id)
    emp = get_object_or_404(employer,id=emp_id)
    form = employer_form(request.POST or None, instance=emp)

    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'Employer_form.html', {'form': form, 'emp': emp}) 

def employer_detail(request, emp_id):
    emp = get_object_or_404(employer, id=emp_id)
        
    return render(request, 'Employerdetail.html', {'emp': emp}) 

def employer_delete(request, emp_id):
    emp = employer.objects.get(id=emp_id)

    if request.method == 'POST':
        emp.delete()
        return redirect('home')
    
    return render(request, 'Employer_delete.html', {'emp': emp})
