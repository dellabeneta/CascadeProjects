# 🛠 Bitscrafting: Análise Técnica Detalhada

## 📜 Arquitetura de Scripts do Projeto

### Visão Geral dos Scripts

#### 1. `scripts/environment.sh`
**Objetivo**: Script abrangente para gerenciamento de ambiente

**Principais Recursos**:
- Suporte a múltiplos ambientes (dev, qa, prod)
- Carregamento dinâmico de variáveis de ambiente
- Orquestração com Docker Compose
- Exibição de URLs de recursos após a inicialização

**Fluxo de Trabalho**:
```bash
# Iniciar ambiente
./scripts/environment.sh start dev

# Parar ambiente
./scripts/environment.sh stop dev
```

**Carregamento de Variáveis de Ambiente**:
- Carrega ambiente base: `config/base/.env.base`
- Carrega configuração específica do ambiente: `config/environments/{env}/.env.{env}`

#### 2. `Makefile`
**Objetivo**: Interface de comandos simplificada para tarefas de desenvolvimento

**Comandos Disponíveis**:
- `dev-up`: Iniciar ambiente de desenvolvimento
- `dev-down`: Parar ambiente de desenvolvimento
- `dev-logs`: Visualizar logs dos contêineres
- `dev-shell`: Acessar shell do contêiner backend
- `clean`: Limpar recursos Docker

**Exemplos de Uso**:
```bash
# Iniciar ambiente de desenvolvimento
make dev-up

# Parar ambiente de desenvolvimento
make dev-down

# Acessar shell do backend
make dev-shell
```

#### 3. `docker-apocalypse.sh`
**Objetivo**: Limpeza abrangente do ambiente Docker

**Funcionalidade**:
- Para todos os contêineres em execução
- Remove todos os contêineres
- Remove todas as imagens
- Remove todos os volumes
- Remove todas as redes

**Cuidado**: Operação destrutiva, use com cuidado

**Uso Recomendado**:
```bash
# Dar permissão de execução
chmod +x docker-apocalypse.sh

# Executar limpeza
./docker-apocalypse.sh
```

### 🔧 Considerações Técnicas

#### Fluxo de Inicialização do Ambiente
1. O script `environment.sh` é chamado
2. Arquivos `.env` específicos do ambiente são carregados
3. Arquivos de configuração do Docker Compose são mesclados
4. Contêineres são construídos e iniciados
5. URLs dos recursos são exibidas

#### Configuração do Docker Compose
- Configuração base: `config/base/docker-compose.base.yml`
- Configuração específica do ambiente: `config/environments/{env}/docker-compose.{env}.yml`

### 🚨 Práticas Recomendadas

1. **Nunca comite informações sensíveis**
   - Use `.env.example` como modelo
   - Mantenha arquivos `.env` reais no `.gitignore`

2. **Gerenciamento de Ambiente Consistente**
   - Sempre use `./scripts/environment.sh` para controle do ambiente
   - Evite comandos manuais do Docker Compose

3. **Limpeza de Recursos**
   - Use `docker-apocalypse.sh` para reset completo
   - Seja cuidadoso com volumes de dados

### 🔍 Dicas de Depuração

- Verifique logs dos contêineres: `make dev-logs`
- Acesse shell do contêiner: `make dev-shell`
- Verifique variáveis de ambiente: Revise arquivos `.env`

### 📊 Otimização de Desempenho

- Use builds de múltiplos estágios do Docker
- Minimize a contagem de camadas nos Dockerfiles
- Use `.dockerignore` para reduzir o contexto de build

## 🤝 Contribuindo para a Arquitetura de Scripts

1. Mantenha a legibilidade dos scripts
2. Adicione comentários explicando lógica complexa
3. Siga convenções de nomenclatura existentes
4. Teste scripts em diferentes ambientes

## 📝 Notas

Este documento fornece insights sobre a arquitetura de scripts do projeto. Sempre consulte a versão mais recente dos scripts e configurações.