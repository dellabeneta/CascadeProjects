.PHONY: dev-up dev-down dev-logs dev-shell qa-up qa-down prod-up prod-down

# Desenvolvimento
dev-up:
	./scripts/environment.sh start dev

dev-down:
	./scripts/environment.sh stop dev

dev-logs:
	docker-compose -f config/base/docker-compose.base.yml \
					-f config/environments/dev/docker-compose.dev.yml logs -f

dev-shell:
	docker-compose -f config/base/docker-compose.base.yml \
					-f config/environments/dev/docker-compose.dev.yml \
					exec backend /bin/bash