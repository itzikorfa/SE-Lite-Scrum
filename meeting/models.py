from django.db import models
from django.utils import timezone
from groups.models import Group
from sprint.models import Sprint
from datetime import datetime
from django.core.urlresolvers import reverse
# Create your models here.

class MeetingType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Meeting type")

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name',)


class Meeting(models.Model):
    team = models.ForeignKey(Group, related_name="teammeeting")
    type = models.ForeignKey(MeetingType, related_name="meetingtyperel")
    date = models.DateField(default=timezone.now)
    log = models.TextField()
    tasks_meta = models.CharField(max_length=200, null=True, default="")
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return '{}: {} at {}'.format(self.team, self.type, self.date)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.team.slug})


    class Meta:
        ordering = ['-update']
