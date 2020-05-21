from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import context
from daydreamBkS.models import Category
from daydreamBkS.models import Book
from daydreamBkS import views


def index(request):
    allcategory = Category.objects.all()
    allbooks = Book.objects.all()
    context = {
        'allcategory': allcategory,
        'allbooks': allbooks,
    }

    return render(request, 'index.html', context)


def categories(request):
    return render(request, 'categories.html')


def books_show(request):
    allbooks = Book.objects.all()
    context = {
        'allbooks': allbooks,
    }
    return render(request, 'product.html', context)
