from django.db import models
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from company.models import Company

class Product (models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Product: {}".format(self.name)

    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={"id": self.id})