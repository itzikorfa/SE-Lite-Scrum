from django.db import models
from task.models import TaskProperty
from django.core.urlresolvers import reverse
# Create your models here.

class Log(models.Model):
    task = models.ForeignKey(TaskProperty, related_name="log4tasks")
    log = models.TextField()
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "log for task "

    def get_absolute_url(self):
        return reverse("task:detail", kwargs={"pk": self.task.task.pk})