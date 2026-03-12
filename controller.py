import os
import time
import random
import logging
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

def list_user_posts(cl):
    """Lista os posts do usuário atual com delays para simular uso humano."""
    try:
        user_id = cl.user_id
        
        # Simula uma pequena pausa antes de buscar os posts
        delay = random.uniform(2, 5)
        logger.info(f"Aguardando {delay:.2f}s antes de buscar posts...")
        time.sleep(delay)
        
        medias = cl.user_medias(user_id, amount=20)
        
        print(f"\n{'='*60}")
        print(f"{'ID DO POST':<20} | {'DATA':<20} | {'LEGENDA'}")
        print(f"{'-'*60}")
        
        for media in medias:
            created_at = media.taken_at.strftime('%d/%m/%Y %H:%M')
            caption = (media.caption_text[:30] + '...') if len(media.caption_text) > 30 else (media.caption_text or "")
            print(f"{media.pk:<20} | {created_at:<20} | {caption}")
            
            # Delay entre o processamento de cada post se necessário (simulando scroll)
            time.sleep(random.uniform(0.5, 1.5))
            
        print(f"{'='*60}\n")
        
    except Exception as e:
        logger.error(f"Erro ao listar posts: {e}")

def post_content(cl):
    """Verifica e posta conteúdos da pasta 'content' baseada na data atual."""
    today = datetime.now().strftime('%Y-%m-%d')
    content_path = Path("content") / today
    
    if not content_path.exists():
        logger.info(f"Nenhum conteúdo agendado para hoje ({today}) em {content_path}.")
        return

    # Busca imagens e legenda
    images = sorted([f for f in content_path.glob("*") if f.suffix.lower() in [".jpg", ".jpeg", ".png"]])
    caption_file = content_path / "caption.txt"
    
    if not images:
        logger.error(f"Nenhuma imagem encontrada na pasta {content_path}.")
        return

    caption = ""
    if caption_file.exists():
        with open(caption_file, "r", encoding="utf-8") as f:
            caption = f.read()

    try:
        logger.info(f"Iniciando postagem para {today}...")
        delay = random.uniform(5, 10)
        logger.info(f"Aguardando {delay:.2f}s antes de postar...")
        time.sleep(delay)

        if len(images) == 1:
            # Post único
            media = cl.photo_upload(images[0], caption)
            logger.info(f"Post único realizado com sucesso! ID: {media.pk}")
        else:
            # Carrossel
            media = cl.album_upload(images, caption)
            logger.info(f"Carrossel realizado com sucesso com {len(images)} imagens! ID: {media.pk}")

    except Exception as e:
        logger.error(f"Erro ao realizar postagem: {e}")
