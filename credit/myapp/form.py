# '''from django import forms
# from .models import CreditCardApplication

# class CreditCardApplicationForm(forms.ModelForm):
#     class Meta:
#         model = CreditCardApplication
        
#         fields = '__all__'  # ✅ Without parentheses or brackets'''
# from django import forms
# from .models import CreditCardApplication

# class CreditCardApplicationForm(forms.ModelForm):
#     class Meta:
#         model = CreditCardApplication
#         fields = '__all__'
#         widgets = {
#             'dob': forms.DateInput(attrs={'type': 'date'}),
#         }

from django import forms
from .models import CreditCardApplication

class CreditCardApplicationForm(forms.ModelForm):
    class Meta:
        model = CreditCardApplication
        fields = '__all__'  # Includes all model fields, or specify: ['first_name', 'last_name', ...]
