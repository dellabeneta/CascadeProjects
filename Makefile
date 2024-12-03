.PHONY: dev-up dev-down

# Desenvolvimento
dev-up:
	./scripts/environment.sh start dev

dev-down:
	./scripts/environment.sh stop dev