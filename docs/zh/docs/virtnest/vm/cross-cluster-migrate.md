# 虚拟机跨集群迁移

本功能暂未做 UI 界面能力，请参考以下操作步骤。

## 使用场景

- 当原集群发生故障或性能下降导致该集群上的虚拟机无法访问时，将虚拟机迁移到其他的集群上。
- 需要对集群进行计划内的维护或升级时，将虚拟机迁移到其他的集群上。
- 当特定应用的性能需求变化，需要调整资源分配时，迁移虚拟机到其他的集群上以匹配更合适的资源配置。

## 前提条件

实现虚拟机跨集群迁移之前，需要满足以下前提条件：

- 集群网络互通：确保原有集群与目标迁移集群之间的网络是互通的
- 相同存储类型：目标迁移集群需支持与原有集群相同的存储类型（例如，如果导出集群使用 rook-ceph-block 类型的 StorageClass，则导入集群也必须支持此类型）。
- 在原有集群的 KubeVirt 中开启 VMExport Feature Gate。

## 开启 VMExport Feature Gate

激活 VMExport Feature Gate，在原有集群内执行如下命令，
可参考[如何激活特性门控](https://kubevirt.io/user-guide/cluster_admin/activating_feature_gates/#how-to-activate-a-feature-gate)。

```sh
kubectl edit kubevirt kubevirt -n virtnest-system
```

这条命令将修改 `featureGates`，增加 `VMExport`。

```yaml
apiVersion: kubevirt.io/v1
kind: KubeVirt
metadata:
  name: kubevirt
  namespace: virtnest-system
spec:
  configuration:
    developerConfiguration:
      featureGates:
        - DataVolumes
        - LiveMigration
        - VMExport
```

## 配置原有集群的 Ingress

安装 LB 类型的 ingress-controller。

在 `virtnest-system` 命名空间下创建 tls secret：

```bash
export KEY_FILE=key.pem
export CERT_FILE=cert.ca
export HOST=upgrade-test.com
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ${KEY_FILE} -out ${CERT_FILE} -subj "/CN=${HOST}/O=${HOST}" -addext "subjectAltName = DNS:${HOST}"

export CERT_NAME=nginx-tls
kubectl -n virtnest-system create secret tls ${CERT_NAME} --key ${KEY_FILE} --cert ${CERT_FILE}
```

在 `virtnest-system` 命名空间下创建 Ingress，配置 Ingress 以指向 `virt-exportproxy` Service：

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-vm-export
  namespace: virtnest-system
spec:
  tls:
    - hosts:
        - upgrade-test.com
      secretName: nginx-tls
  rules:
    - host: upgrade-test.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: virt-exportproxy
                port:
                  number: 8443
  ingressClassName: nginx
```

## 配置目标集群的 CoreDNS ConfigMap

```bash
kubectl edit cm coredns -n kube-system
```

找到 `Corefile` 配置部分，并添加 `hosts` 配置。这里假设 Ingress 的 LB 配置为 `192.168.1.10`：

```yaml
Corefile: |
  .:53 {
      errors
      health
      ready
      kubernetes cluster.local in-addr.arpa ip6.arpa {
          pods insecure
          fallthrough in-addr.arpa ip6.arpa
      }
      hosts {
          192.168.1.10 upgrade-test.com
          fallthrough
      }
      prometheus :9153
      forward . /etc/resolv.conf
      cache 30
      loop
      reload
      loadbalance
  }

```

## 迁移步骤

1. 创建 VirtualMachineExport CR

    === "虚拟机关机状态下的冷迁移"

        ```yaml
        apiVersion: v1
        kind: Secret
        metadata:
          name: example-token # 导出虚拟机所用 token
          namespace: default # 虚拟机所在命名空间
        stringData:
          token: 1234567890ab # 导出时所用的 token

        ---
        apiVersion: export.kubevirt.io/v1alpha1
        kind: VirtualMachineExport
        metadata:
          name: example-export # 导出名称, 可自行修改
          namespace: default # 虚拟机所在命名空间
        spec:
          tokenSecretRef: example-token # 和上面创建的 token 名称保持一致
          source:
            apiGroup: "kubevirt.io"
            kind: VirtualMachine
            name: testvm # 虚拟机名称
        ```

    === "虚拟机不关机状态下的热迁移"

        ```yaml
        apiVersion: v1
        kind: Secret
        metadata:
          name: example-token # 导出虚拟机所用 token
          namespace: default # 虚拟机所在命名空间
        stringData:
          token: 1234567890ab # 导出时所用的 token

        ---
        apiVersion: export.kubevirt.io/v1alpha1
        kind: VirtualMachineExport
        metadata:
          name: export-snapshot # 导出名称, 可自行修改
          namespace: default # 虚拟机所在命名空间
        spec:
          tokenSecretRef: export-token # 和上面创建的token名称保持一致
          source:
            apiGroup: "snapshot.kubevirt.io"
            kind: VirtualMachineSnapshot
            name: export-snap-202407191524 # 对应的虚拟机快照名称
        ```

1. 检查 VirtualMachineExport 是否准备就绪：
    
    ```sh
    # 这里的 example-export 需要替换为创建的 VirtualMachineExport 名称
    kubectl get VirtualMachineExport example-export -n default
    
    NAME             SOURCEKIND       SOURCENAME   PHASE
    example-export   VirtualMachine   testvm       Ready
    ```

1. 当 VirtualMachineExport 准备就绪后，导出虚拟机 YAML。

    === "如果已安装 virtctl"
    
        使用以下命令导出虚拟机的 YAML：

        ```sh
        # 自行将 example-export替换为创建的 VirtualMachineExport 名称
        # 自行通过 -n 指定命名空间
        virtctl vmexport download example-export --manifest --include-secret --output=manifest.yaml
        ```

    === "如果没有安装 virtctl"
        
        使用以下命令导出虚拟机 YAML：

        ```sh
        # 自行替换 example-export 替换为创建的 VirtualMachineExport 名称 和命名空间
        manifesturl=$(kubectl get VirtualMachineExport example-export -n default -o=jsonpath='{.status.links.internal.manifests[0].url}')
        secreturl=$(kubectl get VirtualMachineExport example-export -n default -o=jsonpath='{.status.links.internal.manifests[1].url}')
        # 自行替换 secert 名称和命名空间
        token=$(kubectl get secret example-token -n default -o=jsonpath='{.data.token}' | base64 -d)
    
        curl -H "Accept: application/yaml" -H "x-kubevirt-export-token: $token"  --insecure  $secreturl > manifest.yaml
        curl -H "Accept: application/yaml" -H "x-kubevirt-export-token: $token"  --insecure  $manifesturl >> manifest.yaml
        ```

1. 导入虚拟机

    将导出的 `manifest.yaml` 复制到目标迁移集群并执行以下命令（如果命名空间不存在则需要提前创建）：

    ```sh
    kubectl apply -f manifest.yaml
    ```

    创建成功后，重启虚拟机，虚拟机成功运行后，在原有集群内删除原虚拟机（虚拟机未启动成功时，请勿删除原虚拟机）。
