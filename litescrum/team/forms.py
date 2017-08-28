from django import forms
from .models import Team, User

class TeamForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    class Meta:
        model = Team
        fields = ('name',)

