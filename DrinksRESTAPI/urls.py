"""
URL configuration for DrinksRESTAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API Endpoints
    path('drinks/', v.drinkListView, name='drink_list_view'),
    path('drinks/<int:id>/', v.drinkDetails, name="drink_details_view"),

    path('classDrinks/', v.classDrinkListView.as_view(), name='class_drink_list_view'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# Formatter to get the plain json from the database
