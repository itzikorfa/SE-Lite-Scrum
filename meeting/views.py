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
        teampk = self.kwargs.pop('slug')
        teamobj = get_object_or_404(Group, slug=teampk)
        return models.Meeting.objects.all().filter(team = teamobj)


class MeetingStoryListView(ListView):
    model = models.Meeting
    template_name = 'meeting/meeting_story_list.html'

    # def get_queryset(self):
    #     teampk = self.kwargs['slug']
    #     teamobj = Group.objects.get(pk = teampk)
    #     return models.Meeting.objects.all().filter(team = teamobj)

    def get_context_data(self, **kwargs):
        contex = super(MeetingStoryListView,self).get_context_data(**kwargs)
        contex['group'] = get_object_or_404(Group, slug=self.kwargs['slug'])
        contex['meeting'] = models.Meeting.objects.all().filter(team=contex['group'])
        return contex

class MeetingDetailView(DetailView):
    context_object_name = 'meet'
    model = models.Meeting

class MeetingCreateView(CreateView):
    model = models.Meeting
    fields = ('type','date','log')

    def form_valid(self, form):
        group = self.kwargs.pop('slug')
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




class MeetingSpritPlanningView(CreateView):
    model = models.Meeting
    fields = ('date','log')
    template_name = 'meeting/meeting_sprint_planing_form.html'

    def form_valid(self, form):
        from company.models import Company
        from django.utils.text  import slugify
        companyPK = self.kwargs.pop('pk')
        print(companyPK)
        company = get_object_or_404(Company, pk=companyPK)
        groupSlug = slugify(company.name)
        form.instance.team = get_object_or_404(Group, slug=groupSlug , company=company)
        form.instance.type = get_object_or_404(models.MeetingType, name="Sprint Planning")
        return super(MeetingSpritPlanningView, self).form_valid(form)



class MeetingSpritReviewView(CreateView):
    model = models.Meeting
    fields = ('date','log')
    template_name = 'meeting/meeting_sprint_review_form.html'


    def form_valid(self, form):
        from company.models import Company
        from django.utils.text import slugify
        companyPK = self.kwargs.pop('pk')
        print(companyPK)
        company = get_object_or_404(Company, pk=companyPK)
        groupSlug = slugify(company.name)
        form.instance.team = get_object_or_404(Group, slug=groupSlug, company=company)
        form.instance.type = get_object_or_404(models.MeetingType, name="Sprint Review Meeting")
        return super(MeetingSpritReviewView, self).form_valid(form)

