from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from .models import User
from task.models import Task
from todo.models import Todo
class SignUp(LoginRequiredMixin,CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"


class UserInfo(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/user_tasks_list.html'
    context_object_name = "objects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(taskProperty__assign_to__username = self.kwargs['username'])
        context['todos'] = Todo.objects.filter(user__username = self.kwargs['username'])

        return context


