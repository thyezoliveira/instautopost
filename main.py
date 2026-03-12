import os
import logging
from dotenv import load_dotenv
from auth import get_client, login_user
from controller import list_user_posts, post_content

# Configuração de Logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    load_dotenv()
    
    USERNAME = os.getenv("IG_USERNAME")
    PASSWORD = os.getenv("IG_PASSWORD")
    TOTP_KEY = os.getenv("IG_TOTP_KEY") or os.getenv("TOTP_KEY")
    SESSION_FILE = os.getenv("SESSION_FILE", "session.json")
    
    if not USERNAME or not PASSWORD or not TOTP_KEY:
        logger.error("Credenciais não encontradas no arquivo .env. Verifique o arquivo.")
        return

    cl = get_client()
    
    logger.info("Tentando autenticação...")
    if login_user(cl, USERNAME, PASSWORD, TOTP_KEY, SESSION_FILE):
        logger.info("Login realizado com sucesso!")
        
        # 1. Lista os posts do usuário
#        list_user_posts(cl)
        
        # 2. Verifica se há conteúdo agendado para hoje e posta
        post_content(cl)
    else:
        logger.error("Falha na autenticação.")

if __name__ == "__main__":
    main()
