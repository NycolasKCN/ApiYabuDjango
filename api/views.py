from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("hello world!")

def userPage(request):
    return render(request, "home.html")