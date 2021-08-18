from django.db import models
from django.db.models import fields
from rest_framework import serializers
from EmployeeApp.models import Department, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        models=Department
        fields=('DepartmentID','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        models=Employees
        fields=('EmployeeID','Department','DateOfJoining','PhotoFileName')