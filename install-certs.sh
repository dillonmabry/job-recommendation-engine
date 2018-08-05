mkdir -p /opt/traefik/certs
chmod 755 /opt/traefik
chmod 750 /opt/traefik/certs

openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
-keyout /opt/traefik/certs/searchapp.local.key \
-out /opt/traefik/certs/searchapp.local.crt

chmod 644 /opt/traefik/certs/searchapp.local.crt
chmod 600 /opt/traefik/certs/searchapp.local.key

cp /opt/traefik/certs -r backend/
cp traefik/traefik.toml /opt/traefik/
