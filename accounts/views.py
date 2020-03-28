from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginModelForm
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
    return render(request, 'accounts/profile.html')

