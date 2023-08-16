FROM docker.m.daocloud.io/node:16.13.2 as builder

WORKDIR /app
COPY . /app

# package-lock.json is needed
RUN npm ci

ENV VUE_APP_PUBLIC_BASE_PATH=.

RUN npm run build

FROM docker.m.daocloud.io/nginx:1.21.6-alpine

COPY --from=builder /app/dist /usr/share/nginx/html
COPY --from=builder /app/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
