from products.models import Product
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import *
from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.contrib.auth.models import User


def cart_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST

    product_id = data.get("product_id")
    amount = data.get("amount")
    is_delete = data.get("is_delete")

    if is_delete == "true":
        ProductInCart.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInCart.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                   is_active=True, defaults={"amount": amount})
        if not created:
            new_product.amount += int(amount)
            new_product.save(force_update=True)

    # общий случай обработки 2 случаев
    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    products_total_num = products_in_cart.count()

    return_dict["products_total_num"] = products_total_num
    return_dict["products"] = list()

    for item in products_in_cart:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["product_name"] = item.product.product_name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["amount"] = item.amount
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)


def checkout(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True, order__isnull=True)

    products_total_num = products_in_cart.count()
    for item in products_in_cart:
        print(item.order)

        form = CustomerForm(request.POST or None)
        if request.POST:
            # print(request.POST)
            if form.is_valid():
                data = request.POST
                name = data["name"]
                phone = data["phone"]
                adress = data["adress"]

                user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})

                order = Order.objects.get_or_create(user=user, customer_name=name,
                                                    customer_phone=phone, customer_adress=adress, status_id=1)

                print(order, "meh")

                for name, value in data.items():
                    if name.startswith("product_in_cart_"):
                        product_in_cart_id = name.split("product_in_cart_")[1]
                        product_in_cart = ProductInCart.objects.get(id=product_in_cart_id)

                        product_in_cart.amount = value
                        product_in_cart.order = order
                        product_in_cart.form.save(force_update=True)
                        ProductInOrder.objects.get(product=product_in_cart.product,
                                                   amount=product_in_cart.amount,
                                                   price_per_item=product_in_cart.price_per_item,
                                                   price_in_total=product_in_cart.price_in_total,
                                                   order=order)

                return HttpResponseRedirect("/detail", request.META["HTTP_REFERER"])

        return render(request, "orders/checkout.html", locals())