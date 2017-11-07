from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.shortcuts import get_object_or_404
from project.models import ProjectBacklog
from accounts.models import User
from . import models
from sprint.models import Sprint

class TaskListView(ListView):
    model = models.Task


class TaskDetailView(DetailView):
    context_object_name = 'task_details'
    model = models.Task
    template_name = 'task/task_detail.html'


class TaskCreateView(CreateView):
    fields = ('name','description',
              'priority','task_type'
              ,'team','estimated_time',)
    model = models.Task

    def form_valid(self, form):
        project_pk = self.kwargs.pop('pk')
        form.instance.projectBacklog = get_object_or_404(ProjectBacklog, pk=project_pk)
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(UpdateView):
    fields = ('name', 'description','estimated_time',
              'priority', 'task_type','is_sub_task', 'parent_task', 'link_task'
              , 'team','estimated_time')
    model = models.Task

class TaskDeleteView(DeleteView):
    model = models.Task
    success_url = reverse_lazy("task:list")

class TaskPropertyListView(ListView):
    model = models.Task


class TaskPropertyCreateView(CreateView):
    fields = ( 'sprint','assign_to','task_stage')
    model = models.TaskProperty
    template_name = 'task/task_form.html'

    def get_form(self, form_class=None):
        form = super(TaskPropertyCreateView, self).get_form(form_class)
        task_id = self.kwargs['pk']
        task = get_object_or_404(models.Task, pk=task_id)
        form.fields["assign_to"].queryset = User.objects.filter(groups__name=task.team.name)
        form.fields["sprint"].queryset= Sprint.objects.filter(project_backlog = task.projectBacklog)
        return form

    def form_valid(self, form):
        task_pk = self.kwargs.pop('pk')

        form.instance.task = get_object_or_404(models.Task, pk=task_pk)
        return super(TaskPropertyCreateView, self).form_valid(form)

class TaskPropertyUpdateView(UpdateView):
    fields = ('sprint','assign_to','end_date')
    model = models.TaskProperty
    template_name = 'task/task_form.html'

class TaskPropertyDeleteView(DeleteView):
    model = models.TaskProperty
    success_url = reverse_lazy("task:list")
#     TODO: add logs to task detail


class TaskFinished(UpdateView):
    model = models.Task
    fields = ('task_completed',)
