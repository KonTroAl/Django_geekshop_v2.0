from django.urls import path

from adminapp import views

app_name = 'adminapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_users_read/', views.admin_users_read, name='admin_users_read'),
    path('admin_users_create/', views.admin_users_create, name='admin_users_create'),
]