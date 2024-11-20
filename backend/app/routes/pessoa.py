from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import date

from app.core.database import get_db
from app.models.pessoa import Pessoa
from app.schemas.pessoa import PessoaCreate, PessoaUpdate, PessoaResponse

# Criar o router com prefixo /pessoas
router = APIRouter(
    prefix="/pessoas",
    tags=["pessoas"],
    responses={404: {"description": "Pessoa não encontrada"}}
)

@router.post("/", response_model=PessoaResponse, status_code=status.HTTP_201_CREATED)
def criar_pessoa(pessoa: PessoaCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova pessoa no sistema.
    
    Args:
        pessoa: Dados da pessoa a ser criada
        db: Sessão do banco de dados
    
    Returns:
        PessoaResponse: Dados da pessoa criada
    
    Raises:
        HTTPException: Se o email já estiver cadastrado
    """
    # Verificar se já existe pessoa com este email
    db_pessoa = db.query(Pessoa).filter(Pessoa.email == pessoa.email).first()
    if db_pessoa:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )
    
    # Criar nova pessoa
    db_pessoa = Pessoa(**pessoa.model_dump())
    db.add(db_pessoa)
    db.commit()
    db.refresh(db_pessoa)
    return db_pessoa

@router.get("/", response_model=List[PessoaResponse])
def listar_pessoas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Lista todas as pessoas cadastradas.
    
    Args:
        skip: Número de registros para pular (paginação)
        limit: Número máximo de registros a retornar
        db: Sessão do banco de dados
    
    Returns:
        List[PessoaResponse]: Lista de pessoas cadastradas
    """
    pessoas = db.query(Pessoa).offset(skip).limit(limit).all()
    return pessoas

@router.get("/{pessoa_id}", response_model=PessoaResponse)
def obter_pessoa(pessoa_id: int, db: Session = Depends(get_db)):
    """
    Obtém uma pessoa específica pelo ID.
    
    Args:
        pessoa_id: ID da pessoa
        db: Sessão do banco de dados
    
    Returns:
        PessoaResponse: Dados da pessoa encontrada
    
    Raises:
        HTTPException: Se a pessoa não for encontrada
    """
    pessoa = db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()
    if pessoa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pessoa não encontrada"
        )
    return pessoa

@router.put("/{pessoa_id}", response_model=PessoaResponse)
def atualizar_pessoa(
    pessoa_id: int,
    pessoa: PessoaUpdate,
    db: Session = Depends(get_db)
):
    """
    Atualiza os dados de uma pessoa específica.
    
    Args:
        pessoa_id: ID da pessoa
        pessoa: Dados a serem atualizados
        db: Sessão do banco de dados
    
    Returns:
        PessoaResponse: Dados atualizados da pessoa
    
    Raises:
        HTTPException: Se a pessoa não for encontrada
    """
    db_pessoa = db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()
    if db_pessoa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pessoa não encontrada"
        )
    
    # Atualizar apenas os campos fornecidos
    pessoa_data = pessoa.model_dump(exclude_unset=True)
    for key, value in pessoa_data.items():
        setattr(db_pessoa, key, value)
    
    db.commit()
    db.refresh(db_pessoa)
    return db_pessoa

@router.delete("/{pessoa_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_pessoa(pessoa_id: int, db: Session = Depends(get_db)):
    """
    Remove uma pessoa do sistema.
    
    Args:
        pessoa_id: ID da pessoa
        db: Sessão do banco de dados
    
    Raises:
        HTTPException: Se a pessoa não for encontrada
    """
    pessoa = db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()
    if pessoa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pessoa não encontrada"
        )
    
    db.delete(pessoa)
    db.commit()
