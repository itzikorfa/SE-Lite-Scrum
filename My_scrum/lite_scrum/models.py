from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import MaxValueValidator, MinValueValidator

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

class Product (models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Product: {}".format(self.name)
    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={"id": self.id})

class ProductBackLog(models.Model):
    company = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    product_owner = models.ForeignKey(User, default=1,related_name='%(class)s_product_owner')
    group = models.ForeignKey(Group, default=1,related_name='%(class)s_product_owner')

    def __str__(self):
        return "{} | {}".format(self.company, self.name)

    def get_absolute_url(self):
        return reverse("backlog:backlog_detail", kwargs={"id": self.id})

class UserStory(models.Model):
    backlog = models.ForeignKey(ProductBackLog, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField()
    priority = models.IntegerField(default=5 ,
                                   validators=[MaxValueValidator(10),
                                               MinValueValidator(0)])
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}({})".format(self.name, self.priority)


class TeamMembers(models.Model):
        userstory = models.ForeignKey(UserStory,on_delete=models.CASCADE)
        user = models.ForeignKey(User,on_delete=models.CASCADE)

        def __str__(self):
            return "{}:{}".format(self.userstory,self.user)
