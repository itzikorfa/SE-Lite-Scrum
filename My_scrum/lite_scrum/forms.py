from django import forms
from django.contrib.auth import base_user
from .models import Company, Backlog
from django.contrib.auth.models import User

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

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')