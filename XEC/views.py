from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from .forms import UsersLoginForm
from django.views.generic import ListView

from models import *


def Login_page(request):
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        login(request, user)
        return redirect("/")

    context = {'form': form,
               'title': 'login'}
    return render(request, 'registration/login.html', context)


@login_required()
def AysHome(request):
    return render(request, 'XEC/ays_home.html')
