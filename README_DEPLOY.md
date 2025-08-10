# PulseWatch Deploy (Fixed Bundle)

This bundle includes cleaned config files for Docker Compose, Nginx, and Gunicorn.

## Quick start on the server
```bash
cd /opt/pulsewatch
docker compose down --remove-orphans
docker compose up -d --build
docker compose ps

# validate nginx and hit app through TLS
docker compose exec -T nginx nginx -t && docker compose exec -T nginx nginx -s reload
curl -I http://127.0.0.1:8000/
curl -I https://pulsewatch.pro/health
curl -I https://pulsewatch.pro/
```

## Notes
- `web` runs with gunicorn (2 workers) listening on 0.0.0.0:8000.
- `nginx` proxies to `web` and serves ACME challenges from `nginx/www`.
- `certbot` container is present for renew hooks; add a cron on host to run renewals.
- Ensure certificates at `/etc/letsencrypt/live/pulsewatch.pro/` exist on first issuance.
- Edit `nginx/nginx.conf` to include your production server_name and TLS paths if not already set.
