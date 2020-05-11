from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse('欢迎使用Daydream! Have a good time!')