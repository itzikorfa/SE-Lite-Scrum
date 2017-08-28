from django.contrib import admin
from company.models import Company
from product.models import Product


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'company_id','email','timestamp']
    list_display_links = ['email']
    list_filter = ['name', 'email','timestamp']
    search_fields = ['__str__', 'company_id','email','timestamp']
    list_editable = ['name']
    class Meta:
        model = Company


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','company','description','timestamp']
    search_fields = ['__str__', 'company', 'description', 'timestamp']
    class Meta:
        model = Product

admin.site.register(Company, CompanyAdmin)
admin.site.register(Product, ProductAdmin)