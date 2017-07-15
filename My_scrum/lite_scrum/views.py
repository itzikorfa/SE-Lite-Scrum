from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CompnyForm, BacklogForm, UserForm, GroupForm
from .models import Backlog
from .models import Company


# Create your views here.

def add_group(request):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    form = GroupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "record added")
        return HttpResponseRedirect("home.html")
    return render(request, "registration/add_user.html", {
        "title": "Create Group",
        "forms": form
    })

def add_user(request):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    form = UserForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        login(instance)
        messages.success(request, "record added")
        return HttpResponseRedirect("home.html")
    return render(request, "registration/add_user.html", {
        "title": "Create User",
        "forms": form
    })
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         new_user = User.objects.create_user(**form.cleaned_data)
    #         login(new_user)
    #         # redirect, or however you want to get to the main view
    #         return HttpResponseRedirect('main.html')
    # else:
    #     form = UserForm()
    #
    # return render(request, 'registration/add_user.html', {
    #     'title': "Add User",
    #     'form': form
    # })


def company_list(request):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    queryset_company = Company.objects.all()

    return render(request, "company_list.html ", {
        "title": "Company List",
        "object_list": queryset_company
    })

def company_update(request,id=None):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    print("in update")
    instance = get_object_or_404(Company, id=id)
    print(instance)
    form = CompnyForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "record updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, "company_form.html", {
        "title": "Company List",
        "object": instance,
        "forms": form
    })

def company_detail(request,id):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(Company, id = id)
    backlog = Backlog.objects.filter(company=id)

    return render(request, "company_details.html", {
        "title": "Company List",
        "object": instance,
        "backlog": backlog
    })

def company_create(request):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    form = CompnyForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "record added")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request,"company_form.html",{
        "title": "Company create",
        "forms": form
    })



def company_delete(request,id=None):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(Company, id=id)
    instance.delete()
    messages.success(request, "record deleted")
    return redirect("company:company_list")


def backlog_list(request):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    queryset_backlog = Backlog.objects.all()

    return render(request, "backlog_list.html", {
        "title": "Backlog List",
        "object_list": queryset_backlog
    })


def backlog_update(request, id=None):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(Backlog, id=id)
    form = BacklogForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "record updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, "backlog_form.html", {
        "title": "Backlog Update {}".format(instance.name),
        "object": instance,
        "forms": form
    })


def backlog_detail(request, id):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(Backlog, id=id)
    return render(request, "backlog_details.html", {
        "title": "Detail: {}".format(instance.name),
        "object": instance
    })


def backlog_create(request):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    form = BacklogForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "record added")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, "backlog_form.html", {
        "title": "Company create",
        "forms": form
    })


def backlog_delete(request, id=None):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(Backlog, id=id)
    instance.delete()
    messages.success(request, "record deleted")
    return redirect("backlog:backlog_list")
