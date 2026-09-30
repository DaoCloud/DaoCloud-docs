# Failed to Start the istio-init Container in the Working Cluster

## Error Log

```log
error Command error output: xtables parameter problem: iptables-restore: unable to initialize table 'nat'
```

## Problem Cause

In the service mesh, if you deploy the mesh instance Istio on some special operating systems (such as some Red Hat distributions), the problem is usually related to the underlying operating system and network configuration. The causes of this problem are:

- Missing iptables modules

    The nat table of iptables requires kernel module support. If the relevant modules (such as xt_nat and iptable_nat) are missing on the Red Hat operating system in the environment, this problem will occur.

- Firewall conflicts

    Both OpenShift and Istio rely on iptables to manage network rules. If firewalld or other network tools (such as nftables) are enabled on the system, they may conflict with iptables.

- Incompatibility between nftables and iptables

    In Red Hat 8 and later versions, iptables is implemented through the nftables backend by default. If some configurations use the traditional iptables instead of nftables, similar problems will occur.

## Solution

The service mesh provides a corresponding `DaemonSet` named `istio-os-init`, which is responsible for activating the required kernel modules on the nodes of each cluster.

!!! note

    Only a small number of operating systems have restrictions, so this feature is not deployed in the working cluster by default (it has been confirmed that OpenShift needs manual handling due to Red Hat system restrictions).

In the global service management cluster, copy the `DaemonSet` resource `istio-os-init` in the `istio-system` namespace and deploy it to `istio-system` in the same way.

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

You can also directly copy the YAML above and deploy it to the cluster where the mesh instance resides.
