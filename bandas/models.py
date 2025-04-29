from django.db import models

# Create your models here.
class Banda(models.Model):
    foto = models.ImageField(null=True, blank=True)
    anoDeCriacao = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    informacoes = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}: criada em: {self.anoDeCriacao}: {self.foto}:'


class Album(models.Model):
    capa = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    banda = models.ForeignKey(Banda,on_delete=models.CASCADE,related_name='Albuns')

    def __str__(self):
        return f'{self.nome}: {self.capa}:'


class Musica(models.Model):
    nome = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    letra = models.TextField(default=1, blank=True, null=True)
    album = models.ForeignKey(Album,on_delete=models.CASCADE,related_name='Musicas')

    def __str__(self):
        return f'{self.nome}: {self.link}: {self.letra}'