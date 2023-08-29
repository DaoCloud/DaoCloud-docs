# gproduct-demo

## Environment setup

```sh
npm install
```

Compile and hot-reload for development:

```sh
npm run serve
```

Compile and build:

```sh
npm run build
```

Fix linting issues:

```sh
npm run lint
```

## Custom Configuration

Refer to the [Configuration Reference](https://cli.vuejs.org/config/) for customization options.

Build the image:

```sh
docker build -t release.daocloud.io/henry/gproduct-demo .
```

Run on Kubernetes:

```sh
kubectl apply -f demo.yaml
```
