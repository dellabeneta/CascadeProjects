# 🛠 Bitscrafting: Guia Técnico do Projeto

## 📑 Índice
1. [Arquitetura do Projeto](#arquitetura-do-projeto)
2. [Scripts e Automação](#scripts-e-automação)
3. [Ambientes e Configuração](#ambientes-e-configuração)
4. [Práticas de Desenvolvimento](#práticas-de-desenvolvimento)
5. [Troubleshooting](#troubleshooting)

## 🏗 Arquitetura do Projeto

### Backend (FastAPI)
- **Estrutura de Diretórios**:
  ```
  backend/
  ├── app/
  │   ├── api/         # Rotas e endpoints
  │   ├── core/        # Configurações centrais
  │   ├── models/      # Modelos SQLAlchemy
  │   ├── schemas/     # Schemas Pydantic
  │   └── services/    # Lógica de negócio
  ```

### Frontend (React)
- **Estrutura de Diretórios**:
  ```
  frontend/
  ├── src/
  │   ├── components/  # Componentes React
  │   ├── hooks/       # Custom hooks
  │   ├── pages/       # Páginas da aplicação
  │   ├── services/    # Serviços e API
  │   └── theme/       # Configuração de tema
  ```

## 🤖 Scripts e Automação

### 1. Scripts Principais

#### `environment.sh`
```bash
./scripts/environment.sh <comando> <ambiente>
```
- **Comandos**: start, stop, restart
- **Ambientes**: dev, qa, prod
- **Variáveis**: Carrega automaticamente do diretório config/

#### `docker-apocalypse.sh`
- **Uso**: Limpeza completa do ambiente Docker
- **Cuidado**: Remove TODOS os recursos Docker
- **Recomendação**: Use apenas em desenvolvimento

### 2. Makefile
```makefile
dev-up      # Inicia ambiente de desenvolvimento
dev-down    # Para ambiente de desenvolvimento
dev-logs    # Visualiza logs dos containers
dev-shell   # Acessa shell do backend
clean       # Limpa recursos Docker
```

## ⚙️ Ambientes e Configuração

### Estrutura de Configuração
```
config/
├── base/
│   ├── .env.base
│   └── docker-compose.base.yml
└── environments/
    ├── dev/
    │   ├── .env.dev
    │   └── docker-compose.dev.yml
    ├── qa/
    └── prod/
```

### Variáveis de Ambiente
- **Base**: Configurações comuns a todos ambientes
- **Ambiente-específico**: Sobrescreve configurações base
- **Sensíveis**: Nunca commitar .env reais

## 👨‍💻 Práticas de Desenvolvimento

### Backend
1. **Padrões de Código**
   - Use Type Hints
   - Docstrings em funções públicas
   - Testes para novas funcionalidades

2. **Banco de Dados**
   - Use migrations para alterações
   - Evite queries raw
   - Mantenha índices otimizados

### Frontend
1. **Componentes**
   - Componentização atômica
   - Props typing
   - Memoização quando necessário

2. **Estado**
   - Use React Query para cache
   - Context API para estado global
   - Local state quando possível

## 🔍 Troubleshooting

### Problemas Comuns

1. **Containers não iniciam**
   ```bash
   # Verifique logs
   make dev-logs
   
   # Verifique portas em uso
   sudo lsof -i :5173
   sudo lsof -i :8000
   ```

2. **Erro de permissão**
   ```bash
   # Ajuste permissões Docker
   sudo usermod -aG docker $USER
   newgrp docker
   ```

3. **Banco de dados**
   ```bash
   # Acesse PostgreSQL
   make dev-shell
   python -m scripts.verify_admin
   ```

### Logs e Monitoramento
- Use `make dev-logs` para todos containers
- Verifique `/backend/logs` para logs específicos
- Monitor Docker stats: `docker stats`

## 📝 Notas de Desenvolvimento

1. **Pull Requests**
   - Mantenha mudanças focadas
   - Inclua testes
   - Atualize documentação

2. **Segurança**
   - Nunca commite credenciais
   - Mantenha dependências atualizadas
   - Revise permissões de arquivos

3. **Performance**
   - Profile endpoints lentos
   - Otimize queries N+1
   - Monitore uso de memória