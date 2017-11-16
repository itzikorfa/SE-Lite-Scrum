from django.db import models
from django.utils import timezone
from groups.models import Group
from sprint.models import Sprint
from datetime import datetime
# Create your models here.

class MeetingType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Meeting type")

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name',)


class Meeting(models.Model):
    team = models.ForeignKey(Group, related_name="teammeeting")
    sprint  = models.ForeignKey(Sprint, related_name="meetingSprint")
    type = models.ForeignKey(MeetingType, related_name="meetingtyperel")
    date = models.DateField(default=timezone.now)
    log = models.TextField()
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return '{}: {} at {}'.format(self.team, self.type, self.date)


    class Meta:
        ordering = ['-date','type']
