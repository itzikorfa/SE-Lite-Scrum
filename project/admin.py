from django.contrib import admin
from .models import *
admin.site.register(Project)
admin.site.register(ProjectBacklog)
admin.site.register(ProjectBacklogSettings)
admin.site.register(TaskStages)
admin.site.register(ProjeckBacklogStages)

# Register your models here.
