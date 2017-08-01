from django.contrib import admin
from lite_scrum.models import Company
from lite_scrum.models import ProductBackLog


# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'company_id','email','timestamp']
    list_display_links = ['email']
    list_filter = ['name', 'email','timestamp']
    search_fields = ['__str__', 'company_id','email','timestamp']
    list_editable = ['name']
    class Meta:
        model = Company


class BacklogAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'timestamp']
    list_display_links = ['company']
    list_filter = ['name', 'company']
    search_fields = ['__str__', 'company']
    list_editable = ['name']

    class Meta:
        model = ProductBackLog



admin.site.register(Company, CompanyAdmin)
admin.site.register(ProductBackLog, BacklogAdmin)
