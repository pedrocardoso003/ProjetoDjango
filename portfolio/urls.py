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
]