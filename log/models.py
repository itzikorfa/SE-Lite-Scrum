from django.db import models
from task.models import TaskProperty
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
"""
Log class that represents the log of the task and help monitor the task progress
"""
class Log(models.Model):
    task = models.ForeignKey(TaskProperty, related_name="log4tasks")
    log = models.TextField()
    presentage_complete = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name="%completed", default=0)
    time_spent = models.IntegerField(
        validators=[ MinValueValidator(0)], default=0, verbose_name="number of hours")
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "log for task "

    def get_absolute_url(self):
        return reverse("task:detail", kwargs={"pk": self.task.task.pk})