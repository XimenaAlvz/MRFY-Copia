from django.http import HttpResponse
from django.template import Context, Template
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import Recipe, Tag, Ingredient, RecipeIngredient, RecipeTag
from django.contrib import messages
from django.db.models import Q
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

    context = {
        "receta": receta,
        "tags": receta.recipetag_set.all(),  # Obtener todas las relaciones RecipeTag asociadas a la receta
        "ingredientes": receta.recipeingredient_set.all()  # Obtener todas las relaciones RecipeIngredient asociadas a la receta
    }

    return render(request, 'vista_receta/recipe.html', context)  # Renderiza el template con la receta
    #return render(request, 'vista_receta/recipe.html', {'receta': receta})

def search(request):
    query = request.GET.get('q')
    recipes = []

    if query:
        # Filtrar recetas por el término de búsqueda en el nombre y en las etiquetas
        recipes = Recipe.objects.filter(
            Q(Nombre__icontains=query) |  # Buscar en el nombre de la receta
            Q(Etiquetas__Nombre__icontains=query)  # Buscar en los nombres de las etiquetas asociadas a las recetas
        ).distinct()

    return render(request, 'search/search.html', {'recipes': recipes, 'query': query})