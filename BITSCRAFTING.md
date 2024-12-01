# 🛠 Bitscrafting: Technical Deep Dive

## 📜 Project Scripting Architecture

### Scripts Overview

#### 1. `scripts/environment.sh`
**Purpose**: Comprehensive environment management script

**Key Features**:
- Multi-environment support (dev, qa, prod)
- Dynamic environment variable loading
- Docker Compose orchestration
- Resource URL display after startup

**Workflow**:
```bash
# Start environment
./scripts/environment.sh start dev

# Stop environment
./scripts/environment.sh stop dev
```

**Environment Variable Loading**:
- Loads base environment: `config/base/.env.base`
- Loads specific environment config: `config/environments/{env}/.env.{env}`

#### 2. `Makefile`
**Purpose**: Simplified command interface for development tasks

**Available Targets**:
- `dev-up`: Start development environment
- `dev-down`: Stop development environment
- `dev-logs`: View container logs
- `dev-shell`: Access backend container shell
- `clean`: Prune Docker resources

**Usage Examples**:
```bash
# Start dev environment
make dev-up

# Stop dev environment
make dev-down

# Access backend shell
make dev-shell
```

#### 3. `docker-apocalypse.sh`
**Purpose**: Comprehensive Docker environment cleanup

**Functionality**:
- Stops all running containers
- Removes all containers
- Removes all images
- Removes all volumes
- Removes all networks

**Caution**: Destructive operation, use carefully

**Recommended Usage**:
```bash
# Give execution permission
chmod +x docker-apocalypse.sh

# Run cleanup
./docker-apocalypse.sh
```

### 🔧 Technical Considerations

#### Environment Initialization Flow
1. `environment.sh` script is called
2. Environment-specific `.env` files are loaded
3. Docker Compose files are merged
4. Containers are built and started
5. Resources URLs are displayed

#### Docker Compose Configuration
- Base configuration: `config/base/docker-compose.base.yml`
- Environment-specific: `config/environments/{env}/docker-compose.{env}.yml`

### 🚨 Best Practices

1. **Never commit sensitive information**
   - Use `.env.example` as a template
   - Keep real `.env` files in `.gitignore`

2. **Consistent Environment Management**
   - Always use `./scripts/environment.sh` for environment control
   - Avoid manual Docker Compose commands

3. **Resource Cleanup**
   - Use `docker-apocalypse.sh` for complete reset
   - Be cautious with data volumes

### 🔍 Debugging Tips

- Check container logs: `make dev-logs`
- Access container shell: `make dev-shell`
- Verify environment variables: Review `.env` files

### 📊 Performance Optimization

- Use multi-stage Docker builds
- Minimize layer count in Dockerfiles
- Use `.dockerignore` to reduce build context

## 🤝 Contributing to Scripting

1. Maintain script readability
2. Add comments explaining complex logic
3. Follow existing naming conventions
4. Test scripts in different environments

## 📝 Notes

This document provides insights into the project's scripting architecture. Always refer to the latest version of scripts and configurations.
