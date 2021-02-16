from django.urls import path

from authapp.views import UserCreateView, logout, login, UserProfileView

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
]