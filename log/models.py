from django.db import models
from task.models import TaskProperty
# Create your models here.

class Log(models.Model):
    task = models.ForeignKey(TaskProperty, related_name="log4tasks")
    log = models.TextField()
    update = models.DateTimeField(auto_now=False, auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "log for task "

