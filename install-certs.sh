mkdir -p /opt/traefik/certs
chmod 755 /opt/traefik
chmod 750 /opt/traefik/certs

openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
-keyout /opt/traefik/certs/localhost.key \
-out /opt/traefik/certs/localhost.crt

chmod 644 /opt/traefik/certs/localhost.crt
chmod 600 /opt/traefik/certs/localhost.key

cp /opt/traefik/certs -r backend/
cp traefik/traefik.toml /opt/traefik/
