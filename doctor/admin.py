from django.contrib import admin

from .models import Doctor,Consulation,Record
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Consulation)
admin.site.register(Record)

