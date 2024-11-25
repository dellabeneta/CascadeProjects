#!/bin/bash

echo "ATENÇÃO! Este script irá remover todos os containers, imagens, volumes e redes Docker!"
echo "Esta ação não pode ser desfeita."
read -p "Tem certeza que deseja continuar? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Operação cancelada."
    exit 1
fi

echo "Parando todos os containers..."
docker stop $(docker ps -a -q)

echo "Removendo todos os containers..."
docker rm $(docker ps -a -q)

echo "Removendo todas as imagens..."
docker rmi $(docker images -q)

echo "Removendo todos os volumes..."
docker volume rm $(docker volume ls -q)

echo "Removendo todas as redes..."
docker network rm $(docker network ls -q)

echo "Removendo cache do Docker..."
docker system prune -af --volumes

echo "Limpeza concluída! Seu sistema Docker foi resetado completamente."
