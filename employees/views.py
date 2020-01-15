from django.shortcuts import render
from django.core.validators import FileExtensionValidator

from .models import Employee

# Create your views here.


def employees_list(request):
    employees = Employee.object.all()
    return render(request, 'employees/employees_list.html', {'employees': employees})


def upload_employee_data(request):
    if request.method == 'GET':
        return render(request, 'employees/upload_data.html')
    # elif request.method == 'POST':


def uploads_log(request):
    return render(request, 'employees/uploads_log.html')
