# Sistema de Cadastro de Pessoas - Frontend

Interface web moderna para o sistema de gerenciamento de pessoas.

## Tecnologias

- **React 18**: Biblioteca JavaScript para construção de interfaces
- **Vite**: Build tool e dev server
- **Material-UI 5.14.20**: Biblioteca de componentes React
- **React Router 6**: Navegação
- **Axios**: Cliente HTTP para requisições à API

## Dependências Principais

```json
{
  "react": "^18.3.1",
  "react-dom": "^18.3.1",
  "@mui/material": "^5.14.20",
  "@mui/icons-material": "^5.14.20",
  "@emotion/react": "^11.13.5",
  "@emotion/styled": "^11.13.5",
  "axios": "^1.7.7",
  "react-router-dom": "^6.28.0"
}
```

## Estrutura do Projeto

```
frontend/
├── src/
│   ├── components/        # Componentes React reutilizáveis
│   ├── contexts/         # Contextos React (tema, autenticação)
│   ├── pages/           # Páginas da aplicação
│   │   ├── ListaPessoas.jsx
│   │   ├── CadastrarPessoa.jsx
│   │   └── EditarPessoa.jsx
│   ├── services/        # Serviços e integrações
│   │   └── api.js
│   ├── App.jsx         # Componente principal
│   └── main.jsx        # Ponto de entrada
├── public/             # Arquivos públicos
├── index.html
└── package.json
```

## Funcionalidades

- Lista de pessoas com ações de editar/excluir
- Formulário de cadastro de pessoas
- Formulário de edição de pessoas
- Navegação entre páginas
- Interface responsiva e moderna
- Integração com API REST
- Suporte a temas Light & Dark

## Páginas

- `/`: Lista de pessoas cadastradas
- `/cadastrar`: Formulário de cadastro
- `/editar/:id`: Formulário de edição

## Configuração da API

O frontend está configurado para se conectar ao backend na porta 8000. 
A URL base da API pode ser configurada através da variável de ambiente `VITE_API_URL`.

## Temas

O sistema suporta dois temas:
- Light: Tema claro para uso diurno
- Dark: Tema escuro para uso noturno

A seleção do tema é persistida no navegador e pode ser alterada através do botão na barra de navegação.
