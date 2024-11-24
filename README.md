## 📫 Contato

Desenvolvido por Michel Dellabeneta 👋

[![LinkedIn](https://img.shields.io/badge/-Michel%20Dellabeneta-blue?style=flat-square&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/mdellabeneta/)](https://www.linkedin.com/in/mdellabeneta/)
[![GitHub](https://img.shields.io/badge/-dellabeneta-gray?style=flat-square&logo=github&logoColor=white&link=https://github.com/dellabeneta/)](https://github.com/dellabeneta/)
[![Gmail](https://img.shields.io/badge/-m.dellabeneta@gmail.com-red?style=flat-square&logo=gmail&logoColor=white&link=mailto:m.dellabeneta@gmail.com)](mailto:m.dellabeneta@gmail.com)
[![Linktree](https://img.shields.io/badge/-Linktree-green?style=flat-square&logo=linktree&logoColor=white&link=https://linktr.ee/dellabeneta)](https://linktr.ee/dellabeneta)

💼 Este projeto de estudos está aberto a colaborações!

# Sistema de Cadastro de Pessoas

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
- Python 3.x
- FastAPI (Framework web)
- SQLite (Banco de dados)
- SQLAlchemy (ORM)
- Pydantic (Validação de dados)
- Uvicorn (Servidor ASGI)

### Frontend
- React 18
- Material-UI (MUI)
- React Router
- Axios
- Vite

## 🛠️ Estrutura do Projeto

```
python-sistema-cadastro/
├── backend/                 # API REST em FastAPI
│   ├── app/                # Código principal da aplicação
│   │   ├── core/          # Configurações e utilitários core
│   │   ├── models/        # Modelos do banco de dados
│   │   ├── routes/        # Rotas da API
│   │   ├── schemas/       # Schemas Pydantic
│   │   └── main.py       # Ponto de entrada da aplicação
│   ├── scripts/           # Scripts utilitários
│   └── requirements.txt   # Dependências Python
│
├── frontend/              # Interface web em React
│   ├── src/              # Código fonte
│   │   ├── components/   # Componentes React reutilizáveis
│   │   ├── contexts/     # Contextos React
│   │   ├── pages/        # Páginas da aplicação
│   │   ├── services/     # Serviços e integrações
│   │   ├── App.jsx       # Componente principal
│   │   └── main.jsx      # Ponto de entrada
│   ├── public/           # Arquivos públicos
│   └── package.json      # Dependências Node.js
│
└── docs/                 # Documentação e assets
    └── images/          # Screenshots e imagens
```

## 🚀 Como Executar

### Backend

1. Entre na pasta do backend:
```bash
cd backend
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o servidor:
```bash
uvicorn app.main:app --reload --port 8000
```

### Frontend

1. Entre na pasta do frontend:
```bash
cd frontend
```

2. Instale as dependências:
```bash
npm install
```

3. Execute o servidor de desenvolvimento:
```bash
npm run dev
```

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

## 🚀 Melhorias para Produção

Lista de melhorias e ajustes necessários para preparar o sistema para um ambiente de produção:

### 1. 🔒 Segurança
- Configuração adequada de CORS
- Implementação de autenticação e autorização (JWT/OAuth2)
- Rate limiting para prevenção de abusos
- Configuração de HTTPS/SSL
- Remoção de informações sensíveis de logs e mensagens de erro

### 2. 🗄️ Banco de Dados
- Migração para banco de dados de produção (PostgreSQL/MySQL)
- Implementação de backups automáticos
- Configuração de pools de conexão
- Otimização com índices adequados
- Sistema de migrations para controle de versão

### 3. ⚡ Performance e Escalabilidade
- Implementação de sistema de cache (Redis/Memcached)
- Otimização de consultas ao banco
- Configuração de compressão de respostas
- Implementação de paginação em listagens
- Configuração de load balancing

### 4. 📊 Monitoramento e Logs
- Sistema de logging estruturado
- Monitoramento de performance (New Relic/Datadog)
- Sistema de alertas para erros
- Implementação de health checks
- Métricas de negócio

### 5. 🔄 CI/CD
- Pipeline de integração contínua
- Testes automatizados (unitários/integração/e2e)
- Sistema de deploy automatizado
- Configuração de ambientes (dev/staging/prod)
- Linting e formatação de código

### 6. 🎨 Frontend
- Minificação e otimização de assets
- Implementação de lazy loading
- Otimização de imagens e recursos
- Capacidades de PWA
- Implementação de error boundaries

### 7. 📚 Documentação
- Processo de deploy
- Guia de troubleshooting
- Documentação da arquitetura
- Swagger/OpenAPI completo
- Documentação de variáveis de ambiente

### 8. 🏗️ Infraestrutura
- Containerização com Docker
- Orquestração (Kubernetes se necessário)
- Configuração de CDN
- Sistema de backups
- Plano de disaster recovery

### 9. 🔐 Gestão de Secrets e Configurações
- Mover SECRET_KEY do JWT para variável de ambiente
- Configurar demais variáveis de JWT (ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES)
- Criar arquivo .env.example com template das variáveis
- Adicionar .env ao .gitignore
- Implementar validação de variáveis de ambiente obrigatórias
- Configurar caminho do banco SQLite via variável de ambiente
- Preparar estrutura para secrets futuros (email, APIs externas, etc)
- Implementar rotação automática de secrets
- Considerar uso de cofre de secrets (HashiCorp Vault, AWS Secrets Manager)

### 10. 💻 Código
- Remoção de código de debug
- Otimização de imports
- Validações mais robustas
- Tratamento de erros completo
- Implementação de tipos estáticos

### 11. 🌟 Boas Práticas de Produção
- Versionamento de API
- Políticas de retry
- Implementação de circuit breakers
- Configuração de timeouts
- Graceful shutdown

## 📫 Contato

Desenvolvido por Michel Dellabeneta 👋

[![LinkedIn](https://img.shields.io/badge/-Michel%20Dellabeneta-blue?style=flat-square&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/mdellabeneta/)](https://www.linkedin.com/in/mdellabeneta/)
[![GitHub](https://img.shields.io/badge/-dellabeneta-gray?style=flat-square&logo=github&logoColor=white&link=https://github.com/dellabeneta/)](https://github.com/dellabeneta/)
[![Gmail](https://img.shields.io/badge/-m.dellabeneta@gmail.com-red?style=flat-square&logo=gmail&logoColor=white&link=mailto:m.dellabeneta@gmail.com)](mailto:m.dellabeneta@gmail.com)
[![Linktree](https://img.shields.io/badge/-Linktree-green?style=flat-square&logo=linktree&logoColor=white&link=https://linktr.ee/dellabeneta)](https://linktr.ee/dellabeneta)

💼 Este projeto de estudos está aberto a colaborações!
