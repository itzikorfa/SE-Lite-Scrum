from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from company.models import Company
from django.core.validators import ValidationError
# from accounts.models import User

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()

"""
Group class that unite all the users 
"""

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="GroupMember")
    company = models.ForeignKey(Company, related_name="groupcompany")

    class Meta:
        unique_together= ('name', 'company')
        ordering = ('name')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})


    class Meta:
        ordering = ["name"]

"""
Many to many relations
"""
class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name="memberships")
    user = models.ForeignKey(User,related_name='user_groups')

    def __str__(self):
        return self.user.username

    # def validate_unique(self, *args, **kwargs):
    #     super(GroupMember, self).validate_unique(*args, **kwargs)
    #     tmp =GroupMember.objects.filter(group=self.group, user=self.user)
    #     if len(tmp)>0:
    #         raise ValidationError({'user': ['user must be unique per group', ]})



    class Meta:
        unique_together = ("group", "user")

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.group.slug})

