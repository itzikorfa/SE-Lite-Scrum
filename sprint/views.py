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

    def get_context_data(self, **kwargs):
        context = super(SprintDetailView, self).get_context_data(**kwargs)
        sprint = models.Sprint.objects.get(pk=self.kwargs['pk'])
        if sprint.sprint_available():
            context['available'] = True
        else:
            context['available'] = False
        return context

class SprintCreateView(CreateView):
    fields = ("project_backlog","name","start_date","end_date")
    model = models.Sprint


class SprintUpdateView(UpdateView):
    fields = ("name","start_date","end_date")
    model = models.Sprint

class SprintDeleteView(DeleteView):
    model = models.Sprint
    success_url = reverse_lazy("sprint:list")

class SprintListForProject(ListView):
    models = models.Sprint


    def get_queryset(self):
        from project.models import Project, ProjectBacklog
        projectPK = self.kwargs['pk']
        pb = ProjectBacklog.objects.get(pk = projectPK)
        return models.Sprint.objects.filter(project_backlog=pb)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        from project.models import Project, ProjectBacklog
        projectPK = self.kwargs['pk']
        pb = ProjectBacklog.objects.get(pk=projectPK)
        contex['project'] = Project.objects.get(pk=pb.project.pk)
        return contex