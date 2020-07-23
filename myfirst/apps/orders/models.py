from django.db import models
from products.models import Product
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=28, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s " % self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_adress = models.CharField(max_length=120, blank=True, null=True, default=None)
    comments = models.TextField(max_length=500, blank=True, null=True, default=None)
    price_in_total = models.DecimalField(max_digits=10, decimal_places=2, default=0) # for all products in total
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s " % (self.id, self.status.name)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(blank=True, null=True, default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_in_total = models.DecimalField(max_digits=10, decimal_places=2, default=0) # PIT * amount
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Товар %s " % self.product.product_name

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def save(self, *args, **kwargs): # шаблон для переопределения метода save чтобы переопределять собственные поля
        price_per_item = self.product.product_price
        self.price_per_item = price_per_item

        self.price_in_total = self.amount * price_per_item

        order = self.order
        all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

        order_total_price = 0
        for item in all_products_in_order:
            order_total_price += item.price_in_total

        self.order.price_in_total = order_total_price
        self.order.save(force_update=True)

        super(ProductInOrder, self).save(*args, **kwargs)


def Pr_in_Order_post_save(instance, sender, **kwargs): # обращение через instance(сущность: сохраняется значение в бд) вместо self
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.price_in_total

    instance.order.price_in_total = order_total_price
    instance.order.save(force_update=True)


post_save.connect(Pr_in_Order_post_save, sender=ProductInOrder)


class ProductInCart(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(blank=True, null=True, default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_in_total = models.DecimalField(max_digits=10, decimal_places=2, default=0) # PIT * amount
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Товар %s " % self.product.product_name

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

    def save(self, *args, **kwargs):
        price_per_item = self.product.product_price
        self.price_per_item = price_per_item
        self.price_in_total = int(self.amount) * price_per_item

        super(ProductInCart, self).save(*args, **kwargs)
