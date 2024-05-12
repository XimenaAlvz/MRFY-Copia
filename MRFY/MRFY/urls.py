"""
URL configuration for MRFY project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from MRFY.views import index, inicio, recipe, search, register_user, login_user, logout_user, lista_compras

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),  # Empty path maps to the index view
    path('index/', index, name='index'),
    path('inicio/', inicio, name='inicio'),
    path('form/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('recipe/<int:id_receta>/', recipe, name='recipe_detail'),
    path('search/', search, name='search'),
    path('lista/', lista_compras, name='lista_compras')
]
