from django.shortcuts import render
from .forms import *
# Create your views here.
from django.http import HttpResponse


def index(request):
    form = StartupModelForm(request)
    if request.method == 'GET':
        form = StartupModelForm(request.GET, request)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            start = form.cleaned_data.get("start")
        return render(request, 'index.html', {'form': form, })
    return render(request, 'index.html', {'form': form, })
