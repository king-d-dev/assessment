from django.shortcuts import render
from django.contrib.auth import authenticate


def home(request):
    return render(request, 'home.html')
