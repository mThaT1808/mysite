import self as self
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from individual_work.models import Job, Contractor, Customer
from individual_work.forms import JobForm, CustomerForm, ContractorCustomerForm

def index(request):
    jobs = Job.objects.all()
    contractors = Contractor.objects.all()
    customers = Customer.objects.all()

    return render(request, 'list_page.html', {'jobs': jobs, 'contractors': contractors, 'customers': customers})

def job_form(request: HttpRequest):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/individual_work/')
        else:
            return HttpResponse('Ошибка')
    else:
        form = JobForm()
    return render(request, 'New_Job_form.html', {'form': form})


def start_page(request):
    return render(request, "main_page_2.html")


def get_customer(request: HttpRequest):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            obj = Customer()
            obj.name = form.cleaned_data['customer_name']
            obj.phone_number = form.cleaned_data['customer_phone_number']
            obj.save()
            return HttpResponseRedirect('/individual_work/')
    else:
        form = CustomerForm()

    return render(request, 'New_customer_form.html', {'form': form})


def contractor_customer_form(request: HttpRequest):
    if request.method == 'POST':
        form = ContractorCustomerForm(request.POST)
        if form.is_valid():
            obj = Contractor()
            obj.name = form.cleaned_data['contractor_name']
            obj.description = form.cleaned_data['contractor_description']
            obj.job = form.cleaned_data['contractor_job']
            obj.save()
            obj = Customer()
            obj.name = form.cleaned_data['customer_name']
            obj.phone_number = form.cleaned_data['customer_phone_number']
            obj.save()
    else:
        form = ContractorCustomerForm()


    return render(request, 'New_contractor_customer_form.html', {'form': form})


def job(request: HttpRequest, id: int):
    _job = Job.objects.get(pk=id)
    job_id = _job.id
    contractors = Contractor.objects.filter(job=job_id)

    ctx = {
        'job': _job,
        'contractors': contractors
    }
    return render(request, 'job.html', ctx)


