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