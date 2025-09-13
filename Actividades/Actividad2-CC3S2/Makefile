SHELL := /bin/bash
.DEFAULT_GOAL := help
DIR := $(shell pwd)
CERT_DIR := "$(DIR)/certs"
DOMAIN ?= "miapp.local"
APP_PORT ?= 8080
CRT :="$(CERT_DIR)/$(DOMAIN).crt"
KEY :="$(CERT_DIR)/$(DOMAIN).key"
NGINX_LINK := "/etc/nginx/sites-enabled/miapp.conf"
NGINX_SITE := "/etc/nginx/sites-available/miapp.conf"
HOST := "miapp.local"

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

.PHONY: tls-cert
tls-cert: ## Generar certificados TLS autofirmados
	@mkdir -p $(CERT_DIR)
	@if [[ -f "$(CRT)" && -f "$(KEY)" ]]; then\
		echo "Certificado existente en $(CRT)";\
	else\
    	echo "Generando certificado autofirmado (SAN: DNS:$(DOMAIN), IP:127.0.0.1)"; \
    	openssl req -x509 -newkey rsa:2048 -days 365 -nodes \
      		-keyout "$(KEY)" -out "$(CRT)" \
      		-subj "/CN=$(DOMAIN)" \
      		-addext "subjectAltName=DNS:$(DOMAIN),IP:127.0.0.1" >/dev/null 2>&1; \
  	fi
	@sudo chmod +x ./scripts/nginx_setup.sh
	@PORT=APP_PORT CERT_DIR=CERT_DIR DOMAIN=DOMAIN NGINX_LINK=NGINX_LINK NGINX_SITE=NGINX_SITE\
	 crt=CRT key=KEY ./scripts/nginx_setup.sh

.PHONY: tls-check
tls-check: ## Verificar certificados TLS
	@openssl s_client -connect "$(DOMAIN):443" -servername "$(DOMAIN)" -brief </dev/null || true

	@echo "curl -k https://$(DOMAIN)/"
	@curl -sS -k "https://$(DOMAIN)/"
	@echo "ss -ltnp | grep -E ':(443|$(PORT))'"
	@ss -ltnp | grep -E ":(443|$(PORT))"  || true

	@if [[ -d /run/systemd/system ]]; then \
		echo "journalctl -u nginx -n 50 --no-pager"; \
		sudo journalctl -u nginx -n 50 --no-pager; \
		if [[ -f /var/log/nginx/error.log ]]; then \
			sudo tail -n 50 /var/log/nginx/error.log; \
		fi \
	fi \