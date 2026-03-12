import os
import pyotp
from instagrapi import Client
from instagrapi.exceptions import LoginRequired, ChallengeRequired
import logging

logger = logging.getLogger(__name__)

def get_client():
    """Configura e retorna um cliente autenticado do Instagram."""
    cl = Client()
    
    # Simula um dispositivo real (User Agent e hardware)
    cl.device_settings = {
        "app_version": "269.0.0.18.75",
        "android_version": 26,
        "android_release": "8.0.0",
        "dpi": "480dpi",
        "resolution": "1080x1920",
        "manufacturer": "samsung",
        "device": "SM-G950F",
        "model": "dreamlte",
        "cpu": "exynos8895",
        "version_code": "444444444"
    }
    
    return cl

def login_user(cl, username, password, totp_key, session_file="session.json"):
    """Realiza o login com suporte a sessão persistente e 2FA."""
    try:
        if os.path.exists(session_file):
            cl.load_settings(session_file)
            cl.login(username, password)
            try:
                cl.get_timeline_feed() # Verifica se a sessão é válida
                return True
            except LoginRequired:
                logger.info("Sessão expirada, realizando novo login...")
        
        totp = pyotp.TOTP(totp_key)
        cl.login(username, password, verification_code=totp.now())
        cl.dump_settings(session_file)
        return True
        
    except ChallengeRequired:
        logger.error("Desafio (Checkpoint) detectado. Resolva manualmente no app.")
        return False
    except Exception as e:
        logger.error(f"Erro no login: {e}")
        return False
