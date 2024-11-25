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

## 🚀 Tecnologias Utilizadas

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
python-sistema-cadastro/
├── backend/                          # API REST em FastAPI
│   ├── app/                          # Código principal da aplicação
│   │   ├── core/                     # Configurações e utilitários core
│   │   ├── models/                   # Modelos do banco de dados
│   │   ├── routes/                   # Rotas da API
│   │   ├── schemas/                  # Schemas Pydantic
│   │   └── main.py                   # Ponto de entrada da aplicação
│   ├── scripts/                      # Scripts utilitários
│   ├── Dockerfile                    # Configuração do container
│   └── requirements.txt              # Dependências Python
│
├── frontend/                         # Interface web em React
│   ├── src/                          # Código fonte
│   │   ├── components/               # Componentes React reutilizáveis
│   │   ├── contexts/                 # Contextos React
│   │   ├── pages/                    # Páginas da aplicação
│   │   ├── services/                 # Serviços e integrações
│   │   ├── App.jsx                   # Componente principal
│   │   └── main.jsx                  # Ponto de entrada
│   ├── public/                       # Arquivos públicos
│   ├── Dockerfile                    # Configuração do container
│   └── package.json                  # Dependências Node.js
│
├── docker-apocalypse.sh              # Script de limpeza do ambiente Docker
├── docker-compose.yml                # Configuração dos containers
└── docs/                             # Documentação e assets
    └── images/                       # Screenshots e imagens
```

## 🚀 Como Executar

### Usando Docker (Recomendado)

1. Clone o repositório:
```bash
git clone <repository-url>
cd python-sistema-cadastro
```

2. Dê permissão de execução ao script de limpeza:
```bash
chmod +x docker-apocalypse.sh
```

3. Inicie os containers:
```bash
docker compose up -d
```

4. Acesse:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- Documentação API: http://localhost:8000/docs

Para limpar completamente o ambiente Docker (use com cautela):
```bash
./docker-apocalypse.sh
```

## 🔧 Configurações

### Backend
- Python 3.11+
- FastAPI com dependências otimizadas
- PostgreSQL 15 para persistência de dados
- Pydantic para validação de dados

### Frontend
- React 18
- Material-UI 5.14.20 (versão estável)
- Vite para build e desenvolvimento
- Axios para requisições HTTP

### Docker
- Containers isolados para cada serviço
- Script de limpeza com confirmação de segurança
- Volumes persistentes para dados

## 📱 Acessando o Sistema

- Frontend: http://localhost:5173
- API Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

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

💼 Este projeto de estudos está aberto a colaborações!
