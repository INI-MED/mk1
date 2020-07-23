
from django.urls import path
from django.conf.urls import url

from . import views  # . means local library


urlpatterns = [
    url(r"^cart_adding/$", views.cart_adding, name="cart_adding"),
    url(r"^checkout/$", views.checkout, name="checkout"),
    #url(r"^cartpage/$", views.cartpage, name="cartpage"),
]








