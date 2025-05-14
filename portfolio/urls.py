# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'portfolio'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.lista_tecnologias, name='lista_tecnologias'),
    path('cv/', views.cv_view, name='cv'),
    path('projetos/novo', views.novo_projeto_view, name="novo_projeto"),
    path('projetos/edita/<int:projeto_id>/', views.edita_projeto_view, name="edita_projeto"),
    path('projetos/<int:projeto_id>/apaga', views.apaga_projeto_view,name="apaga_projeto"),
]