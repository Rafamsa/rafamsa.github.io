import os
import requests

# Substitua pelas suas credenciais
TOKEN = "IGAAbA314t9zRBZAFp2M2ktQURKQWRsNDktT1p4UHEtanhobVRZARi1fcW1jTVMwb3EtYjZAuQXVRR0J3MDB4SW9uY2NOdnVGRjFVcUQ2Q1B4ckJzcGJlc0JOUlJUYTd4cEhvSWVoZA0JOVVljT2Q3ai0xWkU1VWhxWkNETTlXazUwUQZDZD"
PASTA_DESTINO = "content/ilustracoes"
os.makedirs(PASTA_DESTINO, exist_ok=True)

# URL inicial da API
url = f"https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,permalink,timestamp&access_token={TOKEN}"

todas_postagens = []

print("Buscando postagens no Instagram...")

# O loop que navega pelas páginas da API da Meta
while url:
    resposta = requests.get(url)
    dados_instagram = resposta.json()

    lote_atual = dados_instagram.get("data", [])
    todas_postagens.extend(lote_atual)

    # Se houver uma próxima página, a API entrega o link em 'next'
    url = dados_instagram.get("paging", {}).get("next")

print(
    f"Foram encontradas {len(todas_postagens)} postagens no total. Gerando arquivos Markdown..."
)

for post in todas_postagens:
    post_id = post.get("id")
    media_url = post.get("media_url")
    data_publicacao = post.get("timestamp")
    media_type = post.get("media_type")
    permalink = post.get("permalink")
    legenda_completa = post.get("caption", "")

    titulo = legenda_completa.split("\n")[0] if legenda_completa else f"Arte {post_id}"
    titulo_limpo = titulo.replace('"', "").replace("\n", " ").strip()

    conteudo_md = f"""---
title: "{titulo_limpo}"
date: {data_publicacao}
image: "{media_url}"
media_type: "{media_type}"
link_instagram: "{permalink}"
---

{legenda_completa}
"""

    caminho_arquivo = os.path.join(PASTA_DESTINO, f"{post_id}.md")
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo_md)

print(
    f"🎉 Sucesso absoluto! {len(todas_postagens)} arquivos salvos em '{PASTA_DESTINO}'."
)
