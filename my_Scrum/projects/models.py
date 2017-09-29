from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from company.models import Company
from groups.models import Group
import datetime
import misaka

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(blank=True, default='')
    slug = models.SlugField(allow_unicode=True, unique=True)
    company = models.ForeignKey(Company, related_name="projects")
    ETA = models.DateField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated  = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "[{}] {}".format(self.company, self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("projects:single", kwargs={"pk": self.pk})