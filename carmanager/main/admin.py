from django.contrib import admin
#
# Register your models here.
from .models import Transport,Firm,Type_transport

admin.site.register(Transport)
admin.site.register(Firm)
admin.site.register(Type_transport)
