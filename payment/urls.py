
from django.urls import path
from .views import *

urlpatterns = [

    path('razorpay_order', PaymentView.as_view(), name='razorpay_order'),
    path('razorpay_callback', CallbackView.as_view(), name='razorpay_callback'),
]