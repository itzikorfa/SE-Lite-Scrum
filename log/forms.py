from django import forms
from static.browser.utiles.widgets import RangeInput
from .models import Log
from task.models import Task

class LogCreateViewForm4MProject(forms.ModelForm):
    class Meta:
        model= Log
        fields = ('task', 'log', )



