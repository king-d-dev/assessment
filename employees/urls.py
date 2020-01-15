from django.urls import path

from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.employees_list, name='list'),
    path('uploads-log/', views.uploads_log, name='uploads_log'),
    path('upload-data/', views.upload_employee_data, name='upload_data')
]
