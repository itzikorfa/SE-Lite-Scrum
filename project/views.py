from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from braces.views import SelectRelatedMixin
from . import models

# Create your views here.


class ProjectListView(SelectRelatedMixin, ListView):
    model = models.Project
    select_related = ("company",)


class ProjectDetailView(DetailView):
    context_object_name = 'project_details'
    model = models.Project
    template_name = 'project/project_detail.html'


class ProjectCreateView(CreateView):
    fields = ("name",'description','ETA','company')
    model = models.Project

    def get_form(self, form_class=None):
        form = super(ProjectCreateView, self).get_form(form_class)
        form.fields['ETA'].widget.attrs.update({'class': 'datepicker'})
        return form

class ProjectUpdateView(UpdateView):
    fields = ("name",'description','ETA')
    model = models.Project

class ProjectDeleteView(DeleteView):
    model = models.Project
    success_url = reverse_lazy("project:list")

