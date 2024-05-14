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
from MRFY.views import index, inicio, recipe, search, register_user, login_user, logout_user, lista_compras, add_to_shopping_list, clear_shopping_list, lista_edit, guardar_cambios_lista, delete_item, publicar_receta, brew_coffee, teapot_view

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
    path('lista/', lista_compras, name='lista_compras'),
    path('add_to_shopping_list/<int:recipe_id>/', add_to_shopping_list, name='add_to_shopping_list'),
    path('clear_shopping_list/', clear_shopping_list, name='clear_shopping_list'),
    path('guardar_cambios_lista/', guardar_cambios_lista, name='guardar_cambios_lista'),
    path('list_edit/', lista_edit, name='lista_edit'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('recipeform/', publicar_receta, name='publicar_receta'),
    path('brew/', brew_coffee, name='brew_coffee'),
    path('teapot/', teapot_view, name='teapot'),
    
]
