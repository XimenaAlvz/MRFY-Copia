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
from django.db.models import F
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.http import JsonResponse
from .models import ShoppingList, ShoppingListItem
from decimal import Decimal
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
        
        # Redirigir después del registro exitoso
        return redirect('login')
        
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
            return redirect('inicio')
            
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
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    # Obtener la lista de compras del usuario autenticado
    shopping_list, created = ShoppingList.objects.get_or_create(user=request.user)

    # Iterar sobre los ingredientes de la receta
    for recipe_ingredient in recipe.recipeingredient_set.all():
        # Verificar si el ingrediente ya existe en la lista de compras
        existing_item = shopping_list.items.filter(IDIngrediente=recipe_ingredient.IDIngrediente).first()

        # Si el ingrediente ya está en la lista de compras, sumar la cantidad
        if existing_item:
            if existing_item.quantity is not None and recipe_ingredient.Cantidad is not None:
                existing_item.quantity += recipe_ingredient.Cantidad
                existing_item.save()
        # Si el ingrediente no está en la lista de compras, agregarlo
        else:
            # Crear un nuevo elemento en la lista de compras
            ShoppingListItem.objects.create(
                shopping_list=shopping_list,
                IDIngrediente=recipe_ingredient.IDIngrediente,
                quantity=recipe_ingredient.Cantidad,
                unit=recipe_ingredient.Unidad,
                name=recipe_ingredient.IDIngrediente.Nombre
            )

    return redirect('lista_compras')

def lista_edit(request):
    # Obtener la lista de compras del usuario autenticado
    shopping_list = ShoppingList.objects.get(user=request.user)
    
    # Obtener todos los elementos de la lista de compras
    items = shopping_list.items.all().order_by('name')
    
    context = {
        'items': items
    }
    
    return render(request, 'lista_compras/lista_edit.html', context)

def guardar_cambios_lista(request):
    if request.method == 'POST':
        # Obtener la lista de compras del usuario autenticado
        shopping_list = ShoppingList.objects.get(user=request.user)
        
        # Iterar sobre los elementos de la lista de compras
        for item in shopping_list.items.all():
            # Obtener el nuevo valor de la cantidad desde el formulario
            new_quantity = request.POST.get(str(item.id), None)
            # Actualizar la cantidad si se proporcionó un nuevo valor
            if new_quantity is not None:

                if new_quantity == '':
                    new_quantity = None
                item.quantity = new_quantity
                item.save()
    
    return redirect('lista_compras')

def clear_shopping_list(request):
    # Obtener la lista de compras del usuario autenticado
    shopping_list = request.user.shopping_list
    # Vaciar la lista de compras
    shopping_list.clear_items()
    # Redirigir a la página de lista de compras
    return redirect('lista_compras')

def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(ShoppingListItem, id=item_id)
        item.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)