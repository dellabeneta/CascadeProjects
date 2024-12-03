# Pessoas CRUD 👥

Uma aplicação moderna de gerenciamento de cadastros, construída com Python e React.

## 🚀 Visão Geral

Sistema completo para cadastro e gerenciamento de pessoas, oferecendo uma experiência de usuário intuitiva e responsiva.

## ✨ Recursos Principais

- Sistema completo de autenticação e autorização
- CRUD completo de pessoas com validações
- Interface moderna e responsiva com Material-UI
- Suporte a temas light e dark
- Documentação interativa da API com Swagger/OpenAPI
- Containerização completa com Docker
- Ambiente de desenvolvimento otimizado

## 📸 Interface

### Temas Adaptáveis
Experimente a interface em diferentes temas:

<div align="center">
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
</div>

### Documentação da API
Interface Swagger para exploração dos endpoints:

<div align="center">
  <img src="docs/images/api-docs.png" alt="API Docs" width="800"/>
</div>

## 🛠 Tecnologias

### Backend
- **Framework**: FastAPI
- **Linguagem**: Python 3.11+
- **ORM**: SQLAlchemy
- **Autenticação**: JWT
- **Documentação**: OpenAPI (Swagger)

### Frontend
- **Framework**: React 18
- **Estilização**: Material-UI
- **Gerenciamento de Estado**: React Query
- **Formulários**: React Hook Form

### Infraestrutura
- **Banco de Dados**: PostgreSQL 15
- **Containerização**: Docker & Docker Compose
- **CI/CD**: GitHub Actions

## 🏁 Começando

### 📋 Pré-requisitos

Antes de começar, certifique-se de que seu ambiente atenda aos seguintes requisitos:

- **Sistema Operacional**
  - Linux (recomendado)
  - macOS
  - Windows (com WSL2)

- **Ferramentas Necessárias**
  - 🐳 Docker (versão 20.10 ou superior)
  - 🐳 Docker Compose (versão 1.29 ou superior)
  - 🖥️ Bash (shell script)
  - 🌐 Conexão com a internet para download de imagens

- **Recursos de Hardware**
  - Mínimo: 4GB RAM
  - Recomendado: 8GB RAM
  - Espaço em disco: 5GB livres

- **Portas Necessárias**
  - Porta 5173 (Frontend)
  - Porta 8000 (Backend)
  - Porta 5432 (PostgreSQL)

- **Verificação Rápida**
  ```bash
  # Verifique as versões
  docker --version
  docker compose version
  ```

### ⚠️ Notas Importantes

- Certifique-se de que as portas especificadas não estejam em uso por outros serviços
- Usuário deve ter permissões para executar comandos Docker
- Recomenda-se fechar outros containers ou aplicações que possam conflitar

### 🚀 Iniciando o Projeto

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/dellabeneta/python-peoples-crud.git
   cd python-peoples-crud
   ```

2. **Configure o Ambiente**
   ```bash
   # Copie o arquivo de exemplo de variáveis de ambiente
   cp .env.example .env
   
   # Ajuste as variáveis conforme necessário
   nano .env
   ```

3. **Inicie o Ambiente de Desenvolvimento**
   ```bash
   # Usando o script de ambiente
   ./scripts/environment.sh start dev
   
   # OU usando make
   make dev-up
   ```

4. **Acesse a Aplicação**
   - Frontend: http://localhost:5173
   - API Docs: http://localhost:8000/docs
   - Admin: http://localhost:8000/admin

### 🔑 Credenciais Padrão

Para acessar o sistema pela primeira vez, use as seguintes credenciais de administrador:

```
Username: admin
Password: admin
Email: admin@example.com
```

**Importante**: Por segurança, recomenda-se alterar a senha do administrador após o primeiro acesso.

### 📚 Documentação Adicional

- [Guia de Desenvolvimento](./BITSCRAFTING.md)
- [Changelog](./CHANGELOG.md)
- [Contribuição](./CONTRIBUTING.md)

### 🔧 Comandos Úteis

```bash
# Visualizar logs
make dev-logs

# Acessar shell do backend
make dev-shell

# Parar o ambiente
make dev-down

# Limpar todos os recursos Docker
./docker-apocalypse.sh
```

### 🤝 Como Contribuir

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 🤝 Contribuição

Contribuições são bem-vindas!

## 📄 Licença

Este projeto está sob licença MIT.
