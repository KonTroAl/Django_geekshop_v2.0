from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.models import User
from adminapp.forms import UserAdminRegisterFrom


def index(request):
    return render(request, 'adminapp/index.html')


def admin_users_read(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterFrom(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users_read'))
    else:
        form = UserAdminRegisterFrom()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)
