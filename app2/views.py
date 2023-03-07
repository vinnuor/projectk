from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def second_app(request):
    return HttpResponse('<h1>secod hii ra macha</h1>')

def app_second(request):
    return HttpResponse('<h2>hii</h1>')