from django.shortcuts import render



# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'product' : [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': '6 090,00 руб.',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                'picture': '/static/vendor/img/products/Adidas-hoodie.png',
                'button': 'Отправить в корзину',
                'button_class': 'btn btn-outline-success'
            },

            {
                'name': 'Синяя куртка The North Face',
                'price': '23 725,00 руб.',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                'picture': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                'button': 'Удалить из корзины',
                'button_class': 'btn btn-outline-danger'
            },

            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': '3 390,00 руб.',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                'picture': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'button': 'Отправить в корзину',
                'button_class': 'btn btn-outline-success'
            },

            {
                'name': 'Черный рюкзак Nike Heritage',
                'price': '2 340,00 руб.',
                'description': 'Плотная ткань. Легкий материал.',
                'picture': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
                'button': 'Отправить в корзину',
                'button_class': 'btn btn-outline-success'
            },

            {
                'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'price': '13 590,00 руб.',
                'description': 'Гладкий кожаный верх. Натуральный материал.',
                'picture': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
                'button': 'Отправить в корзину',
                'button_class': 'btn btn-outline-success'
            },

            {
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'price': '2 890,00 руб.',
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                'picture': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'button': 'Отправить в корзину',
                'button_class': 'btn btn-outline-success'
            }
        ]
    }
    return render(request, 'mainapp/products.html', context)
