from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models

# Create your views here.


class CompanyListView(ListView):
    model = models.Company


class CompanyDetailView(DetailView):
    context_object_name = 'company_details'
    model = models.Company
    template_name = 'company/company_detail.html'


class CompanyCreateView(CreateView):
    fields = ("name",)
    model = models.Company


class CompanyUpdateView(UpdateView):
    fields = ("name",)
    model = models.Company

class ComapnyDeleteView(DeleteView):
    model = models.Company
    success_url = reverse_lazy("company:list")

