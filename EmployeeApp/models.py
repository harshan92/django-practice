from django.db import models

# Create your models here.
class Department(models.Model):
    DepartmentID=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeID=models.AutoField(primary_key=True)
    Department=models.CharField(max_length=500)
    DateOfJoining=models.DateField()
    PhotoFileName=models.CharField(max_length=500)