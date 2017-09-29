from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from company.models import Company
from . import models
from django.core.urlresolvers import reverse_lazy

class CreateCompany(LoginRequiredMixin, generic.CreateView):
    fields = ("name",)
    model = Company

class UpdateCompany(LoginRequiredMixin, generic.UpdateView):
    fields = ("name",)
    model = Company

class SingleCompany(generic.DetailView):
    model = Company

class ListCompanys(generic.ListView):
    model = Company
