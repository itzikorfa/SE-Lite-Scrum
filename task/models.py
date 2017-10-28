from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from project.models import ProjectBacklog,ProjeckBacklogStages
from sprint.models import Sprint
from groups.models import Group
from covey.models import CoveyMatrix
from django.contrib.auth import get_user_model
# Create your models here.
from django.core.urlresolvers import reverse
User = get_user_model()


class Task(models.Model):
    projectBacklog = models.ForeignKey(ProjectBacklog, related_name="tasksInBacklogs")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    priority = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    task_type = models.ForeignKey(CoveyMatrix, default=2, related_name="taskcovmat" )
    is_sub_task = models.BooleanField(default=False)
    parent_task = models.ForeignKey('Task', blank=True, null=True,related_name="parent")
    link_task = models.ForeignKey('Task', blank=True, null=True, related_name="link")
    team = models.ForeignKey(Group, blank=True, null=True, related_name="group", verbose_name="Team")
    presentage_complete = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(0)], verbose_name="%completed", default=0)
    task_completed = models.BooleanField(default=False)
    estimated_time =models.IntegerField(validators=[MinValueValidator(0)])
    acutal_time = models.IntegerField(blank=True,null=True ,validators=[MinValueValidator(0)])




    def __str__(self):
        return "Task {}".format(self.name)

    def get_absolute_url(self):
        return reverse("task:detail" ,kwargs={'pk':self.pk})


class TaskProperty(models.Model):
    task = models.OneToOneField(Task, related_name="taskProperty")
    sprint = models.ForeignKey(Sprint, related_name="taskSprint")
    assign_to = models.ForeignKey(User, related_name="assignTo")
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(blank=True, null= True)
    task_stage = models.ForeignKey(ProjeckBacklogStages, related_name="taskStage"
                                   ,default=0)


    def __str__(self):
        if self.end_date:
            return "{}: {}-{}".format(self.task,self.start_date, self.end_date)
        else:
            return "{}: start at {} still in progress".format(self.task, self.start_date)


    def get_absolute_url(self):
        return reverse("task:detail" ,kwargs={'pk':self.task.pk})
