import time
import random
import logging
from datetime import datetime

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
            caption = (media.caption_text[:30] + '...') if len(media.caption_text) > 30 else media.caption_text
            print(f"{media.pk:<20} | {created_at:<20} | {caption}")
            
            # Delay entre o processamento de cada post se necessário (simulando scroll)
            time.sleep(random.uniform(0.5, 1.5))
            
        print(f"{'='*60}\n")
        
    except Exception as e:
        logger.error(f"Erro ao listar posts: {e}")
