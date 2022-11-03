from .views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
  path('dashboard/', AdminDashboard.as_view()),
  path('alldep', AllDepartment.as_view()),
  path('alldoc',AllDoc.as_view()),
  path('allpatient',AllPatient.as_view()),
  path('adddept',AddDepartment.as_view()),
  path('allappointment',AllAppointment.as_view()),
  path('adddoctor',AddDoctor.as_view()),
  path('updatedoctor',UpdateDoctor.as_view()),
  path('addmedicine',AddMedicine.as_view()),



]

