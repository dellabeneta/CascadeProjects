#!/bin/bash

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Função para exibir mensagem de aviso
show_warning() {
    echo                
    echo -e "${RED}Atenção!${NC}" "Este script irá:"
    echo
    echo "1. Parar todos os containers Docker"
    echo "2. Remover todos os containers"
    echo "3. Remover todas as imagens"
    echo "4. Remover todos os volumes"
    echo "5. Remover todas as redes"
    echo
}

# Função para confirmar ação
confirm_action() {
    while true; do
        echo -n -e "Você tem certeza que deseja prosseguir? Digite ${YELLOW}y${NC} para confirmar ou ${YELLOW}c${NC} para cancelar: "
        read -n 1 response
        echo

        case $response in
            y|Y)
                return 0
                ;;
            c|C)
                echo -e "${RED}Operação cancelada pelo usuário.${NC}"
                exit 1
                ;;
            *)
                echo -e "${YELLOW}Entrada inválida. Por favor, digite 'y' para prosseguir ou 'c' para cancelar.${NC}"
                ;;
        esac
    done
}

# Função principal
main() {
    show_warning
    confirm_action

    echo -e "Iniciando limpeza do Docker..."
    echo

    # Para todos os containers
    echo -e "Parando todos os containers..."
    docker stop $(docker ps -aq) 2>/dev/null || true

    # Remove todos os containers
    echo -e "Removendo todos os containers..."
    docker rm $(docker ps -aq) 2>/dev/null || true

    # Remove todas as imagens
    echo -e "Removendo todas as imagens..."
    docker rmi $(docker images -q) 2>/dev/null || true

    # Remove todos os volumes
    echo -e "Removendo todos os volumes..."
    docker volume rm $(docker volume ls -q) 2>/dev/null || true

    # Remove todas as redes
    echo -e "Removendo todas as redes..."
    docker network rm $(docker network ls -q) 2>/dev/null || true

    # Executa um Prune no Docker System
    echo -e "Removendo caches com prune..."
    docker system prune --all --volumes --force 2>/dev/null || true

    echo
    echo -e "${GREEN}Limpeza do Docker concluída com sucesso!${NC}"
}

# Executa a função principal
main
