from django.db import models
from company.models import Company
from django.core.urlresolvers import reverse
from groups.models import Group
from accounts.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Project(models.Model):
    company = models.ForeignKey(Company, related_name='projects')
    name = models.CharField(max_length=250)
    description = models.TextField(default='', blank=True)
    update = models.DateTimeField(auto_now=False, auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "[{}] {}".format(self.company, self.name)


    def get_absolute_url(self):
        return reverse("project:detail",kwargs={'pk':self.pk})


class ProjectBacklog(models.Model):
    project = models.OneToOneField(Project, related_name="projectBacklog")
    ETA = models.DateField()
    project_owner = models.ForeignKey(User, related_name="projectBacklogOwner")
    scrum_master = models.ForeignKey(User, related_name="projectBacklogSM")

    def __str__(self):
        return "{} ETA: {} (owner: {})".format(self.project,self.ETA,self.project_owner)

class ProjectBacklogSettings(models.Model):
    project_backlog = models.OneToOneField(ProjectBacklog, related_name="projectBacklogSetting")
    sprint_length = models.IntegerField(verbose_name="Sprint length",
                                       validators=[MinValueValidator(0)],default=14)

    def __str__(self):
        return "{} length {}".format(self.project_backlog.project.name , self.sprint_length)
