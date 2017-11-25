from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=40, unique=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("company:detail",kwargs={'pk':self.pk})

    # def save(self, *args, **kwargs):
    #     from groups.models import Group, GroupMember
    #     obj = super(MyModelForm, self).save(*args, **kwargs)
    #     if self.request:
    #         user = self.request.user
    #         group , create = Group.objects.get_or_create(name=self.name, company= self)
    #         gm , create = GroupMember.objects.get_or_create(group=group, )


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        from groups.models import Group, GroupMember
        super(Company, self).save(force_insert=force_insert, force_update=force_update, using=using,
             update_fields=update_fields)
        group , create = Group.objects.get_or_create(name=self.name, company= self)
        gm , create = GroupMember.objects.get_or_create(group=group, user=self.owner)


    class Meta:
        ordering = ['name']