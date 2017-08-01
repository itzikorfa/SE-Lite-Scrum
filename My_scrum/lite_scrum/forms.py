from django import forms
from .models import Company, ProductBackLog, Product
from django.contrib.auth.models import User, Group

class CompnyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name', 'company_id', 'email'
        ]


class BacklogForm(forms.ModelForm):
    class Meta:
        model = ProductBackLog
        fields = ['name', 'company', 'product_owner']



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'permissions')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'company','description')
