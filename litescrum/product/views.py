from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ProductForm

from .models import Product
# Create your views here.
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