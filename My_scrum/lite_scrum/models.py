from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=40)
    company_id = models.CharField(max_length=30)
    email = models.EmailField()
    timestamp  = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
        return reverse("company:company_detail", kwargs={"id": self.id})

    def __str__(self):
        return self.name


class Backlog(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    product_backlog = models.BooleanField(default=True)
    release_backlog = models.BooleanField(default=False)
    product_owner = models.ForeignKey(User, default=1,related_name='%(class)s_product_owner')
    scrum_master = models.ForeignKey(User, default=1,related_name='%(class)s_scrum_master')

    def __str__(self):
        return "{} | {}".format(self.company, self.name)

    def get_absolute_url(self):
        return reverse("backlog:backlog_detail", kwargs={"id": self.id})
