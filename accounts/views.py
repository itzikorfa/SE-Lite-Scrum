from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from .models import User
from django.shortcuts import get_object_or_404

class SignUp(LoginRequiredMixin,CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"


class UserInfo(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/accounts_detail.html'
    context_object_name = "context_object_name"

    def get_object(self, queryset=None):
        pk = int(self.kwargs['pk'])
        object = User.objects.get(pk = pk)
        print(object)
        return object


