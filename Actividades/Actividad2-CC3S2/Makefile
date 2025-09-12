SHELL := /bin/bash
.DEFAULT_GOAL := help

.PHONY: help
help: ## Mostrar los targets disponibles
	@grep -E '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: hosts-setup
hosts-setup: ## Añadir entradas a /etc/hosts
	@if grep -qP "^\d+\.\d+\.\d+\.\d+\s+miapp.local$$" /etc/hosts; then \
		echo "La entrada ya existe en /etc/hosts"; \
	else \
		echo "Anhadiendo entradas a /etc/hosts..."; \
		echo '127.0.0.1 miapp.local' | sudo tee -a /etc/hosts > /dev/null; \
	fi

