from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    form_class = forms.MemberCreateForm
    success_url = reverse_lazy("login")
    template_name = "member/signup.html "
# Create your views here.
