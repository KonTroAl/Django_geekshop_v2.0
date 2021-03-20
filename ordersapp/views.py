from django.shortcuts import render
from django.urls import reverse_lazy
from django.forms import inlineformset_factory

from django.views.generic import ListView, CreateView

from ordersapp.models import Order, OrderItem
from ordersapp.forms import OrderForm, OrderItemForm

# Create your views here.

class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderItemsCreate(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('ordersapp:order_list')

    def get_context_data(self, **kwargs):
        data = super(OrderItemsCreate, self).get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)

        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            formset = OrderFormSet()

        data['orderitems'] = formset
        return data
