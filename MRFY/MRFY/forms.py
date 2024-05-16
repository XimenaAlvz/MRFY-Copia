from django import forms
from django_select2.forms import Select2MultipleWidget, Select2Widget
from .models import Recipe, Tag, Ingredient
from ckeditor_uploader.widgets import CKEditorUploadingWidget

UNIDADES_CHOICES = [
    ('gramos', 'Gramos'),
    ('kilogramos', 'Kilogramos'),
    ('mililitros', 'Mililitros'),
    ('litros', 'Litros'),
    ('piezas', 'Piezas'),
    ('docenas', 'Docenas'),
    ('cucharadas', 'Cucharadas'),
    ('cucharaditas', 'Cucharaditas'),
    ('tazas', 'Tazas'),
    ('onzas', 'Onzas'),
    ('libras', 'Libras'),
    ('galones', 'Galones'),
    ('pintas', 'Pintas'),
    ('centilitros', 'Centilitros'),
    ('decilitros', 'Decilitros'),
    ('onzas líquidas', 'Onzas líquidas'),
    ('puñados', 'Puñados'),
    ('rebanadas', 'Rebanadas'),
    ('dientes', 'Dientes'),
    ('ramas', 'Ramas'),
]

class RecipeForm(forms.ModelForm):

    Instrucciones = forms.CharField(widget=CKEditorUploadingWidget())

    Ingredientes = forms.ModelChoiceField(
        queryset=Ingredient.objects.all(),
        widget=Select2Widget(attrs={'class': 'hidden'}),
        required=True
    )
    Cantidad = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    Unidad = forms.ChoiceField(choices=UNIDADES_CHOICES, widget=Select2Widget, required=False)

    class Meta:
        model = Recipe
        fields = [
            'Nombre', 'Calorias', 'CarbHidratos', 'Proteinas', 'Grasas', 'Instrucciones', 
            'Comentarios', 'Valoración', 'TiempoPreparación', 'Imagen', 'Etiquetas', 
            'Ingredientes', 'Cantidad', 'Unidad'
        ]
        widgets = {
            'Etiquetas': Select2MultipleWidget,
        }
