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

    def get_form(self, form_class=None):
        form = super(TaskCreateView, self).get_form(form_class)
        from groups.models import GroupMember,Group
        projecktpk = self.kwargs['pk']
        projectbl = get_object_or_404(models.ProjectBacklog, pk=projecktpk)
        # company = get_object_or_404(Company, pk=project.company.pk)
        # group = get_object_or_404(Group, name = company.name)
        form.fields["team"].queryset= Group.objects.filter(company = projectbl.project.company)
        return form

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
    template_name = 'task/task_form_prop.html'

    def get_form(self, form_class=None):
        form = super(TaskPropertyCreateView, self).get_form(form_class)
        task_id = self.kwargs['pk']
        task = get_object_or_404(models.Task, pk=task_id)
        form.fields["assign_to"].queryset = task.team.members.all()
        form.fields["sprint"].queryset= Sprint.objects.filter(project_backlog = task.projectBacklog)
        return form

    def get_context_data(self, **kwargs):
        contex = super(TaskPropertyCreateView,self).get_context_data()
        tp = get_object_or_404(models.Task, pk=self.kwargs['pk'])
        contex['task'] = tp.name
        return contex

    def form_valid(self, form):
        task_pk = self.kwargs.pop('pk')
        form.instance.task = get_object_or_404(models.Task, pk=task_pk)
        return super(TaskPropertyCreateView, self).form_valid(form)

class TaskPropertyUpdateView(UpdateView):
    fields = ('sprint','assign_to','end_date','task_stage')
    model = models.TaskProperty
    template_name = 'task/task_form.html'

class TaskPropertyChangeStageView(UpdateView):
    fields = ('task_stage', )
    model = models.TaskProperty
    template_name = 'task/task_change_stage_form.html'

    def form_valid(self, form):
        from log.models import Log
        pk = self.kwargs['pk']
        taskp = models.TaskProperty.objects.get(pk=pk)
        stage = form.instance.task_stage
        log = Log.objects.create(task=taskp,
                                 log="Stage changed to "+stage.stage_name)
        return super(TaskPropertyChangeStageView, self).form_valid(form)




class TaskPropertyDeleteView(DeleteView):
    model = models.TaskProperty
    success_url = reverse_lazy("task:list")


class TaskFinished(UpdateView):
    model = models.Task
    fields = ('task_completed',)


class TaskUserDetail(TemplateView):
    template_name = "task/tasks_by_username.html"
    context_object_name = "objects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = models.Task.objects.filter(taskProperty__assign_to__username = self.kwargs['username'])

        return context



