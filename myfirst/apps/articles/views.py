from django.shortcuts import render
from products.models import ProductIMG


def home(request):
    session_key = request.session.session_key
    total_product_images = ProductIMG.objects.count()
    products_images = ProductIMG.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_surgeries = products_images.filter(product__product_category__id=1)
    products_images_cosmetics = products_images.filter(product__product_category__id=2)

    return render(request, "articles/home.html", locals())


def detail(request):  # article_id - то,что поймает django в запрошенном id

    return render(request, "articles/detail.html", locals())


def sections(request):
    products_images = ProductIMG.objects.filter(is_active=True, is_main=True, product__is_active=True)
    return render(request, "articles/sections.html/", locals())


def surgery_section(request):
    products_images = ProductIMG.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_surgeries = products_images.filter(product__product_category__id=1)
    return render(request, "articles/surgery.html", locals())


def cosmetics_section(request):
    products_images = ProductIMG.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_cosmetics = products_images.filter(product__product_category__id=2)
    return render(request, "articles/cosmetics.html", locals())


def about_us(request):

    return render(request, "articles/about.html", locals())


def contacts(request):

    return render(request, "articles/contacts.html", locals())