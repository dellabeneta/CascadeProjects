#!/bin/bash

# Criar usuário admin
python scripts/create_admin_simple.py

# Popular com 200 fakes de pessoas
python scripts/create_fake_pessoas.py

# Iniciar o servidor
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
