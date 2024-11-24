# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2024-01-09

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
