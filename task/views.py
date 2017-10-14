from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models


class TaskListView(ListView):
    model = models.Task


class TaskDetailView(DetailView):
    context_object_name = 'task_details'
    model = models.Task
    template_name = 'task/task_detail.html'


class TaskCreateView(CreateView):
    fields = ('projectBacklog','name','description',
              'priority','task_type','is_sub_task','parent_task','link_task'
              ,'team','estimated_time','task_completed')
    model = models.Task


class TaskUpdateView(UpdateView):
    fields = ('name', 'description','estimated_time',
              'priority', 'task_type','is_sub_task', 'parent_task', 'link_task'
              , 'team','estimated_time', 'task_completed')
    model = models.Task

class TaskDeleteView(DeleteView):
    model = models.Task
    success_url = reverse_lazy("task:list")

class TaskPropertyListView(ListView):
    model = models.Task


class TaskPropertyCreateView(CreateView):
    fields = ('task', 'sprint','assign_to','end_date')
    model = models.TaskProperty
    template_name = 'task/task_form.html'


class TaskPropertyUpdateView(UpdateView):
    fields = ('sprint','assign_to','end_date')
    model = models.TaskProperty
    template_name = 'task/task_form.html'

class TaskPropertyDeleteView(DeleteView):
    model = models.TaskProperty
    success_url = reverse_lazy("task:list")
#     TODO: add logs to task detail
