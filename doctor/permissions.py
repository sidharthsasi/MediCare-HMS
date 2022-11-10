from email import message
from rest_framework.permissions import BasePermission


class isDoctor(BasePermission):
    message='you are not Doctor'
    def has_permission(self,request,view):
        if request.user.is_authenticated and request.user.is_doctor:
            return True
