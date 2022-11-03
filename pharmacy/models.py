from django.db import models
# Create your models here.


class Medicine(models.Model):
   
    
    medicine=models.CharField(max_length=250,null=True)
    description = models.TextField()
    price = models.IntegerField(null=True)
    
    def __str__(self):
        return self.medicine