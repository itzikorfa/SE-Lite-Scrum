from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from project.models import ProjectBacklog
from sprint.models import Sprint
from groups.models import Group
from accounts.models import User
# Create your models here.


class Task(models.Model):
    projectBacklog = models.ForeignKey(ProjectBacklog, related_name="tasksInBacklogs")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    priority = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    is_sub_task = models.BooleanField(default=False)
    parent_task = models.ForeignKey('Task', blank=True, null=True,related_name="parent")
    link_task = models.ForeignKey('Task', blank=True, null=True, related_name="link")
    team = models.ForeignKey(Group, blank=True, null=True, related_name="group", verbose_name="scrum")
    task_completed = models.BooleanField(default=False)

    def __str__(self):
        return "Task {}".format(self.name)


class TaskProperty(models.Model):
    task = models.OneToOneField(Task, related_name="taskProperty")
    sprint = models.ForeignKey(Sprint, related_name="taskSprint")
    assign_to = models.ForeignKey(User, related_name="assignTo")
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(blank=True, null= True)


    def __str__(self):
        if self.end_date:
            return "{}: {}-{}".format(self.task,self.start_date, self.end_date)
        else:
            return "{}: start at {} still in progress".format(self.task, self.start_date)


