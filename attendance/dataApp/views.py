from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee,Attendance
from .serializers import EmployeeSerializer,DateSerializer
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from django.contrib.auth import logout
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
import json

# Create your views here.

def get_current_month():
    return datetime.now().month

def get_current_year():
    return datetime.now().year


def tests_by_month(request, id):
    person = Employee.objects.get(id=id)
    month = request.GET.get('month', get_current_month())
    year = request.GET.get('year', get_current_year()) 
    test_list = person.tests.filter(day__month=int(month), day__year=int(year))
    print(str((test_list)))
    context = {'test_list': test_list}
    return render(request, 'dataApp/templates.html', context = context)
    

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DateViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = DateSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated,DjangoModelPermissions]