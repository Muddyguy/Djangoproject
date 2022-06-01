from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartmentSerializer(serializers.models):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'DepartmentName')
                  
class EmployeeSerializer(serializers.models):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                  'EmployeeName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName')
                                   