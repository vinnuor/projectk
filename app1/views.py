from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app(request):
    return HttpResponse('<h1>hii ra macha</h1>')

def app_first(request):
    return HttpResponse('<h2> hii ra mallesh')