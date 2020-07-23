from django.contrib import admin
from .models import *

class ProductIMGInline(admin.TabularInline): # класс для отображения имг в админ
    model = ProductIMG
    extra = 0  # для админки

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

    class Meta():
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductIMGInline]

    class Meta():
        model = Product

admin.site.register(Product, ProductAdmin)

class ProductIMGAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductIMG._meta.fields]

    class Meta():
        model = ProductIMG

admin.site.register(ProductIMG, ProductIMGAdmin)





