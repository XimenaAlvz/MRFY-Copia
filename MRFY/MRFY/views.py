from django.http import HttpResponse
from django.template import Context, Template
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Recipe
import os

def index(request):
    doc_ext = open(os.path.join(settings.BASE_DIR, 'MRFY/templates/landing/index.html'))
    plt = Template(doc_ext.read())
    doc_ext.close()
    ctx = Context()
    return HttpResponse(plt.render(ctx))

def inicio(request):
    #doc_ext = open(os.path.join(settings.BASE_DIR, 'MRFY/plantillas/inicio/inicio.html'))
    #plt = Template(doc_ext.read())
    #doc_ext.close()
    #ctx = Context()
    #return HttpResponse(plt.render(ctx))

    recipes = Recipe.objects.all()

    # Procesar etiquetas antes de pasarlas al template
    for recipe in recipes:
    # Procesar etiquetas
        if recipe.Etiquetas:
            recipe.etiquetas_lista = recipe.Etiquetas.split(',')
        else:
            recipe.etiquetas_lista = []

        # Procesar ingredientes
        if recipe.Ingredientes:
            recipe.ingredientes_lista = recipe.Ingredientes.split(',')
        else:
            recipe.ingredientes_lista = []

    context = {
        "recipes": recipes
    }

    return render(request, 'inicio/inicio.html', context)

    #context = {
    #    "recipes": Recipe.objects.all()
    #}
    #return render(request, 'inicio/inicio.html', context)

def login(request):
    doc_ext = open(os.path.join(settings.BASE_DIR, 'MRFY/templates/login_registro/form.html'))
    plt = Template(doc_ext.read())
    doc_ext.close()
    ctx = Context()
    return HttpResponse(plt.render(ctx))

def recipe(request, id_receta):
    #doc_ext = open(os.path.join(settings.BASE_DIR, 'MRFY/templates/vista_receta/recipe.html'))
    #plt = Template(doc_ext.read())
    #doc_ext.close()
    #ctx = Context()
    #return HttpResponse(plt.render(ctx))
    receta = get_object_or_404(Recipe, IDReceta=id_receta)  # Obtiene la receta por ID o devuelve 404 si no existe
    return render(request, 'vista_receta/recipe.html', {'receta': receta})
