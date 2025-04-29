from django.contrib import admin

from .models import Autor, Artigo, Comentario, Rating

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'bio')
    search_fields = ('nome',)

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'dataCriacao')
    search_fields = ('titulo',)
    ordering = ('dataCriacao',)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'autor', 'dataComentario')
    search_fields = ('autor', 'texto')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'user', 'nota', 'dataRating')
    search_fields = ('user',)


admin.site.register(Autor, AutorAdmin)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Rating, RatingAdmin)