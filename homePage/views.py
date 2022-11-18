from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Pagina inicial")

def userPagr(request):
    return HttpResponse("User page")
