from django.db import models
from django.core.urlresolvers import reverse
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