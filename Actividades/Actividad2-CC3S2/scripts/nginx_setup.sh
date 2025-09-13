#!/usr/bin/env bash

echo "Escribiendo server block de Nginx en $NGINX_SITE (requiere sudo)"
sudo tee "$NGINX_SITE" >/dev/null <<NGX
server {
    listen 443 ssl;
    server_name $DOMAIN;

    ssl_certificate     $crt;
    ssl_certificate_key $key;

    add_header Strict-Transport-Security "max-age=31536000" always;

    location / {
        proxy_pass http://127.0.0.1:$PORT;
        proxy_http_version 1.1;
        proxy_set_header Host \$host;
        proxy_set_header X-Forwarded-For \$remote_addr;
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Forwarded-Host \$host;
    }
}

server {
    listen 80;
    server_name $DOMAIN;
    return 301 https://$DOMAIN\$request_uri;
}
NGX

if [[ ! -e "$NGINX_LINK" ]]; then
    sudo ln -s "$NGINX_SITE" "$NGINX_LINK" || true
fi

echo "Recargando Nginx"
if [ -d /run/systemd/system ]; then
    sudo systemctl reload nginx
else
    sudo service nginx reload
fi