from django.db import models
from datetime import datetime

class CreditCardApplication(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    ssn = models.CharField(max_length=11, unique=True)
    
    # Contact Information
    work_phone = models.CharField(max_length=15, blank=True, null=True)
    home_phone = models.CharField(max_length=15, blank=True, null=True)
    mobile_phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    
    # Address
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    
    # Employment
    company = models.CharField(max_length=100, blank=True, null=True)
    employment_status = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    employment_duration = models.CharField(max_length=50, blank=True, null=True)
    
    # Financial Information
    income = models.DecimalField(max_digits=10, decimal_places=2)
    bank_account = models.BooleanField()
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    
    # Preferences & T&C
    language = models.CharField(max_length=50)
    agreed_terms = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
