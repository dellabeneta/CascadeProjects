from pydantic import BaseModel, EmailStr, Field, validator
from datetime import date, datetime
from typing import Optional
import re

class PessoaBase(BaseModel):
    """Schema base com os campos comuns"""
    nome: str = Field(..., min_length=2, max_length=100, description="Nome completo da pessoa")
    email: str = Field(..., max_length=100, description="Endereço de email")
    telefone: str = Field(..., max_length=20, description="Número de telefone")
    cpf: str = Field(..., max_length=14, description="CPF da pessoa")
    data_nascimento: date = Field(..., description="Data de nascimento")
    ativo: bool = Field(default=True, description="Status do cadastro")

    @validator('data_nascimento', pre=True)
    def parse_data_nascimento(cls, v):
        if isinstance(v, str):
            try:
                # Aceitar apenas formato dd/mm/yyyy
                return datetime.strptime(v, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("Data deve estar no formato dd/mm/yyyy")
        return v

    @validator('cpf')
    def validate_cpf(cls, v):
        # Garantir que o CPF está no formato correto
        if not re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", v):
            raise ValueError("CPF deve estar no formato 000.000.000-00")
        return v

    @validator('telefone')
    def validate_telefone(cls, v):
        # Garantir que o telefone está no formato correto
        if not re.match(r"\(\d{2}\) \d-\d{4}-\d{4}", v):
            raise ValueError("Telefone deve estar no formato (XX) X-XXXX-XXXX")
        return v

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
    cpf: Optional[str] = Field(None, max_length=14)
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
                "cpf": "123.456.789-01",
                "data_nascimento": "1990-01-01",
                "ativo": True
            }
        }
