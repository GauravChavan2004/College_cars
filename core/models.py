from django.db import models
from django.contrib.auth.models import User
import re
class Car(models.Model):
    MAKE_CHOICES = [
        ('MARUTI', 'Maruti'),
        ('HYUNDAI', 'Hyundai'),
        ('TATA', 'Tata'),
        ('TOYOTA', 'Toyota'),
        ('HONDA', 'Honda'),
        ('FORD', 'Ford'),
        ('KIA', 'Kia'),
        # Add more makes as needed
    ]

    
    make = models.CharField(max_length=20, choices=MAKE_CHOICES)
    model = models.CharField(max_length=100)
    registration_year = models.CharField(max_length=10, help_text="Enter in the format: eg. Aug 2020")
    manufacture_year = models.IntegerField()
    owner = models.IntegerField()
    km_driven = models.IntegerField()
    transmission_type = models.CharField(max_length=20, choices=[('MANUAL', 'Manual'), ('AUTOMATIC', 'Automatic')])
    fuel_type = models.CharField(max_length=20, choices=[('PETROL', 'Petrol'), ('DIESEL', 'Diesel'),('PETROL+CNG', 'Petrol+cng'), ('ELECTRIC', 'Electric')])
    insurance_validity = models.CharField(max_length=100)
    insurance_type = models.CharField(max_length=20, choices=[('COMPREHENSIVE', 'Comprehensive'), ('THIRD-PARTY', 'Third-Party')])
    RTO = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car_location = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.make} {self.model} ({self.registration_year})"