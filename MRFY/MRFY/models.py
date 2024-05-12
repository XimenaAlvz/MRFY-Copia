from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Recipe(models.Model):
    IDReceta = models.AutoField(primary_key=True, unique=True)  # Clave primaria que coincide con la base de datos
    Nombre = models.CharField(max_length=100, null=False)
    Calorias = models.CharField(max_length=50, null=True)
    CarbHidratos = models.CharField(max_length=50, null=True)
    Proteinas = models.CharField(max_length=50, null=True)
    Grasas = models.CharField(max_length=50, null=True)
    Instrucciones = models.TextField(null=True)
    Comentarios = models.TextField(null=True)
    Valoración = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    TiempoPreparación = models.CharField(max_length=50, null=True)
    Imagen = models.TextField(default='images/wallpaper4.jpg')
    Etiquetas = models.ManyToManyField('Tag', through='RecipeTag')
    Ingredientes = models.ManyToManyField('Ingredient', through='RecipeIngredient')

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=255, blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=50, null=True, blank=True, default='')
    allergies = models.CharField(max_length=255, null=True, blank=True, default='')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]

class Ingredient(models.Model):
    IDIngrediente = models.AutoField(primary_key=True, unique=True)  # Clave primaria que coincide con la base de datos 
    Nombre = models.CharField(max_length=100, null=False)

class RecipeIngredient(models.Model):
    IDReceta = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    IDIngrediente = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    Cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Unidad = models.CharField(max_length=50, null=True)

class Tag(models.Model):
    IDTag = models.AutoField(primary_key=True, unique=True)  # Clave primaria que coincide con la base de datos
    Nombre = models.CharField(max_length=100, null=False)

class RecipeTag(models.Model):
    IDReceta = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    IDTag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class ShoppingList(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shopping_list')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Shopping List of {self.user.email}'
    
    def clear_items(self):
        self.items.all().delete()

class ShoppingListItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    unit = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.name} ({self.quantity} {self.unit})'
