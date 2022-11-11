from .views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('signup/', Patient_Signup.as_view(),name='signup'),
    path('signin', MyTokenObtainPairView.as_view()),
    path('signin/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('signout', LogoutView.as_view(), name='auth_logout'),
    path('appointment', BookAppointment.as_view(), name='appointment'),
    path('booklab', BookLab.as_view(), name='booklab'),
    path('getpatient', GetPatient.as_view(), name='getpatient'),
    path('updatepatient/<int:id>', UpdateDelPatient.as_view(), name='updatepatient') ,
    path('allpatient', AllPatient.as_view(), name='allpatient'),


]
