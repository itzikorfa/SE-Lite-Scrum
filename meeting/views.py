from django.shortcuts import render
from   . import models
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from django.shortcuts import get_object_or_404
from groups.models import Group
from task.models import Task
from datetime import datetime as dt

# Create your views here.
class MeetingListView(ListView):
    model = models.Meeting

    def get_queryset(self):
        teampk = self.kwargs.pop('team')
        teamobj = Group.objects.get(pk = teampk)
        return models.Meeting.objects.all().filter(team = teamobj)

class MeetingDetailView(DetailView):
    context_object_name = 'meet'
    model = models.Meeting

class MeetingCreateView(CreateView):
    model = models.Meeting
    fields = ('type','date','log')

    def form_valid(self, form):
        group = self.kwargs.pop('group')
        form.instance.team = get_object_or_404(Group, slug=group)
        return super(MeetingCreateView, self).form_valid(form)


class MeetingCreateDailyView(CreateView):
    model = models.Meeting
    fields = ('date','log')
    template_name = 'meeting/meeting_daily_form.html'

    def get_form(self, form_class=None):
        # TODO get all tasks in current sprints of groups
        form = super(MeetingCreateDailyView, self).get_form(form_class)
        group_slug = self.kwargs['slug']
        group = Group.objects.get(slug=group_slug)
        tasks = Task.objects.filter(team=group, taskProperty__sprint__start_date__lte=dt.today().date(),
                            taskProperty__sprint__end_date__gte=dt.today().date(),
                            task_completed = False)
        res = ""
        ans = "*   What have you completed the last meeting?\n" \
              "*   What do you plan to complete the next meeting?\n" \
              "*   What is getting in your way?"
        self.tasks_meta = ""
        for task in tasks:
            res += "Task '{}' assign to @{}:\n".format(task.name, task.taskProperty.assign_to)
            res += ans + '\n'*2
            self.tasks_meta += task.name+'\n'
        form.initial = {'log': res}

        return form

    def form_valid(self, form):
        group = self.kwargs.pop('slug')
        form.instance.team = get_object_or_404(Group, slug=group)
        form.instance.type = get_object_or_404(models.MeetingType, name="Daily")
        form.instance.tasks_meta = self.tasks_meta
        return super(MeetingCreateDailyView, self).form_valid(form)

class MeetingUpdateView(UpdateView):
    fields = ("log",)
    model = models.Meeting




class MeetingDeleteView(DeleteView):
    model = models.Meeting
    success_url = reverse_lazy("meeting:list")

