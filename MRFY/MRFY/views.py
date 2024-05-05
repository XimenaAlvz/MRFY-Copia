from django.http import HttpResponse
from django.template import Context, Template
from django.conf import settings
import os

def index(request):
    doc_ext = open(os.path.join(settings.BASE_DIR, 'MRFY/plantillas/landing/index.html'))
    plt = Template(doc_ext.read())
    doc_ext.close()
    ctx = Context()
    return HttpResponse(plt.render(ctx))

def inicio(request):
    doc_ext = open(os.path.join(settings.BASE_DIR, 'MRFY/plantillas/inicio/inicio.html'))
    plt = Template(doc_ext.read())
    doc_ext.close()
    ctx = Context()
    return HttpResponse(plt.render(ctx))

def login(request):
    doc_ext = open(os.path.join(settings.BASE_DIR, 'MRFY/plantillas/login_registro/form.html'))
    plt = Template(doc_ext.read())
    doc_ext.close()
    ctx = Context()
    return HttpResponse(plt.render(ctx))

def recipe(request):
    doc_ext = open(os.path.join(settings.BASE_DIR, 'MRFY/plantillas/vista_receta/recipe.html'))
    plt = Template(doc_ext.read())
    doc_ext.close()
    ctx = Context()
    return HttpResponse(plt.render(ctx))
