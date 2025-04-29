from bandas.models import Banda, Album, Musica

1. Listar o nome das bandas, ordenadas alfabeticamente
R:Banda.objects.order_by('nome').values_list('nome', flat=True)

2.Listar os nomes dos álbuns de uma banda específica (ex: "Queen"), ordenados por nome
R:banda = Banda.objects.get(nome="Queen")
banda.Albuns.order_by('nome').values_list('nome', flat=True)

3.Apresentar todos os álbuns lançados entre 1970 e 1980
R:Album.objects.filter(nome__isnull=False, banda__anoDeCriacao__gte="1970", banda__anoDeCriacao__lte="1980").values('nome', 'banda__nome')

4.Criar uma playlist de um álbum: listar links das músicas do álbum "A Night at the Opera"
R:album = Album.objects.get(nome="A Night at the Opera")
album.Musicas.values_list('link', flat=True)

5.
R:

6.
R:

7.Mostrar todas as bandas que têm mais de 1 álbum
R:from django.db.models import Count
Banda.objects.annotate(num_albuns=Count('Albuns')).filter(num_albuns__gt=1).values('nome', 'num_albuns')

8.
R:



10.Listar todas as bandas que não têm álbuns associados
R:Banda.objects.filter(Albuns__isnull=True).values_list('nome', flat=True)



