from django.http import HttpResponse
from django.shortcuts import render
from .task import *
# Create your views here.

def home(request):
    email()
    return HttpResponse('<h1>hello </h1>')