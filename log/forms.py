from django import forms
from static.browser.utiles.widgets import RangeInput
from .models import Log
from task.models import Task

class LogCreateViewForm4MProject(forms.ModelForm):
    class Meta:
        model= Log
        fields = ('task', 'log', )

    def __init__(self, *args, **kwargs):
        # if 'task_id' in kwargs:
        task_id=kwargs.pop('prj')
        self.fields['task'].queryset = Task.objects.filter(pk=task_id)
        # self.fields['task'].widget.attrs['readonly'] = True
        super(LogCreateViewForm4MProject, self).__init__(self, *args, **kwargs)


