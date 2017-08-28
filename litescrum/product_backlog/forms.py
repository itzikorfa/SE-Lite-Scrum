from django import forms
from .models import ProductBackLog

class ProductBacklogForm(forms.ModelForm):
    class Meta:
        model = ProductBackLog
        fields = ['name', 'product', 'product_owner']