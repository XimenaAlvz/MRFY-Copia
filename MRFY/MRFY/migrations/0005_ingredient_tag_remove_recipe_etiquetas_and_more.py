# Generated by Django 5.0.3 on 2024-05-11 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MRFY', '0004_alter_recipe_idreceta_alter_user_correo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('IDIngrediente', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('IDTag', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='Etiquetas',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='Ingredientes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='Imagen',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='IDReceta',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.CharField(max_length=50, null=True)),
                ('Unidad', models.CharField(max_length=50, null=True)),
                ('IDIngrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MRFY.ingredient')),
                ('IDReceta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MRFY.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDReceta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MRFY.recipe')),
                ('IDTag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MRFY.tag')),
            ],
        ),
    ]