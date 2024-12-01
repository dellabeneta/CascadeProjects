# Pessoas CRUD 👥

Uma aplicação moderna de gerenciamento de cadastros, construída com Python e React.

## 🚀 Visão Geral

Sistema completo para cadastro e gerenciamento de pessoas, oferecendo uma experiência de usuário intuitiva e responsiva.

## ✨ Recursos Principais

- Cadastro de pessoas
- Edição de registros
- Exclusão de dados
- Interface responsiva
- Suporte a temas light e dark

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

- **Backend**: Python, FastAPI
- **Frontend**: React
- **Banco de Dados**: PostgreSQL
- **Containerização**: Docker

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

### Instalação Rápida

```bash
# Clonar o repositório
git clone https://github.com/dellabeneta/python-peoples-crud.git

# Entrar no diretório
cd python-peoples-crud

# Iniciar ambiente de desenvolvimento
./scripts/environment.sh start dev
```

## 🤝 Contribuição

Contribuições são bem-vindas!
## 📄 Licença

Este projeto está sob licença MIT.
