import products.models
from django.shortcuts import render
from .forms import ProductForm
from products.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)
    form = ProductForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            data = request.POST
            print("TRUE")
    return render(request, "products/product.html", locals())
