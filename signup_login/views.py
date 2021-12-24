
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import CreateUserForm

@csrf_exempt
def registerPage(request) :
    if request.user.is_authenticated :
        return redirect('users')
    else :
        form = CreateUserForm()
        if request.method == 'POST' :
            form = CreateUserForm(request.POST)
            if form.is_valid() :
                user = form.save()
                profile = user.userprofile
                user_group = form.cleaned_data.get('address','email')
                profile.user_type = user_group
                profile.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form' : form}
        return render(request, 'register.html', context)


def loginPage(request) :
    if request.user.is_authenticated :
        return redirect('users')
    else :
        if request.method == 'POST' :
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None :
                login(request, user)
                return redirect('users')
            else :
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request) :
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def users(request) :
    all_user=UserProfile.objects.all()

    return render(request, 'users.html', {'all_user' : all_user})

@login_required(login_url='login')
def delete_users(request, pk):
    queryset = UserProfile.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Deleted Successfully')
        return redirect('users')
    context = {

    }
    return render(request, 'delete_user.html',context)
