from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CompnyForm, ProductBacklogForm, UserForm, GroupForm,ProductForm
from .models import ProductBackLog
from .models import Company, Product


# Create your views here.
#
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
    product = Product.objects.filter(company=id)

    return render(request, "company_details.html", {
        "title": "Company detail",
        "object": instance,
        "product": product
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
        "title": "Company create",
        "forms": form
    })


def product_backlog_delete(request, id=None):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(ProductBackLog, id=id)
    instance.delete()
    messages.success(request, "record deleted")
    return redirect("backlog:backlog_list")

def product_list(request):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    queryset_product = Product.objects.all()

    return render(request, "product_list.html", {
        "title": "Product List",
        "object_list": queryset_product
    })


def product_detail(request, id):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(Product, id=id)
    return render(request, "product_details.html", {
        "title": "Detail: {}".format(instance.name),
        "object": instance
    })


def product_create(request):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    form = ProductForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "record added")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, "product_form.html", {
        "title": "Create Product",
        "forms": form
    })


def product_delete(request, id=None):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(Product, id=id)
    instance.delete()
    messages.success(request, "record deleted")
    return redirect("product:product_list")

def product_update(request, id=None):
    if not request.user.is_authenticated():
        return HttpResponse("<h1>not loggin</h1>")
    instance = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=instance)
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