import os
import requests
import urllib.request

# Substitua pelas suas credenciais
TOKEN = "IGAAbA314t9zRBZAFp2M2ktQURKQWRsNDktT1p4UHEtanhobVRZARi1fcW1jTVMwb3EtYjZAuQXVRR0J3MDB4SW9uY2NOdnVGRjFVcUQ2Q1B4ckJzcGJlc0JOUlJUYTd4cEhvSWVoZA0JOVVljT2Q3ai0xWkU1VWhxWkNETTlXazUwUQZDZD"

# Pastas de destino
PASTA_DESTINO = "content/ilustracoes" 
PASTA_MIDIA = "static/instagram_midia" # Nova pasta onde as fotos vão morar!

os.makedirs(PASTA_DESTINO, exist_ok=True)
os.makedirs(PASTA_MIDIA, exist_ok=True)

url = f"https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,permalink,timestamp&access_token={TOKEN}"

todas_postagens = []

print("Buscando postagens no Instagram...")

while url:
    resposta = requests.get(url)
    dados_instagram = resposta.json()
    
    lote_atual = dados_instagram.get('data', [])
    todas_postagens.extend(lote_atual)
    
    url = dados_instagram.get('paging', {}).get('next')

print(f"Foram encontradas {len(todas_postagens)} postagens no total. Baixando arquivos...")

for post in todas_postagens:
    post_id = post.get('id')
    media_url = post.get('media_url')
    data_publicacao = post.get('timestamp')
    media_type = post.get('media_type')
    permalink = post.get('permalink')
    legenda_completa = post.get('caption', '')
    
    titulo = legenda_completa.split('\n')[0] if legenda_completa else f"Arte {post_id}"
    titulo_limpo = titulo.replace('"', '').replace('\n', ' ').strip()
    
    # 1. Define se é vídeo ou imagem para colocar a extensão correta
    extensao = ".mp4" if media_type == "VIDEO" else ".jpg"
    nome_arquivo_midia = f"{post_id}{extensao}"
    caminho_midia_local = os.path.join(PASTA_MIDIA, nome_arquivo_midia)
    
    # 2. Faz o download do arquivo SÓ SE ele ainda não existir na sua pasta
    if not os.path.exists(caminho_midia_local):
        print(f"Baixando mídia inédita: {titulo_limpo[:20]}...")
        urllib.request.urlretrieve(media_url, caminho_midia_local)
        
    # 3. Avisa ao Hugo que a imagem agora está dentro do próprio site
    url_para_hugo = f"/instagram_midia/{nome_arquivo_midia}"
    
    conteudo_md = f"""---
title: "{titulo_limpo}"
date: {data_publicacao}
image: "{url_para_hugo}"
media_type: "{media_type}"
link_instagram: "{permalink}"
---

{legenda_completa}
"""
    
    caminho_arquivo = os.path.join(PASTA_DESTINO, f"{post_id}.md")
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo_md)

print(f"🎉 Tudo sincronizado! {len(todas_postagens)} artes estão salvas com segurança.")