#!/bin/bash

# Função para carregar variáveis de ambiente
load_env() {
    local env=$1
    if [ -f "config/base/.env.base" ]; then
        set -a
        source config/base/.env.base
        set +a
    fi
    if [ -f "config/environments/$env/.env.$env" ]; then
        set -a
        source config/environments/$env/.env.$env
        set +a
    fi
}

# Função para mostrar os links dos recursos
show_resources() {
    echo -e "\nRecursos disponíveis:"
    echo -e "Frontend: \033[36mhttp://localhost:5173\033[0m"
    echo -e "Backend: \033[36mhttp://localhost:8000\033[0m"
    echo -e "API Docs: \033[36mhttp://localhost:8000/docs\033[0m"
    echo -e "API Redoc: \033[36mhttp://localhost:8000/redoc\033[0m"
    echo -e "Database: \033[36mlocalhost:5432\033[0m"
}

# Função para iniciar ambiente
start_environment() {
    local env=$1
    echo "Starting $env environment..."
    
    load_env $env
    
    docker compose -f config/base/docker-compose.base.yml \
                  -f config/environments/$env/docker-compose.$env.yml \
                  --env-file config/environments/$env/.env.$env \
                  up -d --build

    if [ $? -eq 0 ]; then
        echo -e "\n✅ Ambiente iniciado com sucesso!"
        show_resources
    else
        echo -e "\nErro ao iniciar o ambiente"
        exit 1
    fi
}

# Função para parar ambiente
stop_environment() {
    local env=$1
    echo "Stopping $env environment..."
    
    load_env $env
    
    docker compose -f config/base/docker-compose.base.yml \
                  -f config/environments/$env/docker-compose.$env.yml \
                  --env-file config/environments/$env/.env.$env \
                  down

    if [ $? -eq 0 ]; then
        echo -e "\n✅ Ambiente parado com sucesso!"
    else
        echo -e "\nErro ao parar o ambiente"
        exit 1
    fi
}

# Função principal
main() {
    local action=$1
    local env=$2

    case $action in
        "start")
            start_environment $env
            ;;
        "stop")
            stop_environment $env
            ;;
        *)
            echo "Usage: $0 {start|stop} {dev|qa|prod}"
            exit 1
            ;;
    esac
}

# Executa a função principal com os argumentos passados
main "$@"
