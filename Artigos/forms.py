from django import forms
from .models import Artigo, Comentario, Rating

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'autor', 'conteudo']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'texto']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['user', 'nota']
