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



# TIMESLOT_LIST = (
#         ('1', '09:00 – 10:00'),
#         ('2', '10:00 – 11:00'),
#         ('3', '11:00 – 12:00'),
#         ('4', '12:00 – 13:00'),
#         ('5', '13:00 – 14:00'),
#     )
# class Appointment(models.Model):
#     doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
#     date = models.ForeignKey(Calendar, on_delete=models.CASCADE)
#     time = models.CharField(max_length=50, choices=TIMESLOT_LIST)
#     reason_for_visit = models.CharField(max_length=255)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.patient.user.email

