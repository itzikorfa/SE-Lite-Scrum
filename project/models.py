from django.db import models
from company.models import Company
from django.core.urlresolvers import reverse
from groups.models import Group
from django.contrib.auth.models import User
from datetime import timedelta, datetime
from django.core.validators import MinValueValidator,MaxValueValidator,MaxLengthValidator,MinLengthValidator
from django.utils import timezone

class Project(models.Model):
    company = models.ForeignKey(Company, related_name='projects')
    name = models.CharField(max_length=250)
    description = models.TextField(default='', blank=True)
    update = models.DateTimeField(auto_now=False, auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "[{}] {}".format(self.company, self.name)


    def get_absolute_url(self):
        return reverse("project:detail",kwargs={'pk':self.pk})


    class Meta:
        unique_together = ('name', 'company')


class ProjectBacklog(models.Model):
    project = models.OneToOneField(Project, related_name="projectBacklog")
    ETA = models.DateField()
    project_owner = models.ForeignKey(User, related_name="projectBacklogOwner")
    scrum_master = models.ForeignKey(User, related_name="projectBacklogSM")
    start_date = models.DateField(verbose_name='start date', default=timezone.now)
    def __str__(self):
        return "{} ETA: {} (owner: {})".format(self.project,self.ETA,self.project_owner)

    def get_absolute_url(self):
        return reverse("project:detail",kwargs={'pk':self.project.pk})


class ProjectBacklogSettings(models.Model):
    project_backlog = models.OneToOneField(ProjectBacklog, related_name="projectBacklogSetting")
    sprint_length = models.IntegerField(verbose_name="Sprint length",
                                       validators=[MinValueValidator(0)],default=14)
    sprint_template = models.CharField(max_length=15, default='sprint_', blank=True)

    def __str__(self):
        return "{} length {}".format(self.project_backlog.project.name , self.sprint_length)

    def get_absolute_url(self):
        return reverse("project:detail",kwargs={'pk':self.project_backlog.project.pk})

    def save(self, *args, **kwargs):
        # self.create_sprints()
        super().save(*args, **kwargs)

class TaskStages(models.Model):
    stage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=1
                                ,verbose_name="stage id", unique=True)
    stage_name = models.CharField(max_length=25, validators=[MinLengthValidator(2)], verbose_name="stage name",
                                  unique=True)

    def __str__(self):
        return "[{}] {}".format(self.stage, self.stage_name)

    class Meta:
        ordering=('stage',)


class ProjeckBacklogStages(models.Model):
    project_backlog = models.ForeignKey(ProjectBacklogSettings,
                                        related_name='stagestoProjectBacklog')
    stage = models.ForeignKey(TaskStages, related_name='stagestoTaskStages')

    def __str__(self):
        return "{}-->{}".format(self.project_backlog, self.stage)

    class Meta:
        unique_together = ('project_backlog','stage')