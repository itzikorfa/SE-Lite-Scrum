from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from datetime import datetime
from . import models
from task.models import TaskProperty, Task
from django.shortcuts import get_object_or_404
from . import forms
# Create your views here.


class LogListView(ListView):
    model = models.Log


class LogDetailView(DetailView):
    context_object_name = 'log'
    model = models.Log
    template_name = 'log/log_detail.html'


class LogCreateView(CreateView):
    model = models.Log
    # form_class = forms.LogCreateViewForm4MProject
    fields = ('log','presentage_complete','time_spent')

    def get_initial(self):
        task_id = self.kwargs['pk']
        task = get_object_or_404(Task, pk=task_id)
        return {
            'presentage_complete':task.presentage_complete,
        }

    def get_context_data(self, **kwargs):
        contex = super(LogCreateView, self).get_context_data(**kwargs)
        contex['task']=get_object_or_404(Task, pk=self.kwargs['pk']).name
        return contex


    def form_valid(self, form):
        test = self.kwargs.pop('pk')
        task = get_object_or_404(Task, pk=test)
        task.presentage_complete = form.instance.presentage_complete
        if task.presentage_complete == 100:
            task.task_completed = True
            tp = get_object_or_404(TaskProperty, pk=task.taskProperty.pk)
            tp.end_date = datetime.now()
            tp.save()
        else:
            task.task_completed = False
            tp = get_object_or_404(TaskProperty, pk=task.taskProperty.pk)
            tp.end_date = None
            tp.save()
        if task.acutal_time:
            task.acutal_time = task.acutal_time+form.instance.time_spent
        else:
            task.acutal_time = form.instance.time_spent
        task.save()
        form.instance.task = get_object_or_404(TaskProperty, pk=task.taskProperty.pk)# success_url = reverse_lazy("project:blcreate")

        return super(LogCreateView, self).form_valid(form)


class LogUpdateView(UpdateView):
    fields = ("log",)
    model = models.Log

class LogDeleteView(DeleteView):
    model = models.Log
    success_url = reverse_lazy("log:list")

