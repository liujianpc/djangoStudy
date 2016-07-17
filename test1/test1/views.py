from django.http import HttpResponse
from django.shortcuts import render
def index(req):
    return HttpResponse("<h2 style='color:red;'>Hello world ! </h2>")

def fuck(req):
    return HttpResponse('<h1 style="color:red;">fuck you</h1>')