import secrets
import string
from sqlalchemy.orm import Session
from app.models.user import User
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_secure_password(length=20):
    """Gera uma senha segura aleatória sem caracteres especiais"""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def ensure_master_user(db: Session):
    """
    Garante que existe um usuário master no sistema.
    Se não existir, cria um com senha aleatória.
    """
    # Verificar se já existe usuário master
    master_user = db.query(User).filter(User.username == "master").first()
    
    if not master_user:
        # Gerar senha aleatória
        password = generate_secure_password()
        
        # Criar usuário master
        master_user = User(
            username="master",
            email="master@system.local",
            hashed_password=User.get_password_hash(password)
        )
        
        db.add(master_user)
        db.commit()
        db.refresh(master_user)
        
        # Exibir credenciais
        logger.info("="*50)
        logger.info("USUÁRIO MASTER CRIADO COM SUCESSO!")
        logger.info("="*50)
        logger.info("Credenciais de acesso:")
        logger.info(f"Username: master")
        logger.info(f"Password: {password}")
        logger.info("="*50)
        logger.info("GUARDE ESTAS INFORMAÇÕES!")
        logger.info("="*50)
    else:
        logger.info("Usuário master já existe no sistema.")
