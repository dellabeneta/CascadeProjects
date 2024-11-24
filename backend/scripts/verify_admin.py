from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.models.user import User
import os

# Garantir que o diretório data existe
os.makedirs("./data", exist_ok=True)

# Criar banco e tabelas
engine = create_engine('sqlite:///./data/sql_app.db')

# Criar sessão
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# Buscar admin
admin = db.query(User).filter(User.username == "admin").first()

if admin:
    print("Usuário admin encontrado:")
    print(f"Username: {admin.username}")
    print(f"Email: {admin.email}")
    print(f"Senha hash: {admin.hashed_password}")
else:
    print("Usuário admin NÃO encontrado!")

db.close()
