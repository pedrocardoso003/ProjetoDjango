from django.shortcuts import render
from .models import Projeto, Tecnologia
# Create your views here.
# noobsite/views.py

from django.http import HttpResponse

#def index_view(request):
   #return HttpResponse("portfolio")

def index_view(request):
    return render(request, "portfolio/index.html")

def sobre_view(request):
    return render(request, "portfolio/sobre.html")

def projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def lista_tecnologias(request):
    tecnologias = Tecnologia.objects.prefetch_related('projetos')
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})