# Sistema de Cadastro de Pessoas - Frontend

Interface web moderna para o sistema de gerenciamento de pessoas.

## Tecnologias

- **React**: Biblioteca JavaScript para construção de interfaces
- **Vite**: Build tool e dev server
- **Material-UI (MUI)**: Biblioteca de componentes React
- **React Router**: Navegação
- **Axios**: Cliente HTTP para requisições à API

## Dependências Principais

```json
{
  "react": "^18.2.0",
  "react-dom": "^18.2.0",
  "@mui/material": "^5.x",
  "@mui/icons-material": "^5.x",
  "@emotion/react": "^11.x",
  "@emotion/styled": "^11.x",
  "axios": "^1.x",
  "react-router-dom": "^6.x"
}
```

## Estrutura do Projeto

```
frontend/
├── src/
│   ├── components/
│   ├── pages/
│   │   ├── ListaPessoas.jsx
│   │   ├── CadastrarPessoa.jsx
│   │   └── EditarPessoa.jsx
│   ├── services/
│   │   └── api.js
│   ├── App.jsx
│   └── main.jsx
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

## Páginas

- `/`: Lista de pessoas cadastradas
- `/cadastrar`: Formulário de cadastro
- `/editar/:id`: Formulário de edição

## Como Executar

1. Instale as dependências:
```bash
npm install
```

2. Execute o servidor de desenvolvimento:
```bash
npm run dev
```

3. Acesse a aplicação:
- URL: http://localhost:5173

## Configuração

O frontend está configurado para se conectar ao backend na porta 8000. 
Certifique-se de que o backend esteja rodando antes de iniciar o frontend.
