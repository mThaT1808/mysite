from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from individual_work_2.models import Department, Worker
from individual_work_2.forms import DepartmentForm, DepartmentWorkerForm


# Create your views here.

def main(request):
    departments = Department.objects.all()
    return render(request, 'main_page_2.html', {'departments': departments})


def workers_departments(request):
    workers = Worker.objects.all()
    departments = Department.objects.all()
    context = {
        'workers': workers,
        'departments': departments,
    }
    return render(request, 'workers_departments.html', context)


def workers_in_department(request: HttpRequest, id: int):
    department = Department.objects.get(pk=id)
    department_id = department.id
    workers = Worker.objects.filter(department=department_id)
    context = {
        'department': department,
        'workers': workers,
    }
    return render(request, 'workers_in_department.html', context)

def department_form(request: HttpRequest):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/individual_work_2/')
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})

def department_worker_form(request: HttpRequest):
    if request.method == 'POST':
        form = DepartmentWorkerForm(request.POST)
        if form.is_valid():
            obj = Department()
            obj.name = form.cleaned_data['department_name']
            obj.description = form.cleaned_data['department_description']
            obj.save()
            obj = Worker()
            obj.name = form.cleaned_data['worker_name']
            obj.phone_number = form.cleaned_data['worker_phone_number']
            obj.department = form.cleaned_data['worker_department']
            obj.save()
            return HttpResponseRedirect('/individual_work_2/')
    else:
        form = DepartmentWorkerForm()
    return render(request, 'department_worker_form.html', {'form': form})
