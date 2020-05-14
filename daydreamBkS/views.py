from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import context
from daydreamBkS.models import Category
from daydreamBkS import views


def index(request):
    allcategory = Category.objects.all()

    context = {
        'allcategory': allcategory,
    }

    return render(request, 'index.html', context)


def categories(request):

    return render(request, 'categories.html', context)