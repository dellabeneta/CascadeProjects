#!/bin/bash

echo "Iniciando limpeza completa do Docker..."

# Parar todos os containers em execução
echo "Parando todos os containers..."
docker stop $(docker ps -aq)

# Remover todos os containers (em execução e parados)
echo "Removendo todos os containers..."
docker rm $(docker ps -aq)

# Remover todas as imagens, incluindo as em uso
echo "Removendo todas as imagens..."
docker rmi -f $(docker images -aq)

# Remover todos os volumes não utilizados
echo "Removendo todos os volumes não utilizados..."
docker volume rm $(docker volume ls -q)

# Remover todas as redes não utilizadas
echo "Removendo todas as redes não utilizadas..."
docker network rm $(docker network ls -q)

# Limpar o cache de build do Docker
echo "Limpando o cache de build..."
docker builder prune -f

# Limpar todos os objetos não utilizados (imagens, containers, volumes, redes)
echo "Limpando todos os objetos não utilizados..."
docker system prune -a --volumes -f

# Remover o arquivo do banco de dados SQLite
echo "Removendo banco de dados SQLite..."
sudo rm -f ./backend/data/sql_app.db

echo "Limpeza concluída! Seu sistema Docker foi resetado completamente."