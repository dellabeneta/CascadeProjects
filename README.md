# Gerenciamento de Pessoas - Aplicação CRUD

## Descrição do Projeto

Esta é uma aplicação completa de Gerenciamento de Pessoas, desenvolvida com uma arquitetura moderna de pilha completa (full-stack), utilizando:
- Backend: Python com FastAPI
- Frontend: React com Vite
- Banco de Dados: PostgreSQL
- Autenticação: JWT (JSON Web Tokens)

## Funcionalidades Principais

- Cadastro de pessoas
- Autenticação de usuários
- Listagem, edição e exclusão de registros
- Interface responsiva e moderna
- Validação de dados no backend e frontend

## Tecnologias Utilizadas

### Backend
- Framework: FastAPI
- ORM: SQLAlchemy
- Autenticação: 
  - Python-jose para geração de tokens
  - Bcrypt para hash de senhas
- Validação: Pydantic
- Banco de Dados: PostgreSQL (psycopg2)

### Frontend
- Biblioteca: React
- Gerenciamento de Estado: React Hooks
- Roteamento: React Router
- UI: Material-UI (MUI)
- Cliente HTTP: Axios
- Build: Vite

## Pré-requisitos

### Requisitos do Sistema
- Python 3.8+
- Node.js 18+
- npm 9+
- PostgreSQL 12+

### Dependências
- Todas as dependências do Python estão listadas em `backend/requirements.txt`
- Dependências do frontend estão em `frontend/package.json`

## Configuração do Projeto

### Configuração Recomendada (Ambiente Virtual)

1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/python-peoples-crud.git
cd python-peoples-crud
```

2. Configurar Backend
```bash
# Criar ambiente virtual (opcional, mas recomendado)
python3 -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate

# Instalar dependências
cd backend
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Edite o .env com suas configurações
```

3. Configurar Banco de Dados
- Crie um banco de dados PostgreSQL
- Atualize as credenciais no arquivo `.env`

4. Configurar Frontend
```bash
cd ../frontend
npm install
```

## Executando o Projeto

### Método Manual (Recomendado)

#### Backend
```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

#### Frontend
```bash
cd frontend
npm run dev
```

### Método Make (Para Desenvolvedores Experientes)

⚠️ Aviso: O Makefile usa `--break-system-packages`, o que pode causar conflitos no sistema.

```bash
# Instalar dependências
make install

# Executar backend e frontend
make run-all
```

## Scripts Disponíveis

### Backend
- `make backend-install`: Instala dependências do backend
- `make backend-run`: Inicia servidor de desenvolvimento do backend

### Frontend
- `make frontend-install`: Instala dependências do frontend
- `make frontend-run`: Inicia servidor de desenvolvimento do frontend

## Variáveis de Ambiente

Copie `.env.example` para `.env` e configure:
- `DATABASE_URL`: Conexão com banco de dados
- `SECRET_KEY`: Chave para geração de tokens JWT
- Outras configurações específicas do projeto

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Resolução de Problemas

- Verifique se todas as dependências estão instaladas
- Confirme que as variáveis de ambiente estão configuradas corretamente
- Consulte os logs do backend e frontend em caso de erros

## Licença

[Especifique a licença do projeto]

## Contato

[Adicione informações de contato ou link para issues]
