#!/bin/bash

echo "⚠️  ATENÇÃO! Este script irá remover todos os containers, imagens, volumes e redes Docker!"
echo "Esta ação não pode ser desfeita."
read -p "Tem certeza que deseja continuar? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Operação cancelada."
    exit 1
fi

echo "Iniciando limpeza completa do Docker..."

# Parar todos os containers em execução
echo "Parando todos os containers..."
docker stop $(docker ps -a -q)

# Remover todos os containers (em execução e parados)
echo "Removendo todos os containers..."
docker rm $(docker ps -a -q)

# Remover todas as imagens, incluindo as em uso
echo "Removendo todas as imagens..."
docker rmi $(docker images -q)

# Remover todos os volumes não utilizados
echo "Removendo todos os volumes..."
docker volume rm $(docker volume ls -q)

# Remover todas as redes não utilizadas
echo "Removendo todas as redes..."
docker network rm $(docker network ls -q)

# Remover cache do Docker
echo "Removendo cache do Docker..."
docker system prune -af --volumes

echo "✅ Limpeza concluída! Seu sistema Docker foi resetado completamente."