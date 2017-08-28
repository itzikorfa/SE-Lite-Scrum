from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Company
from product.models import Product
from .forms import CompnyForm
import logging
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
        logging.info("record updated")
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
