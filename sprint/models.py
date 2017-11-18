from django.db import models
from project.models import ProjectBacklog
from datetime import datetime, timedelta
from django.core.urlresolvers import reverse


# Create your models here.
PROJECT = "sprint_project"


class Sprint(models.Model):
    name = models.CharField(max_length=150)
    start_date = models.DateField(verbose_name="from")
    # TODO: set end date automaticly
    end_date = models.DateField(verbose_name= "to", blank=True, null=True)
    project_backlog = models.ForeignKey(ProjectBacklog, related_name=("%s" % PROJECT))

    def __str__(self):
        return "{} {} -> {}".format(
            self.name, self.start_date,self.end_date
            )

    def get_absolute_url(self):
        return reverse("sprint:list")

    def is_current_sprint(self):
        if datetime.today().date() >= self.start_date and \
            datetime.today().date() <= self.end_date:
            return True
        return False




    class Meta:
        unique_together = ('name','project_backlog')






    # def create_sprints(self, project_backlog):
    #     end_date= datetime.now()
    #     counter = 1
    #     while project_backlog.ETA > end_date:
    #         tmp = Sprint()
    #         tmp.name = sprint_template+str(counter)
    #         tmp.start_date=end_date
    #         tmp.end_date = tmp.start_date + timedelta(sprint_length)
    #         tmp.project_backlog=project_backlog
    #         tmp.save()
    #         end_date = tmp.end_date
    #
