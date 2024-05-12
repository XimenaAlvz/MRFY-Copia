from django.http import HttpResponse
from django.template import Context, Template
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Recipe, Tag, Ingredient, RecipeIngredient, RecipeTag
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.http import JsonResponse
from .models import ShoppingList, ShoppingListItem
import os

def index(request):
    doc_ext = open(os.path.join(settings.BASE_DIR, 'MRFY/templates/landing/index.html'))
    plt = Template(doc_ext.read())
    doc_ext.close()
    ctx = Context()
    return HttpResponse(plt.render(ctx))

def inicio(request):

    recipes = Recipe.objects.all()

    context = {
        "recipes": recipes,
        "user": request.user
    }

    return render(request, 'inicio/inicio.html', context)

def register_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect('register')
        
        # Verificar si el correo electrónico ya está en uso
        if User.objects.filter(email=email).exists():
            messages.error(request, "Este correo electrónico ya está registrado")
            return redirect('register')
        
        # Crear un nuevo usuario
        User.objects.create_user(email=email, name=name, password=password1)
        
        # Redirigir a alguna página después del registro exitoso
        return redirect('login')  # Cambia 'index' a la URL de la página a la que quieres redirigir
        
    return render(request, 'login_registro/form.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        
        # Autenticar al usuario
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            # Iniciar sesión si el usuario es autenticado correctamente
            login(request, user)
            
            # Redirigir a alguna página después del inicio de sesión exitoso
            return redirect('inicio')  # Cambia 'index' a la URL de la página a la que quieres redirigir
            
        else:
            # Mostrar un mensaje de error si las credenciales son incorrectas
            error_message = "Correo electrónico o contraseña incorrectos."
            return render(request, 'login_registro/login.html', {'error_message': error_message})
    
    return render(request, 'login_registro/login.html')

def logout_user(request):
    logout(request)  # Cerrar la sesión del usuario
    return redirect('inicio') # Redirigir a la página de inicio

def recipe(request, id_receta):

    receta = get_object_or_404(Recipe, IDReceta=id_receta)  # Obtiene la receta por ID o devuelve 404 si no existe

    context = {
        "receta": receta,
        "tags": receta.recipetag_set.all(),  # Obtener todas las relaciones RecipeTag asociadas a la receta
        "ingredientes": receta.recipeingredient_set.all(),  # Obtener todas las relaciones RecipeIngredient asociadas a la receta
        "user": request.user
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

    return render(request, 'search/search.html', {'recipes': recipes, 'query': query, 'user': request.user})

def lista_compras(request):
    # Obtener la lista de compras del usuario autenticado
    shopping_list, created = ShoppingList.objects.get_or_create(user=request.user)

    # Obtener los elementos de la lista de compras ordenados por ID de ingrediente
    items = shopping_list.items.all().order_by('name')

    context = {
        'items': items
    }

    return render(request, 'lista_compras/lista.html', context)


def add_to_shopping_list(request, recipe_id):
    if request.method == 'POST':
        # Obtener la receta correspondiente
        recipe = get_object_or_404(Recipe, pk=recipe_id)

        # Obtener la lista de compras del usuario autenticado
        shopping_list, created = ShoppingList.objects.get_or_create(user=request.user)

        # Agregar los ingredientes de la receta a la lista de compras
        for recipe_ingredient in recipe.recipeingredient_set.all():
            ShoppingListItem.objects.create(
                shopping_list=shopping_list,
                name=recipe_ingredient.IDIngrediente.Nombre,
                quantity=recipe_ingredient.Cantidad,
                unit=recipe_ingredient.Unidad if recipe_ingredient.Unidad else ''  # Proporcionar un valor predeterminado si Unidad es None
            )

        # Redirigir al usuario a su lista de compras
        return redirect('lista_compras')

    # Manejar cualquier otro método de solicitud
    return HttpResponseNotAllowed(['POST'])