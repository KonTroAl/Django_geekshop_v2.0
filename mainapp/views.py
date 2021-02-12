from django.shortcuts import render

from mainapp.models import ProductCategory, Product


# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
