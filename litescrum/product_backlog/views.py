from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .models import ProductBackLog
from .forms import ProductBacklogForm

def product_backlog_list(request):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    queryset_backlog = ProductBackLog.objects.all()

    return render(request, "product_backlog_list.html", {
        "title": "Product Backlog List",
        "object_list": queryset_backlog
    })


def product_backlog_update(request, id=None):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(ProductBackLog, id=id)
    form = ProductBacklogForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "record updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, "product_backlog_form.html", {
        "title": "Product Backlog Update {}".format(instance.name),
        "object": instance,
        "forms": form
    })


def product_backlog_detail(request, id):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(ProductBackLog, id=id)
    return render(request, "product_backlog_details.html", {
        "title": "Detail: {}".format(instance.name),
        "object": instance
    })


def product_backlog_create(request):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    form = ProductBacklogForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "record added")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, "product_backlog_form.html", {
        "title": "Create Product Backlog",
        "forms": form
    })


def product_backlog_delete(request, id=None):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(ProductBackLog, id=id)
    instance.delete()
    messages.success(request, "record deleted")
    return redirect("backlog:backlog_list")

