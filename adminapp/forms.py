from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User
from mainapp.models import ProductCategory

from django import forms



class UserAdminRegisterFrom(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterFrom, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):
    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False


class CategoryAdminForm(forms.ModelForm):
    discount = forms.IntegerField(label='скидка', required=False, min_value=0, max_value=90, initial=0)
    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Category name'
        self.fields['description'].widget.attrs['placeholder'] = 'Category description'
        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] ='form-control py-4'





