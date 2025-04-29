# importar_bandas.py
import json
from bandas.models import Banda, Album, Musica

with open('/home/22308918/mysite/bandas/json/bandas.json', 'r', encoding='utf-8') as file:
    bandas_data = json.load(file)

for banda in bandas_data:
    Banda.objects.create(
        nome=banda['nome'],
        anoDeCriacao=banda['anoDeCriacao'],
        informacoes=banda['informacoes'],
        foto=''
    )

print("Bandas importadas com sucesso.")


with open("/home/22308918/mysite/bandas/json/albuns.json", encoding="utf-8") as file:
    albuns = json.load(file)

for album_dict in albuns:
    # Encontra a banda associada ao álbum
    banda = Banda.objects.filter(nome=album_dict["banda"]).first()
    if banda:
        # Cria o álbum, garantindo que a banda está correta
        album_obj = Album.objects.create(
            nome=album_dict["nome"],
            banda=banda,
            capa='',
        )

        # Cria as músicas associadas ao álbum
        for musica_dict in album_dict["musicas"]:
            Musica.objects.create(
                nome=musica_dict["nome"],
                link='https://example.com',
                letra='Letra não disponível',
                album=album_obj
            )
    else:
        print(f"Banda não encontrada para o álbum {album_dict['nome']}")


print("Importação concluída.")

