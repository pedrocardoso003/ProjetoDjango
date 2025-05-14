from django.shortcuts import render, redirect
from .models import Projeto, Tecnologia
# Create your views here.
# noobsite/views.py

from django.http import HttpResponse
from .forms import ProjetoForm
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

def cv_view(request):
    return render(request, 'portfolio/cv.html')

def novo_projeto_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.save()
            form.save_m2m()  #guarda os many2many tecnologia
            return redirect('portfolio:projetos')
        else:
            print(form.errors)
    else:
        form = ProjetoForm()

    return render(request, 'portfolio/novo_projeto.html', {'form': form})


def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)

    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('portfolio:projetos')  # cria formulário com dados da instância autor
    else:
        form = ProjetoForm(instance=projeto)

    context = {'form': form, 'projeto': projeto}
    return render(request, 'portfolio/edita_projeto.html', context)

def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('portfolio:projetos')





