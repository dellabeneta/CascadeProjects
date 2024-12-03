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
- **Make** (para configuração rápida do projeto)

### Dependências
- Todas as dependências do Python estão listadas em `backend/requirements.txt`
- Dependências do frontend estão em `frontend/package.json`

## Configuração do Projeto

### 🚀 Método Rápido: Usando Make

⚠️ **Importante: Leia o Makefile Antes de Usar**

O projeto fornece um `Makefile` para configuração e execução rápida. **Recomendamos fortemente ler o arquivo `Makefile` completamente antes de executar qualquer comando.**

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/python-peoples-crud.git
cd python-peoples-crud

# Instalar todas as dependências (backend e frontend)
make install

# Iniciar backend e frontend simultaneamente
make run-all
```

#### ⚠️ Aviso Importante sobre Make
- O Makefile usa `--break-system-packages`, o que pode causar conflitos no ambiente Python
- **Recomendado apenas para desenvolvedores experientes**
- Usuários menos experientes devem seguir o método manual de instalação

### 🛠 Método Manual de Instalação

Se preferir mais controle ou evitar potenciais conflitos de pacotes, siga o método manual:

#### 1. Configurar Backend (Python)

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/python-peoples-crud.git
cd python-peoples-crud

# Criar e ativar ambiente virtual (RECOMENDADO)
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências do backend
cd backend
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Edite o .env com suas configurações de banco de dados

# Iniciar servidor backend
uvicorn app.main:app --reload --port 8000
```

#### 2. Configurar Frontend (React)

```bash
# Na raiz do projeto ou em outro terminal
cd frontend

# Instalar dependências do frontend
npm install

# Iniciar servidor de desenvolvimento do frontend
npm run dev
```

### 🔍 Ordem de Inicialização

**Ordem Recomendada:**
1. Iniciar o Backend (Python/FastAPI)
2. Iniciar o Frontend (React)

Isso garante que o backend esteja disponível antes que o frontend tente fazer requisições.

### 💡 Dicas Adicionais

- Sempre verifique as variáveis de ambiente no `.env`
- Certifique-se de que o PostgreSQL está rodando
- Verifique as versões das dependências nos arquivos `requirements.txt` e `package.json`

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

## Contato e Suporte

### Autor
- **Nome**: Michel Torres Dellabeneta
- **Email**: m.dellabeneta@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/mdellabeneta/

## 🎨 Interface do Usuário

### Temas Dinâmicos

A aplicação oferece suporte a dois temas elegantes para melhorar a experiência do usuário:

#### Tema Claro
![Interface em Tema Claro](/docs/images/login-light.png)

#### Tema Escuro
![Interface em Tema Escuro](/docs/images/login-dark.png)

Os temas podem ser alternados facilmente, proporcionando:
- Conforto visual em diferentes condições de iluminação
- Redução da fadiga ocular
- Personalização da experiência do usuário

### Documentação da API

Além da interface de usuário, o projeto inclui documentação completa da API:

![Documentação da API](/docs/images/api-docs.png)

A documentação interativa da API, gerada automaticamente pelo FastAPI, permite:
- Exploração fácil dos endpoints
- Teste direto dos métodos
- Descrição detalhada dos parâmetros e respostas