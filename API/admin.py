from django.contrib import admin

from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_number', 'date')

admin.site.register(Car, CarAdmin)