from django.contrib import admin

# Register your models here.
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'registration_year', 'km_driven', 'price', 'car_location', 'owner')
    list_filter = ('make', 'fuel_type', 'transmission_type', 'insurance_type')
    search_fields = ('make', 'model', 'car_location')
    ordering = ('-registration_year',)  # Display cars in reverse order of registration year

admin.site.register(Car, CarAdmin)