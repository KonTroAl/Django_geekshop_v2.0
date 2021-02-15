from django.urls import path

from mainapp.views import ProductsList

app_name = 'mainapp'

urlpatterns = [
    path('', ProductsList.as_view(), name='index'),
    path('<int:category_id>/', ProductsList.as_view(), name='product'),
    path('<int:category_id>/<int:page>/', ProductsList.as_view(), name='category'),
    path('page/<int:page>/', ProductsList.as_view(), name='page'),
]