from django.http import HttpResponse
from django.template import Context, Template

def index(request):

    doc_ext = open("C:/Users/jerem/OneDrive/Escritorio/Django Project/MRFY/MRFY/plantillas/landing/index.html")

    plt = Template(doc_ext.read())

    doc_ext.close()

    ctx = Context()

    return HttpResponse(plt.render(ctx))

