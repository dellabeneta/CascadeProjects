## Status do Projeto

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/dellabeneta/python-peoples-crud/docker-publish.yml?label=Build)](https://github.com/dellabeneta/python-peoples-crud/actions)
[![GitHub License](https://img.shields.io/github/license/dellabeneta/python-peoples-crud)](https://github.com/dellabeneta/python-peoples-crud/blob/main/LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/dellabeneta/python-peoples-crud?include_prereleases)](https://github.com/dellabeneta/python-peoples-crud/releases)
![GitHub language count](https://img.shields.io/github/languages/count/dellabeneta/python-peoples-crud)
![GitHub top language](https://img.shields.io/github/languages/top/dellabeneta/python-peoples-crud)


# Sistema de Cadastro de Pessoas

## Descrição do Projeto
Um sistema completo de CRUD de pessoas com autenticação JWT, frontend em React, backend em FastAPI e banco de dados PostgreSQL.

## Pré-requisitos
- Docker
- Docker Compose
- Make (opcional, mas recomendado)

## Configuração Local

### 1. Clonar o Repositório
```bash
git clone <url-do-repositorio>
cd python-peoples-crud
```

### 2. Configurar Variáveis de Ambiente
```bash
cp .env.example .env
```

### 3. Editar o `.env`
Abra o arquivo `.env` e configure as variáveis conforme necessário:

```
Configurações do Banco de Dados
POSTGRES_DB=sistema_cadastro
POSTGRES_USER=app_user
POSTGRES_PASSWORD=SenhaPostgres_Complexa_2024!
DATABASE_URL=postgresql://app_user:SenhaPostgres_Complexa_2024!@postgres:5432/sistema_cadastro

Configurações de Autenticação JWT
JWT_SECRET_KEY=ChaveSecretaJWT_NuncaCompartilhe_Maisde32Caracteres!
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

Configurações do Usuário Admin
ADMIN_USERNAME=admin_app
ADMIN_PASSWORD=SenhaAdmin_Forte_2024!@#
ADMIN_EMAIL=admin@seudominio.com
```

### 4. Iniciar o Projeto

#### Usando Make (Recomendado)
```bash
make up
```

#### Ou com Docker Compose Diretamente
```bash
docker compose -f config/docker-compose.yml --env-file .env up -d --build
```

## Acessar a Aplicação

- **Frontend**: http://localhost:5173
- **Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## Parar o Projeto

#### Usando Make
```bash
make down
```

#### Ou com Docker Compose
```bash
docker compose -f config/docker-compose.yml down
```

## Dicas Importantes

- Sempre use o `.env.example` como referência
- Não commite seu `.env` para o repositório
- As senhas padrão são fracas, então sempre personalize
- A primeira inicialização pode levar alguns minutos para baixar as imagens e configurar

## Credenciais Padrão

Se não configurar no `.env`, use:
- **Usuário**: admin
- **Senha**: admin
- **Email**: admin@example.com

## Tecnologias Utilizadas

- **Frontend**: React
- **Backend**: FastAPI
- **Banco de Dados**: PostgreSQL
- **Autenticação**: JWT
- **Containerização**: Docker

## Contribuição

Contribuições são bem-vindas! Para contribuir com este projeto, siga estas etapas:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas alterações (`git commit -m 'Adiciona NovaFeature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## Contato

- **Email**: m.dellabeneta@gmail.com  
- **GitHub**: https://github.com/dellabeneta        
- **Linkedin**: https://www.linkedin.com/in/mdellabeneta/

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

A Licença MIT é uma licença de software livre que permite:
- Uso comercial
- Modificação
- Distribuição
- Uso privado

Com as seguintes limitações:
- Responsabilidade limitada
- Garantia limitada

Consulte o arquivo LICENSE para os termos completos.
