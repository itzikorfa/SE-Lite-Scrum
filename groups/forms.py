from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import NON_FIELD_ERRORS
from .models import GroupMember
from django import forms

class GroupMemberForm(forms.ModelForm):
    class Meta:
        model = GroupMember
        fields = ('user',)
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(user)s's  are not unique.",
            }
        }

