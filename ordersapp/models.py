from django.db import models

from django.conf import settings
from mainapp.models import Product
from django.db.models import F

# Create your models here.

class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен в обработку'),
        (PAID, 'оплачен'),
        (PROCEEDED, 'обрабатывается'),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменен'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='updated', auto_now=True)
    status = models.CharField(verbose_name='status', max_length=3, choices=ORDER_STATUS_CHOICES, default=FORMING)
    is_active = models.BooleanField(verbose_name='active', default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return 'Active Order: {}'.format(self.id)

    def get_total_quantity(self):
        order_items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, order_items)))

    def get_product_type_quantity(self):
        order_items = self.orderitems.select_related()
        return len(order_items)

    def get_total_cost(self):
        order_items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity * x.product.price, order_items)))

    def delete(self):
        for order_item in self.orderitems.select_related():
            order_item.product.quantity = F('quantity') + order_item.quantity
            order_item.product.save()

        self.is_active = False
        self.save()

    def get_summary(self):
        items = self.orderitems.select_related()
        total_cost = sum(list(map(lambda x: x.product_cost(), items)))
        total_quantity = sum(list(map(lambda x: x.quantity, items)))
        return {
            'total_cost': total_cost,
            'total_quantity': total_quantity,
        }

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE)

    product = models.ForeignKey(Product, verbose_name='product', on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)

    def product_cost(self):
        return self.product.price * self.quantity
