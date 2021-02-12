from django.urls import path

from adminapp import views

app_name = 'adminapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_users_read/', views.UserListView.as_view(), name='admin_users_read'),
    path('admin_users_create/', views.UserCreateView.as_view(), name='admin_users_create'),
    path('admin_users_update/<int:pk>/', views.UserUpdateView.as_view(), name='admin_users_update'),
    path('admin_users_delete/<int:pk>/', views.UserDeleteView.as_view(), name='admin_users_delete'),
    path('admin_users_recover/<int:id>/', views.admin_users_recover, name='admin_users_recover'),
    path('admin_category_read/', views.admin_category_read, name='admin_category_read'),
    path('admin_category_create/', views.admin_category_create, name='admin_category_create'),
    path('admin_сategory_update/<int:id>/', views.admin_category_update, name='admin_сategory_update'),
    path('admin_category_delete/<int:id>/', views.admin_category_delete, name='admin_category_delete'),
]