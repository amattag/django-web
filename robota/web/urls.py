"""robota URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('productos/', views.products, name="products"),
    path('productos/<slug>', views.products, name="products"),
    path('ofertas/', views.offers, name="offers"),
    path('noticias/', views.news, name="news"),
    path('noticias/<slug>', views.news, name="news"),
    path('quienes/', views.news, name="who"),
]
