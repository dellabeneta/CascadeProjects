from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Garantir que o diretório data existe
os.makedirs("./data", exist_ok=True)

# URL de conexão com o SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./data/sql_app.db"

# Criar engine do SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Criar classe de sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar classe base para os modelos
Base = declarative_base()

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
