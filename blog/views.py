from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse('<h1>hello python</h1>')


git@github.com:Ilovenjoylife/myboy.git