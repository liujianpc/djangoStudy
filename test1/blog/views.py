from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def intro(req):
    return ('<h1>this is my blog</h1>')
