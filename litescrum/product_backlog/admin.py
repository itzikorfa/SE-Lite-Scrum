from django.contrib import admin
from .models import ProductBackLog
class ProductBacklogAdmin(admin.ModelAdmin):
    list_display = ['name','product_owner','product']
    search_fields = ['__str__','product_owner']
    class Meta:
        model = ProductBackLog

admin.site.register(ProductBackLog,ProductBacklogAdmin)


# Register your models here.
