from errno import EMLINK
from django.db import models
from account.models import Account
# Create your models here.


class Department(models.Model):
    department_name=models.CharField(max_length=100)


    def __str__(self):
        return self.department_name


