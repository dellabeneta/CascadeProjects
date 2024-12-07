from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# URL de conexão com o PostgreSQL
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/sistema_cadastro"
)

# Configurações SSL para banco de dados na nuvem
ssl_args = {}
if os.getenv("DATABASE_SSL_MODE"):
    ssl_args = {
        "ssl_mode": os.getenv("DATABASE_SSL_MODE", "require"),
    }

# Criar engine do SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args=ssl_args
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
