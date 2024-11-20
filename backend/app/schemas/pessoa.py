from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional

class PessoaBase(BaseModel):
    """Schema base com os campos comuns"""
    nome: str = Field(..., min_length=2, max_length=100, description="Nome completo da pessoa")
    email: str = Field(..., max_length=100, description="Endereço de email")
    telefone: Optional[str] = Field(None, max_length=20, description="Número de telefone")
    data_nascimento: date = Field(..., description="Data de nascimento")
    ativo: bool = Field(default=True, description="Status do cadastro")

class PessoaCreate(PessoaBase):
    """Schema para criação de pessoa - herda todos os campos do PessoaBase"""
    pass

class PessoaUpdate(BaseModel):
    """
    Schema para atualização de pessoa.
    Todos os campos são opcionais, pois podemos querer atualizar apenas alguns campos.
    """
    nome: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[str] = Field(None, max_length=100)
    telefone: Optional[str] = Field(None, max_length=20)
    data_nascimento: Optional[date] = None
    ativo: Optional[bool] = None

class PessoaResponse(PessoaBase):
    """
    Schema para resposta - herda do PessoaBase e adiciona o id.
    Usado para retornar dados da API.
    """
    id: int = Field(..., description="ID único da pessoa")

    class Config:
        """Configuração para permitir o uso de modelos SQLAlchemy"""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "nome": "João Silva",
                "email": "joao@email.com",
                "telefone": "(11) 98765-4321",
                "data_nascimento": "1990-01-01",
                "ativo": True
            }
        }
