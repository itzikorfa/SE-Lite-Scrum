from django.contrib import admin
from lite_scrum.models import Company
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'company_id','email','timestamp']
    list_display_links = ['email']
    list_filter = ['name', 'email','timestamp']
    search_fields = ['__str__', 'company_id','email','timestamp']
    list_editable = ['name']
    class Meta:
        model = Company

admin.site.register(Company, CompanyAdmin)