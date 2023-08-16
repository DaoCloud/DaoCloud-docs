# gproduct-demo

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### Image Build
```
docker build -t release.daocloud.io/henry/gproduct-demo .
```

### Run on K8s
```
kubectl apply -f demo.yaml
```
