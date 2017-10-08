from django.db import models
from project.models import ProjectBacklog, ProjectBacklogSettings


# Create your models here.
class Sprint(models.Model):
    name = models.CharField(max_length=150)
    start_date = models.DateField(verbose_name="from")
    # TODO: set end date automaticly
    end_date = models.DateField(verbose_name= "to", blank=True, default=start_date)
    project_backlog = models.ForeignKey(ProjectBacklog)

    def __str__(self):
        return "[{}] Sprint: {}".format(self.project_backlog, self.name)



