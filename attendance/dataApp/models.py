from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework.exceptions import APIException
import datetime
import json

# Employee Data 
class Employee(models.Model):
    name = models.CharField(max_length = 20)
    emp_id = models.IntegerField(unique=True)
    email = models.EmailField(max_length = 30)
    phone_no = models.DecimalField(max_digits=10,decimal_places=0, null=True)

    def __str__(self):
        return "Emp_Id :" + str(self.emp_id) + " ||   Name: " + self.name 
    

# Attendance Record
class Attendance(models.Model):
    day = models.DateField(default = datetime.date.today)
    emp = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='tests')
    present = models.BooleanField(default=False)
    emp_name = emp.name

    def __str__(self):
        return str(self.day) #+ "| Emp_Id: "+  str(self.emp.emp_id) +  " | Emp_Name: " + self.emp.name


# Raises Exception for Absent(for weekends) if selected
@receiver(pre_save, sender=Attendance)
def quantity1(sender, instance,*args, **kwargs):
    if instance.day.weekday()==5 or instance.day.weekday()==6:
        raise APIException("On weekends attendace can't be taken")
        instance.present = False



#Raises Exception for Absent(for weekends) if selected
# @receiver(pre_save, sender=Attendance)
# def quantity1(sender, instance,*args, **kwargs):
#     date_str = str(instance.day)
#     year = int(date_str[0:4])
#     month = int(date_str[5:7])
#     day = int(date_str[8:10])
#     if datetime.date(year,month,day).weekday()==5 or datetime.date(year,month,day).weekday()==6:
#         raise APIException("On Weekends Attendace can't be taken")
#         instance.present = False