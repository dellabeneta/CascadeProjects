#!/bin/bash

# Criar usuário admin
python scripts/create_admin_simple.py

# Iniciar o servidor
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
