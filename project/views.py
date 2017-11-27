from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from braces.views import SelectRelatedMixin
from . import models
from company.models import Company
from django.shortcuts import get_object_or_404
# Create your views here.
from utiles import utiles
# from project.forms import ProjectBacklogForm

class ProjectListView(SelectRelatedMixin, ListView):
    model = models.Project
    select_related = ("company",)


class ProjectDetailView(DetailView):
    context_object_name = 'project_details'
    model = models.Project
    template_name = 'project/project_detail.html'


class ProjectCreateView(CreateView):
    fields = ("name",'description')
    model = models.Project
    # success_url = reverse_lazy("project:blcreate")

    def get_form(self, form_class=None):
        form = super(ProjectCreateView, self).get_form(form_class)
        # form.fields['ETA'].widget.attrs.update({'class': 'datepicker'})
        return form

    def form_valid(self, form):
        company_pk = self.kwargs.pop('pk')
        form.instance.company = get_object_or_404(Company, pk=company_pk)
        return super(ProjectCreateView, self).form_valid(form)

class ProjectUpdateView(UpdateView):
    fields = ("name",'description')
    model = models.Project


class ProjectDeleteView(DeleteView):
    model = models.Project
    context_object_name = "project"
    success_url = reverse_lazy("project:list")

class ProjectBacklogUpdateView(UpdateView):
    fields = ("ETA", 'start_date',"project_owner", 'scrum_master')
    model = models.ProjectBacklog

    def form_valid(self, form):
        project = self.kwargs.pop('pk')
        form.instance.company = get_object_or_404(models.Project, pk=project)
        return super(ProjectBacklogUpdateView, self).form_valid(form)


    def get_form(self, form_class=None):
        form = super(ProjectBacklogUpdateView, self).get_form(form_class)
        from groups.models import GroupMember,Group
        projectbacklogpk = self.kwargs['pk']
        pb = get_object_or_404(models.ProjectBacklog, pk=projectbacklogpk)
        # project = get_object_or_404(models.Project, pk=pb.project.company)
        # company = get_object_or_404(Company, pk=project.company.pk)
        group = get_object_or_404(Group, name = pb.project.company.name)
        form.fields["project_owner"].queryset= group.members.all()
        form.fields["scrum_master"].queryset= group.members.all()
        return form


class ProjectBacklogDetailView(DetailView):
    fields = ('project',"ETA", "project_owner", 'scrum_master')
    model = models.ProjectBacklog


class ProjectBacklogCreateView(CreateView):
    model = models.ProjectBacklog
    # form_class = ProjectBacklogForm
    fields = ("ETA", 'start_date', "project_owner", 'scrum_master')

    def get_form(self, form_class=None):
        form = super(ProjectBacklogCreateView, self).get_form(form_class)
        from groups.models import GroupMember,Group
        projectpk = self.kwargs['pk']
        project = get_object_or_404(models.Project, pk=projectpk)
        company = get_object_or_404(Company, pk=project.company.pk)
        group = get_object_or_404(Group, name = company.name)
        form.fields["project_owner"].queryset= group.members.all()
        form.fields["scrum_master"].queryset= group.members.all()
        return form

    def form_valid(self, form):
        project = self.kwargs.pop('pk')
        # print("project pk: ", project)
        form.instance.project = get_object_or_404(models.Project, pk=project)
        return super(ProjectBacklogCreateView, self).form_valid(form)


class ProjectBacklogSettingUpdateView(UpdateView):
    fields = ("sprint_length", "sprint_template")
    model = models.ProjectBacklogSettings
    template_name = "project/projectbacklogsettings_form.html"


class ProjectBacklogSettingDetailView(DetailView):
    fields = ('project_backlog',"sprint_length", "sprint_template")
    model = models.ProjectBacklogSettings


class ProjectBacklogSettingCreateView(CreateView):
    fields = ("sprint_length", "sprint_template")
    model = models.ProjectBacklogSettings

    def form_valid(self, form):
        project = self.kwargs.pop('pk')
        form.instance.project_backlog = get_object_or_404(models.ProjectBacklog, pk=project)
        utiles.genrate_sprint(form.instance.project_backlog, form.instance.sprint_length,
                              form.instance.project_backlog.ETA)
        return super(ProjectBacklogSettingCreateView, self).form_valid(form)