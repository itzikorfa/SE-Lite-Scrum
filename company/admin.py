from django.contrib import admin
from .models import Company
from groups.models import GroupMember, Group

class CompanyAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        super(CompanyAdmin, self).save_model(request, obj, form, change)
        group, create = Group.objects.get_or_create(name=self.name, company=self)
        user = request.user
        gm, create = GroupMember.objects.get_or_create(group=group, user=user.pk)
        print(gm, create,user   )


# Register your models here.
admin.site.register(Company,CompanyAdmin)