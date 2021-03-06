from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from groups.models import Group,GroupMember
from accounts.models import User
from django.contrib.auth.models import User as account
from . import models
import utiles.utiles as uriles
from .forms import GroupMemberForm


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Group

    def form_valid(self, form):
        from company.models import Company
        company = get_object_or_404(Company, pk=self.kwargs.pop('pk'))
        form.instance.company = company
        return super(CreateGroup, self).form_valid(form)



class SingleGroup(generic.DetailView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user.username
        group =get_object_or_404(Group, slug=self.kwargs['slug'])
        ans, graph, analyse = uriles.create_covey_graph(group.pk)
        context['covey_analyse'] = analyse
        context['covey_graph'] = graph
        return context

class ListGroups(generic.ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(group.name)))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(group.name))

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("group:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:

            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
            ).get()

        except models.GroupMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )
        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )
        return super().get(request, *args, **kwargs)

class CreateGroupMember(generic.CreateView):
    template_name = 'groups/groupmember_form.html'
    model = GroupMember
    fields = ('user',)

    def get_form(self, form_class=None):
        form = super(CreateGroupMember, self).get_form(form_class)
        group = get_object_or_404(Group, slug=self.kwargs['slug'])
        form.fields["user"].queryset = account.objects.exclude(id__in=group.members.all())
        return form

    def form_valid(self, form):
        group = get_object_or_404(Group, slug=self.kwargs.get("slug"))
        form.instance.group = group
        # TODO: add user to company group
        user = form.instance.user
        group = Group.objects.get(name = group.company.name)
        gm, created = GroupMember.objects.get_or_create(user=user, group=group)
        return super(CreateGroupMember, self).form_valid(form)

