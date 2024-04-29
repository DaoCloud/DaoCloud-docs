# OCP 环境接入服务网格配置方法

OCP (OpenShift Container Platform) 是 Red Hat 推出的容器平台。

本页说明服务网格接入 OCP 平台的操作步骤。

## SCC 安全策略设置

在 Openshift 集群中，为服务网格增加命名空间的 __privileged__ 用户权限，以 istio-operator、istio-system 两个命名空间为例：

```shell
oc adm policy add-scc-to-user privileged  system:serviceaccount:istio-operator:istio-operator
oc adm policy add-scc-to-user privileged  system:serviceaccount:istio-system:istio-system
```

## 接入 Openshift 集群

创建一个网格，接入 Openshift 集群。返回网格列表，发现 Openshift 集群已接入成功。

![集群接入成功](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/test/images/ocp01.png)

但后端会报错：

```none
COMMIT
2022-10-27T07:06:50.610621Z info Running command: iptables-restore --noflush /tmp/iptables-rules-1666854410610268141.txt1105821213
2022-10-27T07:06:50.616716Z error Command error output: xtables parameter problem: iptables-restore: unable to initialize table 'nat'

Error occurred at line: 1
Try `iptables-restore -h' or 'iptables-restore --help' for more information.
2022-10-27T07:06:50.616746Z error Failed to execute: iptables-restore --noflush /tmp/iptables-rules-1666854410610268141.txt1105821213, exit status 2
```

通过以下几步消除错误。

## OCP 激活 iptables

### 修改 YAML

参考以下 YAML，根据实际环境修改部署：

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: dsm-init
  namespace: openshift-sdn
spec:
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      app: dsm-init
  template:
    metadata:
      labels:
        app: dsm-init
        type: infra
    spec:
      containers:
      - command:
        - /bin/sh
        - -c
        - |
          #!/bin/sh
          set -x
          iptables -t nat -A OUTPUT -m tcp -p tcp -m owner ! --gid-owner 1337 -j REDIRECT --to-ports 15006
          iptables -t nat -D OUTPUT -m tcp -p tcp -m owner ! --gid-owner 1337 -j REDIRECT --to-ports 15006
          while true; do sleep 100d; done
        image: release.daocloud.io/mspider/proxyv2:1.15.0 # (1)!
        name: dsm-init
        resources:
          requests:
            cpu: 100m
            memory: 20Mi
        securityContext:
          privileged: true
      dnsPolicy: ClusterFirst
      hostNetwork: true
      hostPID: true
      nodeSelector:
        kubernetes.io/os: linux
      priorityClassName: system-node-critical
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      serviceAccount: sdn
      serviceAccountName: sdn
```

1. 修改proxy的镜像地址

### 添加参数

在 globalmesh YAML 中添加以下一行参数：

```yaml
istio.custom_params.components.cni.enabled: "true"
```

!!! note

    OpenShift 4.1 以上版本不再使用 iptables，转而使用 nftables。
    因此需要安装 istio CNI 插件，否则在边车注入时会出现如下错误，即无法执行 iptables-resotre 命令。

    ```none
    istio iptables-restore: unable to initialize table 'nat'
    ```

### 部署 istio-cni

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  components:
    cni:
      enabled: true
      namespace: istio-system
  values:
    sidecarInjectorWebhook:
      injectedAnnotations:
        k8s.v1.cni.cncf.io/networks: istio-cni
    cni:
      excludeNamespaces:
        - istio-system
      psp_cluster_role: enabled
      cniBinDir: /var/lib/cni/bin
      cniConfDir: /etc/cni/multus/net.d
      cniConfFileName: istio-cni.conf
      chained: false
```
