from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.lista_artigos, name='lista_artigos'),
    path('artigos/<int:artigo_id>/', views.detalhe_artigo, name='detalhe_artigo'),
    path('artigos/novo/', views.criar_artigo, name='criar_artigo'),
    path('artigos/<int:artigo_id>/editar/', views.editar_artigo, name='editar_artigo'),
    path('artigos/<int:artigo_id>/apagar/', views.apagar_artigo, name='apagar_artigo'),
]
