from django.db import models


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=64,blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return " %s " % self.category_name

    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"


class Product(models.Model):
    product_name = models.TextField(max_length=200, blank=True, null=True, default=None)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    product_category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    short_product_description = models.CharField(max_length=120, blank=True, null=True, default=None)
    product_description = models.TextField(max_length=500, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " %s %s" % (self.product_price, self.product_name)

    class Meta:
        verbose_name = "Изделие"
        verbose_name_plural = "Изделия"


class ProductIMG(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products_images")
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " %s " % self.id

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"
