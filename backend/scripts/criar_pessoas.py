import requests
from datetime import datetime, timedelta
import random

# Lista de nomes e sobrenomes para gerar combinações
nomes = ["Miguel", "Arthur", "Gael", "Theo", "Heitor", "Ravi", "João", "Pedro", "Bernardo", "Gabriel",
         "Alice", "Helena", "Laura", "Maria", "Valentina", "Heloísa", "Julia", "Sophie", "Luna", "Cecília"]

sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira",
              "Lima", "Gomes", "Ribeiro", "Martins", "Rocha", "Pinto", "Carvalho", "Teixeira"]

# Função para gerar uma data de nascimento aleatória entre 1970 e 2000
def gerar_data_nascimento():
    start_date = datetime(1970, 1, 1)
    end_date = datetime(2000, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")

# URL da API
API_URL = "http://localhost:8080/pessoas/"

# Criar 20 pessoas
for i in range(20):
    # Gerar dados aleatórios
    nome = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    email = f"{nome.lower().replace(' ', '.')}@email.com"
    telefone = f"9{random.randint(10000000, 99999999)}"
    data_nascimento = gerar_data_nascimento()
    
    # Criar payload
    pessoa = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "data_nascimento": data_nascimento,
        "ativo": True
    }
    
    # Fazer requisição POST
    try:
        response = requests.post(API_URL, json=pessoa)
        if response.status_code == 201:
            print(f"Pessoa criada com sucesso: {nome}")
        else:
            print(f"Erro ao criar pessoa {nome}: {response.status_code}")
    except Exception as e:
        print(f"Erro ao criar pessoa {nome}: {str(e)}")

print("\nProcesso finalizado!")
