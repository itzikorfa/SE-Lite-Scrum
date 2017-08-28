from django.db import models
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
import logging

class Team(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("team:team_detail", kwargs={"id": self.id})

class TeamManager(models.Manager):
    use_for_related_fields = True

    @staticmethod
    def add_team_member(user, team):
        TeamMember(user=user,team=team).save()

    @staticmethod
    def remove_team_member(user, team):
        tm = TeamMember.objects.all().filter(user=user, team=team)
        if len(tm):
            tm.delete()

    @staticmethod
    def is_team_member(user, team):
        tm = TeamMember.objects.all().filter(user=user, team=team)
        if len(tm):
            return True
        return False

    @staticmethod
    def get_all_member(team):
        print("getting all members of "+str(team))
        return TeamMember.objects.all().filter(team=team)

    @staticmethod
    def get_all_teams(user):
        return TeamMember.objects.all().filter(user=user)


class TeamMember(models.Model):
    user = models.ForeignKey(User)
    team = models.ForeignKey(Team)
    objects = TeamManager()

    def __str__(self):
        return "{} {}".format(self.user, self.team)


