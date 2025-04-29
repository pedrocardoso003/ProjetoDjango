from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE,related_name='artigos')
    dataCriacao = models.DateTimeField(auto_now_add=True)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    dataComentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} no artigo {self.artigo.titulo}"

class Rating(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='ratings')
    user = models.CharField(max_length=100)
    nota = models.PositiveIntegerField(default=1)
    dataRating = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating de {self.user} para o artigo {self.artigo.titulo}"