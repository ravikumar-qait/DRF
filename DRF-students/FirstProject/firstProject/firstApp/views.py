from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee

# Create your views here.

def employeeViews(request):
    emp = {
        'id' : 12,
        'name' : 'Veer',
        'salary' : 10000000
    }
    data = Employee.objects.all()

    response = {'employees':list(data.values('name','sal'))}

    return JsonResponse(response)