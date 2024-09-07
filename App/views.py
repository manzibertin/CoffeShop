from django.shortcuts import render
from django.http import HttpResponse

def App(request):
    return HttpResponse("Hello world!")
