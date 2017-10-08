from django.contrib import admin
from .models import Project, ProjectBacklog, ProjectBacklogSettings
admin.site.register(Project)
admin.site.register(ProjectBacklog)
admin.site.register(ProjectBacklogSettings)
# Register your models here.
