# Sistema de Cadastro de Pessoas (Famigerado CRUD)

Sistema completo para gerenciamento de pessoas, com backend em FastAPI e frontend em React.

## 📸 Screenshots

<div align="center">

### 🌓 Temas Light & Dark
*Tela de login com suporte a múltiplos temas*
<table>
  <tr>
    <td align="center" width="50%">
      <strong>Tema Light</strong><br/>
      <img src="docs/images/login-light.png" alt="Login - Tema Light" width="400"/>
    </td>
    <td align="center" width="50%">
      <strong>Tema Dark</strong><br/>
      <img src="docs/images/login-dark.png" alt="Login - Tema Dark" width="400"/>
    </td>
  </tr>
</table>

### 📚 Documentação da API
*Interface Swagger com todos os endpoints documentados*
<img src="docs/images/api-docs.png" alt="API Docs" width="800"/>

</div>

## 📋 Visão Geral

O sistema permite gerenciar cadastros de pessoas com as seguintes funcionalidades:
- Listagem de pessoas
- Cadastro de nova pessoa
- Edição de dados
- Exclusão de registro
- Interface web moderna e responsiva

## ⚙️ Tecnologias Utilizadas

### Backend
- Python 3.11
- FastAPI (Framework Web)
- PostgreSQL 15 (Banco de dados)
- SQLAlchemy (ORM)
- Pydantic
- Docker
- Uvicorn (Servidor ASGI)

### Frontend
- React 18
- Material-UI 5.14.20
- React Router
- Axios
- Vite

## 🛠️ Estrutura do Projeto

```
python-peoples-crud/
├── backend/                          # API REST em FastAPI
│   ├── app/                          # Código principal da aplicação
│   │   ├── core/                     # Configurações e utilitários core
│   │   ├── models/                   # Modelos do banco de dados
│   │   ├── routes/                   # Rotas da API
│   │   ├── schemas/                  # Schemas Pydantic
│   │   └── main.py                   # Ponto de entrada da aplicação
│   ├── scripts/                      # Scripts utilitários
│   │   ├── create_admin_simple.py    # Cria usuário admin
│   │   ├── create_fake_pessoas.py    # Gera dados de teste
│   │   ├── wait-for-postgres.py      # Aguarda DB estar pronto
│   │   ├── verify_admin.py          # Verifica usuário admin
│   │   └── init.sh                   # Script de inicialização
│   ├── Dockerfile                    # Configuração do container
│   └── requirements.txt              # Dependências Python
│
├── frontend/                         # Interface web em React
│   ├── src/                         # Código fonte
│   │   ├── components/              # Componentes React reutilizáveis
│   │   ├── contexts/                # Contextos React
│   │   ├── pages/                   # Páginas da aplicação
│   │   ├── services/                # Serviços e integrações
│   │   ├── App.jsx                  # Componente principal
│   │   └── main.jsx                 # Ponto de entrada
│   ├── public/                      # Arquivos públicos
│   ├── Dockerfile                   # Configuração do container
│   ├── package.json                 # Dependências Node.js
│   └── vite.config.js               # Configuração do Vite
│
├── docs/                            # Documentação e assets
│   └── images/                      # Screenshots e imagens
│       ├── login-light.png          # Screenshot tema claro
│       ├── login-dark.png           # Screenshot tema escuro
│       └── api-docs.png             # Screenshot documentação API
│
├── .env.example                     # Exemplo de variáveis de ambiente
├── docker-apocalypse.sh             # Script de limpeza do ambiente Docker
├── docker-compose.yml               # Configuração dos containers
├── CHANGELOG.md                     # Histórico de mudanças
└── README.md                        # Documentação principal
```

## 🔧 Configurações

### Variáveis de Ambiente

O projeto utiliza variáveis de ambiente para configuração. Crie um arquivo `.env` baseado no `.env.example`:

1. Copie o arquivo de exemplo:
```bash
cp .env.example .env
```

2. Configure as variáveis no arquivo `.env`:
```env
# Banco de Dados
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha_segura
POSTGRES_DB=sistema_cadastro
DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}

# JWT Authentication
JWT_SECRET_KEY=sua_chave_secreta_muito_segura
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

# Backend
BACKEND_CORS_ORIGINS=["http://localhost:5173","http://localhost:3000"]
```

## 🚀 Como Executar

### Usando Docker (Recomendado)

O projeto utiliza apenas builds locais dos containers, garantindo que você sempre execute a versão mais recente do código. No `docker-compose.yml`, a diretiva `build` força a construção local das imagens:

```yaml
# Exemplo do docker-compose.yml
backend:
  build:            # Essa configuração garante build local
    context: ./backend
    dockerfile: Dockerfile

frontend:
  build:            # Essa configuração garante build local
    context: ./frontend
    dockerfile: Dockerfile
```

> **Nota**: O projeto NÃO utiliza imagens pré-construídas do Docker Hub. Todas as imagens são construídas localmente a partir do código fonte.

Para executar:

1. Clone o repositório:
```bash
git clone <repository-url>
cd python-peoples-crud
```

2. Dê permissão de execução ao script de limpeza:
```bash
chmod +x docker-apocalypse.sh
```

3. Inicie os containers:
```bash
docker compose up -d
```

4. Acesse o sistema:
- Frontend: http://localhost:5173
- Documentação API: http://localhost:8000/docs ou http://localhost:8000/redoc

Para limpar completamente o ambiente Docker (use com cautela):
```bash
./docker-apocalypse.sh
```

## 🔍 Funcionalidades Principais

1. Gerenciamento de Pessoas
   - Cadastro com nome, email, telefone, data de nascimento
   - Status ativo/inativo
   - Validação de dados
   - Interface intuitiva

2. Listagem
   - Tabela com todas as informações
   - Ações de editar e excluir
   - Formatação adequada de datas

3. Formulários
   - Campos validados
   - Feedback de erros
   - Navegação intuitiva

## 📫 Contato

Desenvolvido por Michel Dellabeneta 👋

[![LinkedIn](https://img.shields.io/badge/-Michel%20Dellabeneta-blue?style=flat-square&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/mdellabeneta/)](https://www.linkedin.com/in/mdellabeneta/)
[![GitHub](https://img.shields.io/badge/-dellabeneta-gray?style=flat-square&logo=github&logoColor=white&link=https://github.com/dellabeneta/)](https://github.com/dellabeneta/)
[![Gmail](https://img.shields.io/badge/-m.dellabeneta@gmail.com-red?style=flat-square&logo=gmail&logoColor=white&link=mailto:m.dellabeneta@gmail.com)](mailto:m.dellabeneta@gmail.com)
[![Linktree](https://img.shields.io/badge/-Linktree-green?style=flat-square&logo=linktree&logoColor=white&link=https://linktr.ee/dellabeneta)](https://linktr.ee/dellabeneta)

Este projeto de estudos está aberto a colaborações!
