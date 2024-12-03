.PHONY: backend-install backend-run frontend-install frontend-run install run-all

# Backend commands
backend-install:
	cd backend && pip install -r requirements.txt --break-system-packages

backend-run:
	cd backend && uvicorn app.main:app --host 0.0.0.0 --reload --port 8000

# Frontend commands
frontend-install:
	cd frontend && npm install

frontend-run:
	cd frontend && npm run dev

# Combined commands
install: backend-install frontend-install

run-all:
	@echo "Starting backend and frontend servers..."
	@make backend-run & make frontend-run

help:
	@echo "Available commands:"
	@echo "  make backend-install  - Install backend dependencies"
	@echo "  make backend-run      - Run backend development server"
	@echo "  make frontend-install - Install frontend dependencies"
	@echo "  make frontend-run     - Run frontend development server"
	@echo "  make install         - Install both backend and frontend dependencies"
	@echo "  make run-all         - Run both backend and frontend servers"
