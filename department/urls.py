from .views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('adddep', AddDepartment.as_view(),name='addep'),
    path('alldep', AllDepartment.as_view()),

]
