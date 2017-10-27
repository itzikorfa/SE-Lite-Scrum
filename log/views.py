from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from task.models import TaskProperty
from django.shortcuts import get_object_or_404
from . import forms
# Create your views here.


class LogListView(ListView):
    model = models.Log


class LogDetailView(DetailView):
    context_object_name = 'log'
    model = models.Log
    template_name = 'log/log_detail.html'


# class LogCreateView(CreateView):
#     fields = ("task",'log')
#     model = models.Log

class LogCreateView(CreateView):
    model = models.Log
    # form_class = forms.LogCreateViewForm4MProject
    fields = ('log',)
    #
    #
    # def get_context_data(self, **kwargs):
    #     test = self.kwargs.pop('pk')
    #     self.task = get_object_or_404(TaskProperty, pk=test)
    #     context = super(LogCreateView, self).get_context_data(**kwargs)
    #     context['pk']=test
    #     print(len(context), context)
    #     return context

    def form_valid(self, form):
        test = self.kwargs.pop('pk')
        # print(test)

        form.instance.task = get_object_or_404(TaskProperty, pk=test)# success_url = reverse_lazy("project:blcreate")

        return super(LogCreateView, self).form_valid(form)


class LogUpdateView(UpdateView):
    fields = ("log",)
    model = models.Log

class LogDeleteView(DeleteView):
    model = models.Log
    success_url = reverse_lazy("log:list")

