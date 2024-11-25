# Backend do Sistema de Cadastro

Sistema de gerenciamento de pessoas desenvolvido com FastAPI e PostgreSQL.

## Tecnologias Utilizadas

- **Python 3.11**: Linguagem de programação
- **FastAPI**: Framework web
- **PostgreSQL**: Banco de dados
- **SQLAlchemy**: ORM para banco de dados
- **Pydantic**: Validação de dados
- **Docker**: Containerização

## Dependências

Principais dependências do projeto:

```
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.1
pydantic-settings==2.1.0
pydantic[email]==2.5.1
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
psycopg2-binary==2.9.9
```

## Como Executar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente:
```bash
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/sistema_cadastro"
```

3. Execute o servidor:
```bash
uvicorn app.main:app --reload
```

O servidor estará disponível em http://localhost:8000

## Documentação da API

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Scripts Úteis

- `create_admin_simple.py`: Cria um usuário admin (admin/admin)
- `create_fake_pessoas.py`: Cria 200 pessoas com dados aleatórios
- `verify_admin.py`: Verifica se o usuário admin existe
- `init.sh`: Script de inicialização que cria admin, dados fake e inicia o servidor
