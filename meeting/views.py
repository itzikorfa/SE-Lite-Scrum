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
from sprint.models import Sprint
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

    def get_form(self, form_class=None):
        form = super(MeetingCreateDailyView, self).get_form(form_class)
        group_slug = self.kwargs['slug']
        sprints = Sprint.objects.filter(start_date__lte = dt.today().date(),end_date__gte = dt.today().date())


    def form_valid(self, form):
        group = self.kwargs.pop('group')
        form.instance.team = get_object_or_404(Group, slug=group)
        return super(MeetingCreateDailyView, self).form_valid(form)

class MeetingUpdateView(UpdateView):
    fields = ("log",)
    model = models.Meeting

    def form_valid(self, form):
        group = self.kwargs.pop('project')
        # print(test)

        form.instance.team = get_object_or_404(Group, pk=group)
        return super(MeetingCreateView, self).form_valid(form)


class MeetingDeleteView(DeleteView):
    model = models.Meeting
    success_url = reverse_lazy("meeting:list")

