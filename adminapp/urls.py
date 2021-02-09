from django.urls import path

from adminapp import views

app_name = 'adminapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_users_read/', views.admin_users_read, name='admin_users_read'),
    path('admin_users_create/', views.admin_users_create, name='admin_users_create'),
    path('admin_users_update/<int:id>/', views.admin_users_update, name='admin_users_update'),
    path('admin_users_delete/<int:id>/', views.admin_users_delete, name='admin_users_delete'),
]