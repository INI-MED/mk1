from django.shortcuts import render
from products.models import ProductIMG


def home(request):
    session_key = request.session.session_key
    products_images = ProductIMG.objects.all()[:4]
    products_images_surgeries = ProductIMG.objects.filter(product__product_category__id=1).all()[:4]
    products_images_cosmetics = ProductIMG.objects.filter(product__product_category__id=2).all()[:4]

    return render(request, "articles/home.html",  locals())


def detail(request):  # article_id - то,что поймает django в запрошенном id

    return render(request, "articles/detail.html", locals())


def sections(request):
    products_images = ProductIMG.objects.all()
    return render(request, "articles/sections.html/", locals())


def surgery_section(request):
    products_images_surgeries = ProductIMG.objects.filter(product__product_category__id=1)
    #products_images_surgeries = products_images.filter(product__product_category__id=1)
    return render(request, "articles/surgery.html", locals())


def cosmetics_section(request):
    products_images_cosmetics = ProductIMG.objects.filter(product__product_category__id=2)
    #products_images_cosmetics = products_images.filter(product__product_category__id=2)
    return render(request, "articles/cosmetics.html", locals())


def about_us(request):

    return render(request, "articles/about.html", locals())


def contacts(request):

    return render(request, "articles/contacts.html", locals())