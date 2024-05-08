from django.http import HttpResponse
from django.template import Context, Template
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import Recipe
from django.contrib import messages
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

#def login(request):
#    doc_ext = open(os.path.join(settings.BASE_DIR, 'MRFY/templates/login_registro/form.html'))
#    plt = Template(doc_ext.read())
#    doc_ext.close()
#    ctx = Context()
#    return HttpResponse(plt.render(ctx))
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario
            messages.success(request, "Registro exitoso.")  # Muestra un mensaje de éxito
            return redirect('inicio')  # Redirige a una página después de registrarse
    else:
        form = UserRegistrationForm()  # Muestra un formulario vacío

    return render(request, 'login_registro/form.html', {'form': form})  # Renderiza el template con el formulario

def recipe(request, id_receta):
    #doc_ext = open(os.path.join(settings.BASE_DIR, 'MRFY/templates/vista_receta/recipe.html'))
    #plt = Template(doc_ext.read())
    #doc_ext.close()
    #ctx = Context()
    #return HttpResponse(plt.render(ctx))
    receta = get_object_or_404(Recipe, IDReceta=id_receta)  # Obtiene la receta por ID o devuelve 404 si no existe
    return render(request, 'vista_receta/recipe.html', {'receta': receta})
