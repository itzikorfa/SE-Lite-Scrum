from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model
from django import template

user = get_user_model()
register = template.Library()



class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    update = models.DateTimeField(auto_now=False, auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("company:single", kwargs={"pk": self.pk})
