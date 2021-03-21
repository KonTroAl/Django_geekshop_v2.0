from django.urls import path, re_path

from ordersapp import views

app_name = 'ordersapp'

urlpatterns = [
    path('', views.OrderList.as_view(), name='order_list'),
    path('forming/complete/<int:pk>/', views.order_forming_complete, name='order_forming_complete'),
    path('create/', views.OrderItemsCreate.as_view(), name='order_create'),
    path('read/<int:pk>/', views.OrderRead.as_view(), name='order_read'),
    path('update/<int:pk>/', views.OrderItemsUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', views.OrderDelete.as_view(), name='order_delete'),
]