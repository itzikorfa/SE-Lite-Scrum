from django import forms

from .models import Company, Backlog


class CompnyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name', 'company_id', 'email'
        ]


class BacklogForm(forms.ModelForm):
    class Meta:
        model = Backlog
        fields = ['name', 'company']
