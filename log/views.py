from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from . import forms
# Create your views here.


class LogListView(ListView):
    model = models.Log


class LogDetailView(DetailView):
    context_object_name = 'log'
    model = models.Log
    template_name = 'log/log_detail.html'


class LogCreateView(CreateView):
    fields = ("task",'log')
    model = models.Log

class LogCreateView4MProject(CreateView):
    model = models.Log
    form_class = forms.LogCreateViewForm4MProject

    def get_context_data(self, **kwargs):
        test = kwargs.pop('prj')
        print(test)
        context = super(LogCreateView4MProject, self).get_context_data(**kwargs)
        context['prj']=self.prj
        print(len(context), context)
        return context


class LogUpdateView(UpdateView):
    fields = ("log",)
    model = models.Log

class LogDeleteView(DeleteView):
    model = models.Log
    success_url = reverse_lazy("log:list")

