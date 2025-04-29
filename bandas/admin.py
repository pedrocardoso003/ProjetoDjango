from django.contrib import admin

from .models import Banda
from .models import Album
from .models import Musica

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome','anoDeCriacao','informacoes')
    ordering = ('nome','anoDeCriacao')
    searchField = ('nome')

admin.site.register(Banda,BandaAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nome','banda','capa')
    ordering = ('nome',)
    searchField = ('nome','banda')

admin.site.register(Album,AlbumAdmin)

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('nome','album','link')
    ordering = ('nome','album')
    searchField = ('nome','banda')

admin.site.register(Musica,MusicaAdmin)