from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Medicine(models.Model):
   
    
    medicine=models.CharField(max_length=500)
    morning=models.IntegerField( validators=[MinValueValidator(0, message='Number of medicines cannot be negative')])
    afternoon=models.IntegerField( validators=[MinValueValidator(0, message='Number of medicines cannot be negative')])
    evening=models.IntegerField( validators=[MinValueValidator(0, message='Number of medicines cannot be negative')])
    days=models.IntegerField( validators=[MinValueValidator(0, message='Number of days cannot be negative')])
    
    def __str__(self):
        return self.description