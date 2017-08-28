from django.db import models
from product.models import Product
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse

class ProductBackLog(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, default=product.name)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    product_owner = models.ForeignKey(User, default=1,related_name='%(class)s_product_owner')
    group = models.ForeignKey(Group, default=1,related_name='%(class)s_product_owner')

    def __str__(self):
        return "{} | {}".format(self.product, self.name)

    def get_absolute_url(self):
        return reverse("product_backlog:product_backlog_detail", kwargs={"id": self.id})