from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

from mainapp.models import ProductCategory, Product


# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


# def products(request, category_id=None):
#     context = {
#         'title': 'GeekShop - Каталог',
#         'categories': ProductCategory.objects.all(),
#         'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all(),
#     }
#     return render(request, 'mainapp/products.html', context)

class ProductsList(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    paginate_by = 3
    context_object_name = 'products'
    ordering = 'name'



    def get_context_data(self, **kwargs):
        context = super(ProductsList, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_queryset(self, product):

        self.queryset = product
        return self.queryset

def category_number(request, category_id=None):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    return products

product_list = ProductsList.get_queryset(category_number())

# def products(request, category_id=None, page=1):
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)
#     else:
#         products = Product.objects.all()
#     per_page = 3
#     paginator = Paginator(products.order_by('name'), per_page)
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#     context = {
#         'title': 'GeekShop - Каталог',
#         'categories': ProductCategory.objects.all(),
#         'products': products_paginator,
#     }
#     return render(request, 'mainapp/products.html', context)