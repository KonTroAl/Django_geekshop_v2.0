from django.urls import path ,re_path

from authapp.views import register, logout, login, UserProfileView, verify

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),

    path('verify/<int:user_id>/<hash>/', verify, name='verify')
]