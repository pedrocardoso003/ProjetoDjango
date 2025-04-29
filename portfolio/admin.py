from django.contrib import admin
from .models import Projeto, Disciplina, Tecnologia, ImagemProjeto, DetalhesExtras

# Register your models here.
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre')
    ordering = ('ano', 'nome')
    search_fields = ('nome',)

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    ordering = ('nome',)
    search_fields = ('nome',)

class ImagemProjetoAdmin(admin.ModelAdmin):
    list_display = ('projeto',)
    ordering = ('projeto',)

class DetalhesExtrasAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'nota_recebida')
    ordering = ('projeto',)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'disciplina', 'github_link', 'video_demo_link')
    ordering = ('titulo',)
    search_fields = ('titulo', 'descricao')
    filter_horizontal = ('tecnologias',)  # Para facilitar seleção de tecnologias no admin

admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(ImagemProjeto, ImagemProjetoAdmin)
admin.site.register(DetalhesExtras, DetalhesExtrasAdmin)
