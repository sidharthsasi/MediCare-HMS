from django.db import models
from account.models import Account
from department.models import Department
# Create your models here.
class Doctor(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)  
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
