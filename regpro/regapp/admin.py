from django.contrib import admin
from .models import Customer


class AdminCustomer(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'username', 'pwd', 'mn']


admin.site.register(Customer, AdminCustomer)
