from django.shortcuts import render, HttpResponseRedirect
from django.db import connection
from django.db.models import F
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from authapp.models import User
from adminapp.forms import UserAdminRegisterFrom, UserAdminProfileForm, CategoryAdminForm
from mainapp.models import ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')


class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_read(request):
#     context = {
#         'users': User.objects.all()
#     }
#     return render(request, 'adminapp/admin-users-read.html', context)

class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterFrom
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterFrom(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users_read'))
#     else:
#         form = UserAdminRegisterFrom()
#     context = {'form': form}
#     return render(request, 'adminapp/admin-users-create.html', context)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request, id=None):
#     user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users_read'))
#     else:
#         form = UserAdminProfileForm(instance=user)
#     context = {
#         'form': form,
#         'current_user': user,
#     }
#     return render(request, 'adminapp/admin-users-update-delete.html', context)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_users_recover(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_category_read(request):
    context = {'categories': ProductCategory.objects.all()}
    return render(request, 'adminapp/admin-category-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryAdminForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category_read'))
    else:
        form = CategoryAdminForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-category-create.html', context)

def db_profile_by_type(prefix, type, queries):
   update_queries = list(filter(lambda x: type in x['sql'], queries))
   print(f'db_profile {type} for {prefix}:')
   [print(query['sql']) for query in update_queries]


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_category_read')
    form_class = CategoryAdminForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = ProductCategory.objects.get(id=self.kwargs['pk'])
        context['current_category'] = category
        return context

    def form_valid(self, form):
        if 'discount' in form.cleaned_data:
            discount = form.cleaned_data['discount']
            if discount:
                self.object.product_set.update(price=F('price') * (1 - discount / 100))
                db_profile_by_type(self.__class__, 'UPDATE', connection.queries)

        return super().form_valid(form)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_category_update(request, id):
#     category = ProductCategory.objects.get(id=id)
#     if request.method == 'POST':
#         form = CategoryAdminForm(data=request.POST, instance=category)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_category_read'))
#     else:
#         form = CategoryAdminForm(instance=category)
#     context = {
#         'form': form,
#         'current_category': category,
#     }
#     return render(request, 'adminapp/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, id):
    category = ProductCategory.objects.get(id=id)
    category.delete()
    return HttpResponseRedirect(reverse('admins:admin_category_read'))
