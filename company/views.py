from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from sprint.models import Sprint
from datetime import datetime as dt
# Create your views here.


class CompanyListView(ListView):
    model = models.Company


class CompanyDetailView(DetailView):
    context_object_name = 'company_details'
    model = models.Company
    template_name = 'company/company_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['sprints'] = Sprint.objects.filter(project_backlog__project__company__pk = self.kwargs['pk'],
                                                   start_date__lte = dt.today().date(),
                                                   end_date__gte = dt.today().date())
        return context


class CompanyCreateView(CreateView):
    fields = ("name",)
    model = models.Company

    def form_valid(self, form):
        object = form.save(commit = False)
        object.owner = self.request.user
        object.save()
        return super(CompanyCreateView, self).form_valid(form)

class CompanyUpdateView(UpdateView):
    fields = ("name",)
    model = models.Company

    def form_valid(self, form):
        object = form.save(commit = False)
        object.owner = self.request.user
        object.save()
        return super(CompanyUpdateView, self).form_valid(form)

class ComapnyDeleteView(DeleteView):
    model = models.Company
    success_url = reverse_lazy("company:list")

