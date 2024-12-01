from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.models.user import User
import os

# URL de conexão com o PostgreSQL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@postgres:5432/sistema_cadastro"
)

# Criar banco e tabelas
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Criar sessão
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# Verificar se o admin já existe
existing_admin = db.query(User).filter(User.username == "admin").first()

if not existing_admin:
    # Criar usuário admin apenas se não existir
    admin = User(
        username="admin",
        email="admin@example.com",
        hashed_password=User.get_password_hash("admin")
    )

    # Adicionar ao banco
    db.add(admin)
    db.commit()
    print("Usuário admin criado:")
    print("Username: admin")
    print("Senha: admin")
else:
    print("Usuário admin já existe, pulando criação")

db.close()
