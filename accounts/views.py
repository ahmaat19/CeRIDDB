from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginModelForm, UserUpdateForm, ProfileUpdateForm
from .decorators import unauthenticated_user, allowed_users



def LoginView(request):
    if  request.user.is_anonymous:
        if request.method == 'POST':
            form = LoginModelForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('/accounts/signup/')
        else:
            form = LoginModelForm()
    else:
        return redirect('/accounts/password_change/')
    context = {
        'form': form,
        'title': 'Login Form',
        'valueBtn': 'Login',
    }
    return render(request, 'accounts/login.html', context)



@login_required
# @allowed_users(allowed_roles=['admin'])
def ProfileView(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated successfully!')
            return redirect('/accounts/profile/')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'accounts/profile.html', context)

