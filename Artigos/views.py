from django.shortcuts import render, redirect
from .models import Artigo
from .forms import ArtigoForm, ComentarioForm, RatingForm
from django.db.models import Avg

def lista_artigos(request):
    artigos = Artigo.objects.all().order_by('-dataCriacao')
    return render(request, 'artigos/lista_artigos.html', {'artigos': artigos})

def detalhe_artigo(request, artigo_id):
    artigo = Artigo.objects.get (id=artigo_id)
    comentarios = artigo.comentarios.all()
    media_rating = artigo.ratings.aggregate(Avg('nota'))['nota__avg']

    comentario_form = ComentarioForm()
    rating_form = RatingForm()

    if request.method == 'POST':
        if 'comentario_submit' in request.POST:
            comentario_form = ComentarioForm(request.POST)
            if comentario_form.is_valid():
                comentario = comentario_form.save(commit=False)
                comentario.artigo = artigo
                comentario.save()
                return redirect('artigos:detalhe_artigo', artigo_id=artigo.id)

        elif 'rating_submit' in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                rating = rating_form.save(commit=False)
                rating.artigo = artigo
                rating.save()
                return redirect('artigos:detalhe_artigo', artigo_id=artigo.id)

    context = {
        'artigo': artigo,
        'comentarios': comentarios,
        'media_rating': media_rating,
        'comentario_form': comentario_form,
        'rating_form': rating_form
    }
    return render(request, 'artigos/detalhe_artigo.html', context)

def criar_artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artigos:lista_artigos')
    else:
        form = ArtigoForm()
    return render(request, 'artigos/novo_artigo.html', {'form': form})

def editar_artigo(request, artigo_id):
    artigo = Artigo.objects.get (id=artigo_id)

    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:lista_artigos')
    else:
        form = ArtigoForm(instance=artigo)
        context = {'form': form, 'artigo': artigo}
    return render(request, 'artigos/edita_artigo.html', context)

def apagar_artigo(request, artigo_id):
    artigo = Artigo.objects.get (id=artigo_id)
    artigo.delete()
    return redirect('artigos:lista_artigos')
