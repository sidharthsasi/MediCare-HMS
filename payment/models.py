from django.db import models
from account.models import Account
# Create your models here.


class RazorpayPayment(models.Model):
    name=models.ForeignKey(Account,on_delete=models.CASCADE)
    Amount           = models.CharField(max_length=200)
    razor_pay       = models.CharField(max_length=200)
    provider_order_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name.first_name



            #     "name" : name,
            # "merchantId": "RAZOR_KEY",
            # "amount": amount,
            # "currency" : 'INR' ,
            # "orderId" : razorpay_order["id"],




class Channel(models.Model):
    name = models.CharField(unique=True, max_length=120)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} said {self.message}'

    class Meta:
        ordering = ['timestamp']