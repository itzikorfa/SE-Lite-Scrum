from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()


class ProjectsList(SelectRelatedMixin, generic.ListView):
    model = models.Projects
    select_related = ("company", "group")


class ProjectsDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Projects
    select_related = ("company", "group")



