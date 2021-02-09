from authapp.forms import UserRegisterForm
from authapp.models import User

from django import forms


class UserAdminRegisterFrom(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterFrom, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'
