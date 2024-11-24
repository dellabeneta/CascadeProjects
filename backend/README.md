# Sistema de Cadastro de Pessoas - Backend

Sistema de gerenciamento de pessoas desenvolvido com FastAPI e SQLite.

## Tecnologias

- **Python 3.x**
- **FastAPI**: Framework web moderno e rápido
- **SQLite**: Banco de dados
- **SQLAlchemy**: ORM para banco de dados
- **Pydantic**: Validação de dados
- **Uvicorn**: Servidor ASGI
- **Python-dotenv**: Gerenciamento de variáveis de ambiente

## Dependências

```
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.1
python-dotenv==1.0.0
aiosqlite==0.19.0
```

## Estrutura do Projeto

```
backend/
├── app/
│   ├── core/
│   │   └── database.py
│   ├── models/
│   │   └── pessoa.py
│   ├── routes/
│   │   └── pessoa.py
│   ├── schemas/
│   │   └── pessoa.py
│   └── main.py
├── scripts/
│   └── criar_pessoas.py
└── requirements.txt
```

## Funcionalidades

- CRUD completo de pessoas
- Validação de dados
- Documentação automática (Swagger UI)
- Script para geração de dados de teste

## API Endpoints

- `GET /pessoas/`: Lista todas as pessoas
- `POST /pessoas/`: Cria uma nova pessoa
- `GET /pessoas/{id}`: Obtém uma pessoa específica
- `PUT /pessoas/{id}`: Atualiza uma pessoa
- `DELETE /pessoas/{id}`: Remove uma pessoa

## Modelos de Dados

### Pessoa

Modelo principal para armazenamento de dados pessoais.

#### Campos
- `id`: Integer (Primary Key)
- `nome`: String(100), obrigatório
- `email`: String(100), único, obrigatório
- `telefone`: String(20), opcional
- `data_nascimento`: Date, obrigatório
- `ativo`: Boolean, default=True

#### Validações
- Nome: mínimo 2 caracteres, máximo 100
- Email: formato válido, máximo 100 caracteres
- Telefone: máximo 20 caracteres
- Data nascimento: data válida
- Todos os campos permitem atualização parcial

## Como Executar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o servidor:
```bash
uvicorn app.main:app --reload --port 8000
```

3. Acesse a documentação:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
