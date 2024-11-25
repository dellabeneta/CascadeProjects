# Backend do Sistema de Cadastro

Sistema de gerenciamento de pessoas desenvolvido com FastAPI e PostgreSQL.

## Tecnologias Utilizadas

- **Python 3.11**: Linguagem de programação
- **FastAPI**: Framework web
- **PostgreSQL 15**: Banco de dados
- **SQLAlchemy**: ORM para banco de dados
- **Pydantic**: Validação de dados

## Dependências

Principais dependências do projeto:

```
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
pydantic[email]==2.5.1
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
psycopg2-binary==2.9.9
Faker==20.1.0
```

## Banco de Dados

O sistema utiliza PostgreSQL 15 como banco de dados. A conexão é gerenciada através da variável de ambiente `DATABASE_URL`.

### Configuração do PostgreSQL

- Host: localhost (ou 'postgres' no Docker)
- Porta: 5432
- Usuário: postgres
- Senha: postgres
- Database: sistema_cadastro

## Documentação da API

- Swagger UI: /docs
- ReDoc: /redoc

## Scripts Utilitários

- `create_admin_simple.py`: Cria um usuário admin (admin/admin)
- `create_fake_pessoas.py`: Cria 200 pessoas com dados aleatórios
- `verify_admin.py`: Verifica se o usuário admin existe
- `wait-for-postgres.py`: Aguarda o PostgreSQL estar pronto
- `init.sh`: Script de inicialização que cria admin e dados fake
