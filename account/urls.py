from .views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', Signup.as_view(),name='signup'),
    path('signin', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]
