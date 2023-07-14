# gproduct-demo

## 搭建环境

```sh
npm install
```

编译和热加载开发环境：

```sh
npm run serve
```

编译和构建：

```sh
npm run build
```

补全 Lint 检查文件：

```sh
npm run lint
```

## 自定义配置

参见[配置参考](https://cli.vuejs.org/config/)。

构建镜像：

```sh
docker build -t release.daocloud.io/henry/gproduct-demo .
```

在 K8s 上运行：

```sh
kubectl apply -f demo.yaml
```
