from django import forms
from project.models import ProjectBacklog
from django.contrib.admin import widgets
from bootstrap_datepicker.widgets import DatePicker
#
# class ProjectBacklogForm(forms.ModelForm):
#
#     class Meta:
#         model = ProjectBacklog
#         fields = ("ETA", 'start_date', "project_owner", 'scrum_master')
#         widgets = {
#             'ETA': DatePicker(
#             options={
#                 "format": "mm/dd/yyyy",
#                 "autoclose": True
#             }),
#
#             'start_date': DatePicker(
#             options={
#                 "format": "mm/dd/yyyy",
#                 "autoclose": True
#             }),
#
#         }
#
#
