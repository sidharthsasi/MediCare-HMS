from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Medicine(models.Model):
   
    
    medicine=models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
    
    def __str__(self):
        return self.medicine