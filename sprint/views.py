from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models


class SprintListView(ListView):
    model = models.Sprint


class SprintDetailView(DetailView):
    context_object_name = 'sprint_details'
    model = models.Sprint
    template_name = 'sprint/sprint_detail.html'


class SprintCreateView(CreateView):
    fields = ("project_backlog","name","start_date","end_date")
    model = models.Sprint


class SprintUpdateView(UpdateView):
    fields = ("name","start_date","end_date")
    model = models.Sprint

class SprintDeleteView(DeleteView):
    model = models.Sprint
    success_url = reverse_lazy("sprint:list")

