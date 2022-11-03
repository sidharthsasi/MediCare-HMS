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
    
    
TIMESLOT_LIST = (
        ('1', '09:00 – 10:00'),
        ('2', '10:00 – 11:00'),
        ('3', '11:00 – 12:00'),
        ('4', '12:00 – 13:00'),
        ('5', '13:00 – 14:00'),
        ('6', '14:00 – 15:00'),
        ('7', '15:00 – 16:00'),
        ('8', '16:00 – 17:00'),
        ('9', '17:00 – 18:00'),
    )
class Appointment(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    age = models.IntegerField(null=True)
    date = models.DateField(null=True)
    time = models.CharField(max_length=50, choices=TIMESLOT_LIST,null=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    reason_for_visit = models.CharField(max_length=255,null=True)  

    # def __str__(self):
    #     return self.user.username



# TIMESLOT_LIST = (
#         ('1', '09:00 – 10:00'),
#         ('2', '10:00 – 11:00'),
#         ('3', '11:00 – 12:00'),
#         ('4', '12:00 – 13:00'),
#         ('5', '13:00 – 14:00'),
#         ('6', '14:00 – 15:00'),
#         ('7', '15:00 – 16:00'),
#         ('8', '16:00 – 17:00'),
#         ('9', '17:00 – 18:00'),
#     )
# class Appointment(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True)
#     user = models.ForeignKey(Account, on_delete=models.CASCADE,null=True)
#     age = models.IntegerField(null=True)
#     date = models.DateField(null=True)
#     time = models.CharField(max_length=50, choices=TIMESLOT_LIST,null=True)
#     reason_for_visit = models.CharField(max_length=255,null=True)

#     def __str__(self):
#         return self.user.username

#     def __init__(self, username, password):
#         self.username = username