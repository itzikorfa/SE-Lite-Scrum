from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from .models import User

class SignUp(LoginRequiredMixin,CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"


class UserInfo(LoginRequiredMixin, DetailView):
    fields = ("name")
    model = User