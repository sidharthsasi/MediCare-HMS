from django.db import models
from account.models import Account
from department.models import Department
from pharmacy.models import Medicine

# Create your models here.
class Doctor(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)  
    department = models.ForeignKey(Department,on_delete=models.CASCADE)


    def __str__(self):
        return self.user.first_name
    


class Consulation(models.Model):
    
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    symptoms = models.CharField(max_length=200)
    medicine = models.ForeignKey(Medicine,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user.first_name