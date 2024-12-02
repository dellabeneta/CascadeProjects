# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [2.0.0] - 27/11/2024

### ⚠️ Breaking Changes
- Refatoração completa da arquitetura do projeto
- Nova estrutura de diretórios mais organizada
- Sistema de autenticação totalmente renovado

### ✨ Adicionado
- Nova interface com suporte a temas light/dark
- Sistema de busca avançado com filtros
- Documentação técnica detalhada (BITSCRAFTING.md)
- Novo sistema de logs e monitoramento
- Scripts de desenvolvimento aprimorados

### 🔧 Modificado
- Atualização de todas as dependências para versões mais recentes
- Melhoria significativa na performance do backend
- Interface mais intuitiva e responsiva
- Sistema de validação mais robusto
- Documentação completamente revisada

### 🔒 Segurança
- Novo sistema de autenticação JWT
- Melhor gerenciamento de sessões
- Proteção contra ataques comuns
- Validações mais rigorosas de entrada

### 🧹 Removido
- Código legado não utilizado
- Dependências obsoletas
- Scripts redundantes

## [1.3.0] - 25/11/2024

### Segurança
- Remoção de credenciais hardcoded do docker-compose.yml
- Implementação de variáveis de ambiente para configurações sensíveis
- Adição de .env.example com template de configuração segura
- Atualização do sistema de autenticação para usar variáveis de ambiente

### Documentação
- Reorganização completa do README.md para melhor clareza
- Adição de instruções detalhadas sobre variáveis de ambiente
- Remoção de informações redundantes e inconsistências
- Melhoria na documentação de segurança e configuração

### Alterado
- Removidas referências às imagens do Docker Hub no docker-compose.yml
- Configurado para usar apenas builds locais dos containers

## [1.2.0] - 24/11/2024

### Adicionado
- Migração do banco de dados de SQLite para PostgreSQL
- Suporte a múltiplas conexões simultâneas
- Melhor performance e escalabilidade
- Confirmação de segurança no script docker-apocalypse.sh
- Emojis nas mensagens do script docker-apocalypse.sh para melhor visualização
- Opção de cancelamento no script de limpeza Docker

### Alterado
- Configuração do banco de dados para usar PostgreSQL
- Atualização da documentação
- Simplificação dos scripts de inicialização
- Atualizado Material-UI para versões estáveis (5.14.20)
- Otimização das dependências do backend
- Melhorias na segurança do script docker-apocalypse.sh
- Atualização da documentação com novas configurações

### Removido
- Dependência do SQLite
- Scripts de migração desnecessários
- Dependências redundantes do backend (pydantic duplicado e bcrypt)
- Versões beta do Material-UI (@mui/material e @mui/icons-material)

### Segurança
- Tokens de autenticação agora expiram ao fechar o navegador
- Melhor gerenciamento de permissões do banco de dados
- Adicionada confirmação antes da limpeza do ambiente Docker
- Otimização das dependências para versões mais estáveis

## [1.1.0] - 24/11/2024

### Adicionado
- Script `docker-apocalypse.sh` para limpeza completa do ambiente Docker
- Suporte ao SQLite CLI no container backend
- Utilitário para gerenciamento do banco de dados via container

### Modificado
- Migração do armazenamento de token de localStorage para sessionStorage
- Melhoria na segurança da sessão do usuário
- Atualização do Dockerfile do backend para incluir sqlite3

### Segurança
- Tokens de autenticação agora expiram ao fechar o navegador
- Melhor gerenciamento de permissões do banco de dados

## [1.0.0] - 23/11/2024

### Adicionado
- Implementação de paginação no backend usando FastAPI
- Novo schema de paginação genérico em `/app/schemas/pagination.py`
- Script de geração de dados de teste com 200 registros
- Paginação no frontend usando Material-UI TablePagination
- Validação de campos únicos (CPF, email)

### Modificado
- Refatoração do componente ListaPessoas.jsx para suportar paginação
- Melhoria na formatação de dados de entrada (telefone, CPF)
- Simplificação do sistema de autenticação
- Atualização das credenciais padrão (usuário: admin, senha: admin)

### Removido
- Remoção de dependências não utilizadas (react-hook-form, yup)
- Scripts complexos de gerenciamento de usuários

### Segurança
- Implementação de validação de campos no backend
- Restrições de unicidade para CPF e email
- Desativação de autocompletar do navegador em campos sensíveis
