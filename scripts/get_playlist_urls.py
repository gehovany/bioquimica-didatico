import re

# Lista de URLs dos vídeos da playlist (baseado no mapeamento)
videos = [
    "https://www.youtube.com/watch?v=noaLQ687JBU",  # Aula 1 - Parte 1
    "https://www.youtube.com/watch?v=YJm7gJQZGxo",  # Aula 1 - Parte 2  
    # Adicionar os demais conforme necessário
]

# Salvar em arquivo
with open('/home/ubuntu/bioquimica-didatico/referencias/video_urls.txt', 'w') as f:
    for i, url in enumerate(videos, 1):
        f.write(f"{i}. {url}\n")

print(f"Total de {len(videos)} URLs salvas")
