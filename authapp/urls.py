from django.urls import path

from authapp.views import UserCreateView, logout, profile, login

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
]