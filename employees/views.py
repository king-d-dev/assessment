from django.shortcuts import render, HttpResponse
from django.contrib import messages

from openpyxl import load_workbook

from .models import Employee


# Create your views here.


def employees_list(request):
    employees = Employee.object.all()
    return render(request, 'employees/employees_list.html', {'employees': employees})


def upload_employee_data(request):
    if request.method == 'POST':
        if not request.FILES['employee_data']:
            return render(request, 'employees/upload_data.html')
        wb = load_workbook(filename=request.FILES['employee_data'])
        wk_sheet = wb.active

        for value in wk_sheet.values:
            print(value)

        return HttpResponse('Thanks for the file')

    return render(request, 'employees/upload_data.html')


def uploads_log(request):
    return render(request, 'employees/uploads_log.html')
