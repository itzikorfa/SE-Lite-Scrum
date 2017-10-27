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
        # print(test)

        form.instance.team = get_object_or_404(Group, pk=group)
        return super(MeetingCreateView, self).form_valid(form)


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

