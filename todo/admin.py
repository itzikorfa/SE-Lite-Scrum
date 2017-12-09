from django.contrib import admin
from .models import Todo
# Register your models here.
class MyAdmin(admin.ModelAdmin):
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.user = user
        instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance



admin.site.register(Todo,MyAdmin)