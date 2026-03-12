import os
import logging
import json
import time
import argparse
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from auth import get_client, login_user
from controller import list_user_posts, post_content

# Configuração de Logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

POSTED_DATES_FILE = Path("posted_dates.json")

def load_posted_dates():
    if POSTED_DATES_FILE.exists():
        with open(POSTED_DATES_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_posted_date(date_str):
    posted_dates = load_posted_dates()
    if date_str not in posted_dates:
        posted_dates.append(date_str)
        with open(POSTED_DATES_FILE, "w") as f:
            json.dump(posted_dates, f)

def run_automation():
    """Executa a lógica de verificação e postagem do dia."""
    today = datetime.now().strftime("%Y-%m-%d")
    posted_dates = load_posted_dates()

    if today in posted_dates:
        logger.info(f"Conteúdo de hoje ({today}) já foi postado.")
        return False

    content_dir = Path("content") / today
    if not content_dir.exists():
        logger.info(f"Nenhuma pasta de conteúdo encontrada para hoje: {content_dir}")
        return False

    logger.info(f"Iniciando postagem automática para {today}...")
    try:
        load_dotenv()
        USERNAME = os.getenv("IG_USERNAME")
        PASSWORD = os.getenv("IG_PASSWORD")
        TOTP_KEY = os.getenv("IG_TOTP_KEY") or os.getenv("TOTP_KEY")
        SESSION_FILE = os.getenv("SESSION_FILE", "session.json")
        
        cl = get_client()
        if login_user(cl, USERNAME, PASSWORD, TOTP_KEY, SESSION_FILE):
            success = post_content(cl)
            if success:
                save_posted_date(today)
                logger.info(f"Postagem de {today} concluída com sucesso.")
                return True
        else:
            logger.error("Falha na autenticação automática.")
    except Exception as e:
        logger.error(f"Erro na postagem automática: {e}", exc_info=True)
    
    return False

def main():
    parser = argparse.ArgumentParser(description="InstAutopost - Automação de Instagram")
    parser.add_argument("--list", action="store_true", help="Listar posts do usuário")
    parser.add_argument("--loop", action="store_true", help="Executar em loop contínuo (1h) para automação")
    
    args = parser.parse_args()
    load_dotenv()

    if args.loop:
        logger.info("Modo Automação Ativado. Verificando a cada 1 hora...")
        while True:
            run_automation()
            time.sleep(3600)  # Espera 1 hora
    elif args.list:
        USERNAME = os.getenv("IG_USERNAME")
        PASSWORD = os.getenv("IG_PASSWORD")
        TOTP_KEY = os.getenv("IG_TOTP_KEY") or os.getenv("TOTP_KEY")
        SESSION_FILE = os.getenv("SESSION_FILE", "session.json")
        cl = get_client()
        if login_user(cl, USERNAME, PASSWORD, TOTP_KEY, SESSION_FILE):
            list_user_posts(cl)
    else:
        # Se rodar sem argumentos (ex: python main.py), tenta postar o dia atual uma única vez
        run_automation()

if __name__ == "__main__":
    main()
