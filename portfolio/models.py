from django.db import models

# Create your models here.
class Tecnologia(models.Model):
    nome = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='tecnologias/', null=True, blank=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.PositiveIntegerField()
    semestre = models.CharField(max_length=20)
    docentes = models.CharField(max_length=300)
    link_moodle = models.URLField()
    link_ulusofona = models.URLField()

    def __str__(self):
        return f'{self.nome} ({self.ano}/{self.semestre})'


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    video_demo_link = models.URLField(blank=True, null=True)
    conceitos_aplicados = models.TextField()

    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='projetos')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')

    def __str__(self):
        return self.titulo


class ImagemProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='projetos/')

    def __str__(self):
        return f'Imagem de {self.projeto.titulo}'


class DetalhesExtras(models.Model):
    projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE, related_name='detalhes_extras')  # 1-1
    nota_recebida = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    comentario_docente = models.TextField(blank=True)

    def __str__(self):
        return f'Detalhes do projeto {self.projeto.titulo}'






