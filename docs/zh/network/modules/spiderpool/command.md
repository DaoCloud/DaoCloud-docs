# 常用命令

本页说明如何在 CLI 命令行使用 spiderpoolctl 程序来调试。

## spiderpoolctl gc

触发对 spiderpool-controller 的垃圾回收请求。

```shell
    --address string         [optional] address for spider-controller (default to service address)
```

## spiderpoolctl ip show

显示正在使用此 IP 的 Pod。选项为：

```shell
    --ip string     [required] ip
```

## spiderpoolctl ip release

尝试释放一个 IP。各选项为：

```shell
    --ip string     [optional] ip
    --force         [optional] force release ip
```

## spiderpoolctl ip set

设定一个 Pod 要使用的 IP。这将更新 ippool 和工作负载端点资源。各选项为：

```shell
    --ip string                 [required] ip
    --pod string                [required] pod name
    --namespace string          [required] pod namespace
    --containerid string        [required] pod container id
    --node string               [required] the node name who the pod locates
    --interface string          [required] pod interface who taking effect the ip
```
