FROM ghcr.io/astral-sh/uv:0.11.13 AS uv

FROM python:3.12-slim AS builder

WORKDIR /app

COPY --from=uv /uv /uvx /bin/

RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked --no-install-project

COPY . .

RUN uv run mkdocs build -f docs/zh/mkdocs.yml -d site
RUN uv run mkdocs build -f docs/en/mkdocs.yml -d site

FROM nginx:alpine AS production

COPY --from=builder /app/docs/zh/site /usr/share/nginx/html
COPY --from=builder /app/docs/en/site /usr/share/nginx/html/en

COPY <<EOF /etc/nginx/conf.d/default.conf
server {
    listen 80;
    listen [::]:80;
    server_name localhost;

    root /usr/share/nginx/html;
    index index.html;

    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    location / {
        try_files \$uri \$uri/ \$uri.html =404;
        add_header X-Frame-Options "SAMEORIGIN" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header Referrer-Policy "no-referrer-when-downgrade" always;
    }

    location /en/ {
        try_files \$uri \$uri/ \$uri.html =404;
    }

    location /health {
        access_log off;
        return 200 "healthy\n";
        add_header Content-Type text/plain;
    }

    location /zh/ {
        return 301 /;
    }

    error_page 404 /404.html;
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /usr/share/nginx/html;
    }
}
EOF

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/health || exit 1

CMD ["nginx", "-g", "daemon off;"]
