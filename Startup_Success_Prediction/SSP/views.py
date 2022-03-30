from django.shortcuts import render
from .forms import *
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from jinja2 import Undefined  # add this
from .forms import *
from .models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView


def homepage(request):
    form = StartupModelForm(request)
    if request.method == 'GET':
        form = StartupModelForm(request.GET, request)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            start = form.cleaned_data.get("start")
        return render(request, 'index.html', {'form': form, })
    return render(request, 'index.html', {'form': form, })


def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        # login(request, user)
        return redirect('SSP:loginPage')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('SSP:homepage')
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(
                        request, f"You are now logged in as {username}.")
                    return redirect("SSP:homepage")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("SSP:loginPage")
