from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.models.user import User
import os
import sys

# Verificar se as variáveis de ambiente necessárias estão definidas
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("Erro: A variável de ambiente DATABASE_URL não está definida")
    print("Configure a string de conexão do seu banco gerenciado no arquivo .env")
    sys.exit(1)

# Configurações do Admin via Variáveis de Ambiente
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")

if not ADMIN_PASSWORD or not ADMIN_EMAIL:
    print("Erro: As variáveis ADMIN_PASSWORD e ADMIN_EMAIL precisam estar definidas no arquivo .env")
    sys.exit(1)

try:
    # Criar banco e tabelas
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

    # Criar sessão
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()

    # Verificar se o admin já existe
    existing_admin = db.query(User).filter(User.email == ADMIN_EMAIL).first()

    if not existing_admin:
        # Criar usuário admin apenas se não existir
        admin = User(
            username=ADMIN_EMAIL,  # Usando o email como username
            email=ADMIN_EMAIL,
            hashed_password=User.get_password_hash(ADMIN_PASSWORD)
        )

        # Adicionar ao banco
        db.add(admin)
        db.commit()
        print(f"Usuário admin criado com sucesso!")
        print(f"Email: {ADMIN_EMAIL}")
    else:
        print(f"Usuário admin {ADMIN_EMAIL} já existe, pulando criação")

except Exception as e:
    print(f"Erro ao conectar ao banco de dados ou criar usuário admin: {str(e)}")
    sys.exit(1)
finally:
    db.close()
