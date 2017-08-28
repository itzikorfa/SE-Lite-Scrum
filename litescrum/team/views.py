from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Team, TeamMember
from product.models import Product
from .forms import TeamForm
import logging


def team_list(request):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    queryset_team = Team.objects.all()

    return render(request, "team_list.html ", {
        "title": "Team List",
        "object_list": queryset_team
    })

def team_update(request,id=None):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    print("in update")
    instance = get_object_or_404(Team, id=id)
    print(instance)
    form = Team(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "record updated")
        logging.info("record updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, "team_form.html", {
        "title": "Team Update",
        "object": instance,
        "forms": form
    })

def team_detail(request,id):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(Team, id = id)
    tm = TeamMember.objects.get_all_member(team=instance)

    return render(request, "team_details.html", {
        "title": "Team detail",
        "object": instance,
        "team_member": tm
    })


def team_create(request):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    form = TeamForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "record added")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request,"team_form.html",{
        "title": "Team create",
        "forms": form
    })



def team_delete(request,id=None):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(Team, id=id)
    instance.delete()
    messages.success(request, "record deleted")
    return redirect("team:team_list")
