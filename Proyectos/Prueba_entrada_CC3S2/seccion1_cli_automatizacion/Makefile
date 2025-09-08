SHELL := /bin/bash
.DEFAULT_GOAL := help

.PHONY: help
help: ## Mostrar los targets disponibles
	@echo "Make targets:"
	@grep -E '^[a-zA-Z0-9_\-]+:.*?##' $(MAKEFILE_LIST) | \
		awk 'BEGIN{FS=":.*?##"}{printf "  \033[36m%-22s\033[0m %s\n", $$1, $$2}'

.PHONY: tools
tools: ## Verificar dependencias

	@command -v bash >/dev/null || { echo "Falta bash"; exit 1; }
	@command -v git >/dev/null || { echo "Falta git"; exit 1; }
	@command -v python3 >/dev/null || { echo "Falta python3"; exit 1; }
	@command -v pytest >/dev/null || { echo "Falta pytest"; exit 1; }
	@command -v curl >/dev/null || { echo "Falta curl"; exit 1; }
	@command -v dig >/dev/null || { echo "Falta dig"; exit 1; }
	@command -v ss >/dev/null || { echo "Falta ss"; exit 1; }
	@command -v jq >/dev/null || { echo "Falta jq"; exit 1; }
	@echo "======================================================"
	@echo -e "\tTools instaladas correctamente"
	@echo "======================================================"

.PHONY: report
report: ## Genera reportes sobre example.com
	@cd scripts && source syscheck.sh

.PHONY: all
all: tools report ## Verifica dependencias y genera todos los reportes (ejecuta tools y report)
