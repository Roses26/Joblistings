
'''
CRUD: 
Create/Add/Insert a new record
Retrieve/Fetch/Get record
Update an existing record
Delete an existing record
    
'''
from django.shortcuts import render, redirect, get_object_or_404

from .models import jobs
from .jobs_form import jobs_form
# Create your views here.
def home(request):
    emps = jobs.objects.all()

    return render(request, 'jobsIndex.html', {'emps': emps})

def create(request):
    form = jobs_form(request.POST or None)
    

    if request.method== 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request, 'job/form.html', {'form': form})

def update(request, emp_id):
    #emp = jobs.objects.get(id=emp_id)
    emp = get_object_or_404(jobs,id=emp_id)
    form = jobs_form(request.POST or None, instance=emp)

    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'jobs_form.html', {'form': form, 'emp': emp}) 

def detail(request, emp_id):
    emp = get_object_or_404(jobs, id=emp_id)
        
    return render(request, 'jobsdetail.html', {'emp': emp}) 

def delete(request, emp_id):
    emp = jobs.objects.get(id=emp_id)

    if request.method == 'POST':
        emp.delete()
        return redirect('home')
    
    return render(request, 'jobsdelete.html', {'emp': emp})

