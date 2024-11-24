import sys
import os
import random
from datetime import datetime

# Adiciona o diretório pai ao PYTHONPATH
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(backend_dir)

# Muda o diretório de trabalho para o backend para que o SQLite encontre o banco de dados
os.chdir(backend_dir)

from app.core.database import SessionLocal, engine, Base
from app.models.pessoa import Pessoa

# Listas de nomes e sobrenomes comuns brasileiros
nomes = [
    "João", "Maria", "José", "Ana", "Pedro", "Paulo", "Carlos", "Lucas",
    "Marcos", "Gabriel", "Rafael", "Felipe", "Bruno", "Rodrigo", "Gustavo",
    "Daniel", "Marcelo", "Eduardo", "Leonardo", "André", "Luiz", "Ricardo",
    "Julia", "Beatriz", "Mariana", "Larissa", "Amanda", "Fernanda", "Patricia",
    "Camila", "Carolina", "Leticia", "Isabela", "Gabriela", "Manuela", "Sofia",
    "Alice", "Laura", "Valentina", "Helena", "Sophia", "Isabella", "Miguel",
    "Arthur", "Bernardo", "Heitor", "Davi", "Lorenzo", "Théo", "Noah", "Isaac"
]

sobrenomes = [
    "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves",
    "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho",
    "Almeida", "Lopes", "Soares", "Fernandes", "Vieira", "Barbosa", "Rocha",
    "Dias", "Nascimento", "Andrade", "Moreira", "Nunes", "Marques", "Machado",
    "Mendes", "Freitas", "Cardoso", "Ramos", "Gonçalves", "Santana", "Teixeira",
    "Moraes", "Correia", "Pinto", "Cruz", "Cunha", "Azevedo", "Cavalcanti"
]

def gerar_cpf():
    """Gera um CPF válido"""
    def calcula_digito(digs):
        mult = len(digs) + 1
        soma = sum(d * m for d, m in zip(digs, range(mult, 1, -1)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    # Gera os primeiros 9 dígitos
    cpf = [random.randint(0, 9) for _ in range(9)]
    
    # Adiciona dígitos verificadores
    cpf.append(calcula_digito(cpf))
    cpf.append(calcula_digito(cpf))
    
    # Formata o CPF
    cpf_str = ''.join(map(str, cpf))
    return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"

def gerar_telefone():
    """Gera um número de celular no formato (XX) 9-XXXX-XXXX"""
    ddd = random.randint(11, 99)
    numero = random.randint(10000000, 99999999)
    return f"({ddd}) 9-{str(numero)[:4]}-{str(numero)[4:]}"

def gerar_data_nascimento():
    """Gera uma data de nascimento entre 1960 e 2005"""
    ano = random.randint(1960, 2005)
    mes = random.randint(1, 12)
    # Ajusta o último dia baseado no mês
    ultimo_dia = 31
    if mes in [4, 6, 9, 11]:
        ultimo_dia = 30
    elif mes == 2:
        ultimo_dia = 29 if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0) else 28
    
    dia = random.randint(1, ultimo_dia)
    return datetime(ano, mes, dia).date()

def gerar_email(nome, sobrenome):
    """Gera um email baseado no nome"""
    # Remove acentos
    from unicodedata import normalize
    nome_limpo = normalize('NFKD', nome.lower()).encode('ASCII', 'ignore').decode('ASCII')
    sobrenome_limpo = normalize('NFKD', sobrenome.lower()).encode('ASCII', 'ignore').decode('ASCII')
    
    # Diferentes formatos de email
    formatos = [
        f"{nome_limpo}.{sobrenome_limpo}",
        f"{nome_limpo}{sobrenome_limpo}",
        f"{nome_limpo}.{sobrenome_limpo[:3]}",
        f"{nome_limpo[:1]}{sobrenome_limpo}",
        f"{nome_limpo}{random.randint(1, 99)}"
    ]
    
    email = random.choice(formatos)
    dominios = ["gmail.com", "hotmail.com", "yahoo.com.br", "outlook.com", "uol.com.br"]
    return f"{email}@{random.choice(dominios)}"

def criar_pessoas(quantidade=200):
    """Cria a quantidade especificada de pessoas com dados aleatórios"""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    pessoas_criadas = 0
    tentativas = 0
    max_tentativas = quantidade * 2  # Para evitar loop infinito
    
    while pessoas_criadas < quantidade and tentativas < max_tentativas:
        nome = random.choice(nomes)
        sobrenome = random.choice(sobrenomes)
        nome_completo = f"{nome} {sobrenome}"
        
        # Gera CPF único
        cpf = gerar_cpf()
        if db.query(Pessoa).filter(Pessoa.cpf == cpf).first():
            tentativas += 1
            continue
        
        # Gera email único
        email = gerar_email(nome, sobrenome)
        if db.query(Pessoa).filter(Pessoa.email == email).first():
            tentativas += 1
            continue
        
        pessoa = Pessoa(
            nome=nome_completo,
            cpf=cpf,
            email=email,
            telefone=gerar_telefone(),
            data_nascimento=gerar_data_nascimento()
        )
        
        db.add(pessoa)
        try:
            db.commit()
            pessoas_criadas += 1
            print(f"Pessoa {pessoas_criadas} criada: {nome_completo} - CPF: {cpf}")
        except Exception as e:
            print(f"Erro ao criar pessoa: {e}")
            db.rollback()
            tentativas += 1
    
    db.close()
    
    print(f"\nTotal de pessoas criadas: {pessoas_criadas}")
    if tentativas >= max_tentativas:
        print("Aviso: Algumas pessoas não puderam ser criadas devido a conflitos de dados únicos")

if __name__ == "__main__":
    criar_pessoas(200)
