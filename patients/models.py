import imp
from django.db import models
from account.models import Account
from department.models import Department
from doctor.models import Doctor
# Create your models here.




class Patient(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_of_birth = models.DateField() 
    address = models.CharField(max_length=255) 
    blood_group = models.CharField(max_length=20,null=True)
    

    def __str__(self):
        return self.user.first_name
    
    

class Appointment(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    age = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
        

    def __str__(self):
        return self.user.first_name