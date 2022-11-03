from .views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('docsignup/', Doctor_Signup.as_view(),name='docsignup'),
    path('docsignin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('all-docs', AllDoc.as_view()),
    path('updatedoctor/<int:id>', UpdateDoctor.as_view(), name='updatedoctor') ,
    path('listpatient',ListPatients.as_view),
    path('consultation',DoctorConsultation.as_view(),name='consultation'),

]
