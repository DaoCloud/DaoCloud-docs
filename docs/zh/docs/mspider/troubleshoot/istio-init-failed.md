# 工作集群中 istio-init 容器启动失败

## 错误日志

```log
error Command error output: xtables parameter problem: iptables-restore: unable to initialize table 'nat'
```

## 问题原因

在服务网格中，将网格实例 Istio 部署一些特殊的操作系统（如 Red Hat 系的发行版本），通常与底层操作系统和网络配置有关，造成这个问题的原因有：

- 缺失 iptables 模块

  - iptables 的 nat 表需要内核模块支持。如果环境上 Red Hat 操作系统上缺少相关模块（如 xt_nat、iptable_nat），就会导致这个问题。

- 防火墙冲突

  - OpenShift 和 Istio 都依赖 iptables 来管理网络规则。如果系统中启用了 firewalld 或其他网络工具（如 nftables），可能与 iptables 发生冲突。

- nftables 与 iptables 的不兼容
  - Red Hat 8 和更新版本中，iptables 默认是通过 nftables 后端实现的。如果某些配置使用了传统 iptables 而非 nftables，就会导致类似问题。

## 解决方法

服务网格提供了对应的 `istio-os-init` 的 `Deamonset` ，负责在每个集群的节点中激活所需要的内核模块。

!!! note

    仅小部分操作系统有限制，所以这个功能在工作集群中默认不会部署 （已确认 Openshift 因为 Red Hat 系统限制，需要手工处理）

从全局管理集群中 `istio-system` 命名空间下将 `DaemonSet` 资源 `istio-os-init`， 复制并同样部署到 `istio-system` 即可.

```yaml
kind: DaemonSet
apiVersion: apps/v1
metadata:
  name: istio-os-init
  namespace: istio-system
  labels:
    app: istio-os-init
spec:
  selector:
    matchLabels:
      app: istio-os-init
  template:
    metadata:
      labels:
        app: istio-os-init
    spec:
      volumes:
        - name: host
          hostPath:
            path: /
            type: ""
      initContainers:
        - name: fix-modprobe
          image: docker.m.daocloud.io/istio/proxyv2:1.16.1
          command:
            - chroot
          args:
            - /host
            - sh
            - "-c"
            - >-
              set -ex

              # Ensure istio required modprobe

              modprobe -v -a --first-time nf_nat xt_REDIRECT xt_conntrack
              xt_owner xt_tcpudp iptable_nat iptable_mangle iptable_raw || echo
              "Istio required basic modprobe done"

              # Load Ipv6 mods # TODO for config for ipv6

              modprobe -v -a --first-time ip6table_nat ip6table_mangle
              ip6table_raw || echo "Istio required ipv6 modprobe done"

              # Load TPROXY mods # TODO for config for TPROXY

              # modprobe -v -a --first-time xt_connmark xt_mark || echo "Istio
              required TPROXY modprobe done"
          resources:
            limits:
              cpu: 100m
              memory: 50Mi
            requests:
              cpu: 10m
              memory: 10Mi
          volumeMounts:
            - name: host
              mountPath: /host
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          imagePullPolicy: IfNotPresent
          securityContext:
            privileged: true
      containers:
        - name: sleep
          image: docker.m.daocloud.io/istio/proxyv2:1.16.1
          command:
            - sleep
            - 100000d
          resources:
            limits:
              cpu: 100m
              memory: 50Mi
            requests:
              cpu: 10m
              memory: 10Mi
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          imagePullPolicy: IfNotPresent
      restartPolicy: Always
      terminationGracePeriodSeconds: 30
      dnsPolicy: ClusterFirst
      securityContext: {}
      schedulerName: default-scheduler
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 0
  revisionHistoryLimit: 10
```

也可以直接复制上面的 `YAML` 直接部署到网格实例部署的集群中。
