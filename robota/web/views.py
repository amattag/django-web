
from django.shortcuts import render

from .models import Robot, New


# Create your views here.

def index(request):
    context = {
        'enterprise': "Robota, Inc",
        'year': 2018,
    }

    return render(request, 'web/index.html', context)


def products(request, slug=None):
    if slug == None:
        context = {
            'robots': Robot.objects.all(),
        }
        return render(request, 'web/products/main.html', context)
    else:
        context = {
            'robot': Robot.objects.get(slug=slug),
        }
        return render(request, 'web/products/main_details.html', context)


def offers(request):
    context = {
        'enterprise': "Robota, Inc",
        'year': 2018,
    }

    return render(request, 'web/content.html', context)


def news(request, slug=None):
    if slug == None:
        context = {
            'news': New.objects.all(),
        }
        return render(request, 'web/news/main.html', context)
    else:
        context = {
            'new': New.objects.get(slug=slug),
        }
        return render(request, 'web/news/main_details.html', context)


def who(request):
    context = {
        'enterprise': "Quienes Somos",
        'year': 2018,
    }

    return render(request, 'web/content.html', context)

