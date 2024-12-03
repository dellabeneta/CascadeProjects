from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine, Base, SessionLocal
from app.routes import pessoa, auth
from app.core.init_admin import ensure_master_user

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Criar a aplicação FastAPI
app = FastAPI(
    title="Sistema de Cadastro de Pessoas",
    description="API para gerenciamento de cadastro de pessoas",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Criar usuário master na inicialização
db = SessionLocal()
try:
    ensure_master_user(db)
finally:
    db.close()

# Incluir as rotas
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(pessoa.router)

# Rota raiz
@app.get("/")
def read_root():
    """Rota inicial da API"""
    return {
        "message": "Bem-vindo à API de Cadastro de Pessoas",
        "docs": "/docs",  # Swagger UI
        "redoc": "/redoc"  # ReDoc
    }
