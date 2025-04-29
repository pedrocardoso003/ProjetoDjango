import json
from portfolio.models import Projeto, Disciplina, Tecnologia, ImagemProjeto, DetalhesExtras

with open('/home/22308918/mysite/portfolio/json/projetos.json', 'r', encoding='utf-8') as file:
    projetos = json.load(file)

for p in projetos:
    # Trata a disciplina
    disciplina_obj, _ = Disciplina.objects.get_or_create(
        nome=p["disciplina"],
        defaults={
            "ano": int(p["ano"].split('º')[0]),
            "semestre": p["semestre"],
            "docentes": "Por preencher",
            "link_moodle": "https://example.com/moodle",  # Placeholder
            "link_ulusofona": "https://example.com/ulusofona"  # Placeholder
        }
    )

    # Cria o projeto
    projeto = Projeto.objects.create(
        titulo=p["nome"],
        descricao=p["descricao"],
        github_link=p["github"] if p["github"] != "N/A" else None,
        video_demo_link=p["video"] if p["video"] != "N/A" else None,
        conceitos_aplicados="\n".join(p["conceitos"]),
        disciplina=disciplina_obj
    )

    # Liga as tecnologias
    for tech_name in p["tecnologias"]:
        tecnologia_obj, _ = Tecnologia.objects.get_or_create(
            nome=tech_name,
            defaults={
                "descricao": "Descrição por preencher.",
                "logo": None
            }
        )
        projeto.tecnologias.add(tecnologia_obj)

    # Adiciona imagens (se houver)
    for img_path in p["imagens"]:
        ImagemProjeto.objects.create(
            projeto=projeto,
            imagem=img_path  # Isto assume que já estão no diretório correto
        )

    # Cria DetalhesExtras (opcional)
    DetalhesExtras.objects.create(
        projeto=projeto,
        nota_recebida=None,
        comentario_docente=""
    )

print("Importação dos projetos concluída.")
