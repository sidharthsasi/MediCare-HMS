from django.db import models
from account.models import Account
from department.models import Department
from pharmacy.models import Medicine
from django.core.validators import MinValueValidator

# Create your models here.
class Doctor(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)  
    degree=models.CharField(max_length=120)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.first_name
    


class Consulation(models.Model):
    
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey('patients.Patient',on_delete=models.CASCADE)
    symptoms = models.CharField(max_length=200,null=True)
    medicine = models.ForeignKey(Medicine,on_delete=models.CASCADE,null=True)
    morning=models.IntegerField( validators=[MinValueValidator(0)],null=True)
    afternoon=models.IntegerField( validators=[MinValueValidator(0)],null=True)
    night=models.IntegerField( validators=[MinValueValidator(0)],null=True)
    days=models.IntegerField( validators=[MinValueValidator(0)],null=True)


    def __str__(self):
        return self.doctor.user.first_name
        

