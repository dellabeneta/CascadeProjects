from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.models.user import User
from passlib.hash import bcrypt

# Criar banco e tabelas
engine = create_engine('sqlite:///sql_app.db')
Base.metadata.create_all(engine)

# Criar sessão
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# Criar usuário admin
admin = User(
    username="admin",
    email="admin@example.com",
    hashed_password=bcrypt.hash("admin")
)

# Adicionar ao banco
db.add(admin)
db.commit()
db.close()

print("Usuário admin criado:")
print("Username: admin")
print("Senha: admin")
