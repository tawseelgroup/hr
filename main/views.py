from django.shortcuts import render, redirect
from .models import Company, Saudi, Employee, Iqama
from .forms import EmployeeForm

from django.http import FileResponse
import os

from django.http import HttpResponse
from django.views import View
from django.templatetags.static import static

# Create your views here.

def main(request):
    com = Company.objects.all() 
    c = Company.objects.count()

    for e in com:
        e.employees = Employee.objects.filter(company=e.id).count()
        
    # for e in range(c):
    # print(com.len)

    context = {
        'com': com,
    }
    return render(request, 'home.html', context)


def company(request, id):
    emp = Employee.objects.filter(company=id)
    com = Company.objects.get(id=id)
    context = {
        'emp': emp,
        'com': com,
    }
    return render(request, 'company/company.html', context)

def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            nationality = form.cleaned_data['nationality']
            sex = 1
            company = form.cleaned_data['company']
            job = form.cleaned_data['job']
            inwork = form.cleaned_data['inwork']
            salary = form.cleaned_data['salary']
            identity = '1558'
            bdate = form.cleaned_data['bdate']
            Saudi.objects.create(name=name, nationality=nationality, sex=sex, company=company, job=job, inwork= inwork, salary=salary, identity=identity, bdate=bdate)
            
            # form.save()
            return redirect('main')
    return render(request, 'home.html')


def AddEmployee(request):
    form = EmployeeForm()
    return render(request, 'company/add.html', {'form': form})


def iqama(request, id):
    com = Company.objects.get(id=id)
    emp = Iqama.objects.filter(company=id)
    context = {
        'com': com,
        'emp': emp,
    }
    return render(request, 'company/iqama.html',context)

def contract(request, id):
    com = Company.objects.get(id=id)
    emp = Employee.objects.filter(company=id)
    context = {
        'com': com,
        'emp': emp,
    }
    return render(request, 'company/contract.html', context)


def payroll(request, id):
    com = Company.objects.get(id=id)
    emp = Employee.objects.filter(company=id)
    context = {
        'com': com,
        'emp': emp,
    }
    return render(request, 'company/payroll.html', context)


def tasks(request, id):
    com = Company.objects.get(id=id)
    emp = Employee.objects.filter(company=id)
    context = {
        'com': com,
        'emp': emp,
    }
    return render(request, 'company/tasks.html', context)


def fleet(request, id):
    com = Company.objects.get(id=id)
    emp = Employee.objects.filter(company=id)
    context = {
        'com': com,
        'emp': emp,
    }
    return render(request, 'company/fleet.html', context)


def employeeiqama(request, c, e):
    emp = Employee.objects.get(id=e)
    com = Company.objects.get(id=c)
    context={
        'emp': emp,
        'com': com,
    }
    return render(request, 'company/employeeiqama.html', context)

def download_pdf(request):
    # Define the path to the PDF file
    pdf_path = os.path.join('files', 'c/', 'your', 'pdf-file.pdf')

    # Open the file in binary mode
    file = open(pdf_path, 'files/rb')

    # Create a response with the file and the correct content type
    response = FileResponse(file, content_type='application/pdf')

    # Optionally set Content-Disposition to force download
    response['Content-Disposition'] = 'attachment; filename="downloaded_file.pdf"'

    return response

class OpenPDFView(View):
    def get(self, request, *args, **kwargs):
        # Path to your PDF file
        pdf_path = "{% static 'files/pdf-file.pdf' %}"
        
        
        # Open the file in binary mode
        with open(pdf_path, 'rb') as pdf_file:
            # Read the PDF content
            pdf_data = pdf_file.read()

        # Create an HTTP response with the PDF data
        response = HttpResponse(pdf_data, content_type='application/pdf')
        
        # Add content disposition to open in a new tab
        response['Content-Disposition'] = 'inline; filename="pdf-file.pdf"'
        
        return response
    
def prods(request):
    if request.method == 'POST':
        prods = request.POST
        b1 = prods.get('b1')
        b2 = prods.get('b2')
        b3 = prods.get('b3')
        b4 = prods.get('b4')
        b5 = prods.get('b5')
        b6 = prods.get('b6')
        context = {
            'b1': b1,
            'b2': b2,
            'b3': b3,
            'b4': b4,
            'b5': b5,
            'b6': b6,
        }
        return render(request, 'prods.html', context)
    return render(request, 'prods.html')





