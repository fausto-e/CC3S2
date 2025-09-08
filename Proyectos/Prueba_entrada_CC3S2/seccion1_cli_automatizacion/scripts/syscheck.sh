#!/bin/bash

WORDIR=$(pwd)
REPORT_DIR="$WORDIR/../reports"

set -euo pipefail

trap 'echo "Error en la línea $LINENO; $BASH_COMMAND"' ERR


# Crear reporte para http.txt
if [ ! -d "$REPORT_DIR" ]; then
    mkdir -p "$REPORT_DIR"
fi

curl -Is https://example.com > "$REPORT_DIR/http.txt"

echo -e "\nComentarios:\nLa respuesta usa HTTP/2 (200 OK), entrega HTML y controla caché con ETag, Last-Modified y Cache-Control (~24h). \
El header Date marca cuándo respondió el servidor y Alt-Svc indica soporte de HTTP/3." >> "$REPORT_DIR/http.txt"


# Crear reporte para dns.txt
echo "Registro A para example.com:" > "$REPORT_DIR/dns.txt"
dig A example.com +noall +answer >> "$REPORT_DIR/dns.txt"

echo -e "\nRegistro AAAA para example.org:" >> "$REPORT_DIR/dns.txt"
dig AAAA example.org +noall +answer >> "$REPORT_DIR/dns.txt"

echo -e "\nRegistro MX para example.com:" >> "$REPORT_DIR/dns.txt"
dig MX example.com +noall +answer >> "$REPORT_DIR/dns.txt"

echo "En DNS, el TTL define cuánto tiempo las respuestas (A, AAAA, MX) pueden guardarse en caché antes de requerir nueva consulta."  >> $REPORT_DIR/dns.txt

echo "Versión TLS observada:" > "$REPORT_DIR/tls.txt"
curl -Iv https://example.com 2>&1 | grep "TLS" >> "$REPORT_DIR/tls.txt"

ss -tuln > "$REPORT_DIR/sockets.txt"
echo -e "\nRiesgos: puertos abiertos sin firewall o servicios innecesarios exponen la máquina a ataques." >> "$REPORT_DIR/sockets.txt"

echo "======================================================"
echo -e "\tsyscheck.sh finalizado correctamente"
echo "======================================================"