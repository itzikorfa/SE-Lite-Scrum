from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=40, unique=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("company:detail",kwargs={'pk':self.pk})

    class Meta:
        ordering = ['name']