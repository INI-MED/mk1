from django.contrib import admin
from .models import *

class ProductInOrdrerInline(admin.TabularInline):
    model = ProductInOrder
    extra = 1


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta():
        model = Status

admin.site.register(Status, StatusAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrdrerInline]

    class Meta():
        model = Order

admin.site.register(Order, OrderAdmin)

class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta():
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)

class ProductInCartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInCart._meta.fields]

    class Meta():
        model = ProductInCart

admin.site.register(ProductInCart, ProductInCartAdmin)





