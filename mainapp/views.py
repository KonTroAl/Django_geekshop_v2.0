from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

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
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductsList, self).get_context_data(**kwargs)
        context['categories'] = categories
        return context

    def get_queryset(self):
        try:
            self.category_id = get_object_or_404(ProductCategory, id=self.kwargs['pk'])
            return Product.objects.filter(category_id=self.category_id)
        except KeyError:
            return Product.objects.all()


categories = ProductCategory.get_all()

products = Product.objects.all()

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