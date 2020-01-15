from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True)
    date_of_birth = models.DateTimeField()
    date_of_employment = models.DateTimeField()
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    supervisors = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True)


class Upload(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    number_of_records_uploaded = models.IntegerField()
    status = models.CharField(max_length=255)
    errors = models.TextField()
