from django import forms
from .models import Company

class CompnyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name', 'company_id', 'email'
        ]