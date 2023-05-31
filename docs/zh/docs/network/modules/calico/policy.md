# 网络策略

## 策略对象

- Pod

    calico 支持通过 `GlobalNetworkPolicy` 和 `NetworkPolicy` 对 Pod 的 Egress/Ingress 流量进行管控。

    特定 Namespace 的 Pod 只能与此 Namespace 下的 Pod 通信。若 namespace 具有 Label: `environment == "development`，则该 namespace 下的 Pod 只能与同一 namespace 下的 Pod 通信：

    ```yaml
    apiVersion: projectcalico.org/v3
    kind: GlobalNetworkPolicy
    metadata:
      name: restrict-development-access
    spec:
      namespaceSelector: 'environment == "development"'
      ingress:
        - action: Allow
          source:
            namespaceSelector: 'environment == "development"'
      egress:
        - action: Allow
          destination:
            namespaceSelector: 'environment == "development"'
    ```

- Service

    Calico 支持对 Kubernetes Service 进行管控：

    ```yaml
    apiVersion: projectcalico.org/v3
    kind: NetworkPolicy
    metadata:
      name: allow-api-access
      namespace: my-app
    spec:
      selector: all()
      egress:
        - action: Allow
          destination:
            services:
              name: kubernetes
              namespace: default
    ```

    此处 Policy 指的是允许所有 Pod 访问 Kubernetes 这个 Service。

- host

    Calico 支持通过 `GlobalNetworkPolicy` 对 Kubernetes 节点进行管控。

- VMs

- `ServiceAccount`

    Calico 支持用 `ServiceAccount` 来灵活地控制策略在 Pod 上的应用方式：

    1. 使用 `ServiceAccounts` 来限制 Pod 的入口流量：

        当访问 namespace: prod-engineering 下具有 Label: `app == "db"` 的 Pod 时，如果访问者 Pod 所使用的 `serviceAccounts` 的 name 是 `api-service` 或者 `user-auth-service`，则请求通过。

        ```yaml
        apiVersion: projectcalico.org/v3
        kind: NetworkPolicy
        metadata:
          name: demo-calico
          namespace: prod-engineering
        spec:
          ingress:
            - action: Allow
              source:
                serviceAccounts:
                  names:
                    - api-service
                    - user-auth-service
          selector: 'app == "db"'
        ```

    2. 使用 `ServiceAccount` 的 Label 限制工作负载的入口流量：

        当访问者 Pod 所绑定的 `ServiceAccounts` 的 Label 满足 `app == "web-frontend"`, 则允许访问 `prod-engineering` namespace 下满足 Label: 'app == "db"' 的 Pod。

        ```yaml
        apiVersion: projectcalico.org/v3
        kind: NetworkPolicy
        metadata:
          name: allow-web-frontend
          namespace: prod-engineering
        spec:
          ingress:
            - action: Allow
              source:
                serviceAccounts:
                  selector: 'app == "web-frontend"'
          selector: 'app == "db"'
        ```

    3. 使用 `serviceAccountSelector` 筛选 Policy 的作用目标：

        只有 `serviceAccountSelector` 匹配 `'role == "intern"` 的 Pod 之间才能互相访问：

        ```yaml
        apiVersion: projectcalico.org/v3
        kind: NetworkPolicy
        metadata:
          name: restrict-intern-access
          namespace: prod-engineering
        spec:
          serviceAccountSelector: 'role == "intern"'
          ingress:
            - action: Allow
              source:
                serviceAccounts:
                  selector: 'role == "intern"'
          egress:
            - action: Allow
              destination:
                serviceAccounts:
                  selector: 'role == "intern"'
        ```

## 对流量的双向管控

- Egress

    支持对匹配策略的 Endpoint 进行出口流量管控

- Ingress

    支持对匹配策略的 Endpoint 进行入口流量管控

## 支持多种管控行为

- Allow

    当数据包匹配定义的行为，允许其通过。

- Deny

    当数据包不匹配定义的行为，禁止其通过。

- Log

    不对数据包进行管控，只是日志记录，然后继续处理下一条规则。

- Pass

    Pass action 会跳过目前剩下的所有规则，跳转到 Calico EndPoint 分配的第一个 Profile，然后执行 Profile 定义的规则。
    Calico 对于每一个 Endpoint 都会绑定两个 Profile（`kns.<namespace>` 和 `ksa.<namespace>.default`）。
    Profile 中定义了一系列的 Label 和策略（由于历史原因，Profile 中包括策略规则，先已废弃）。
    如果该 Endpoint 没有绑定任何的 Profile，那么策略结果相当于 Deny。

## 策略优先级

通过 order 字段指定，如果没有指定，默认最后执行。数值越小优先级越高。如果 order 的值一样，按照 Policy 的 name 字段顺序排序。

## 集群及租户级别的管控

Kubernetes 默认采用零信任模型，即集群内所有 Pod、主机之间都可以相互访问。我们可以定义全局的策略或者租户级别的策略来管控 Pod 的入口、出口流量。

- 全局策略管控

    通过 `GlobalNetworkPolicy` 对象作用于所有 namespace 的 Pod。例如，以下示例禁止带有 label: `app=client` 的 Pod 去访问带有 label: `app=="server"` 的 Pod：

    ```yaml
    apiVersion: projectcalico.org/v3
    kind: GlobalNetworkPolicy
    metadata:
      name: deny-tcp-8080
    spec:
      order: 1
      selector: app == 'server'  
      types:
        - Ingress
        - Egress
      ingress:
        - action: Deny
          metadata:
          annotations:
            from: client
            to: server
          protocol: TCP
          source:
            selector: app == 'client'
          destination:
            ports:
            - 8080
      egress:
        - action: Allow
    ```

    其中，

    - `selector`：通过标签筛选此 Policy 作用于哪些 Pod
    - `types`：管控流量的方向，`Ingress` 表示入口流量，`Egress` 表示出口流量
    - `ingress`：定义入口流量策略的内容
    - `action`：策略动作。可选值为 Allow、Deny、Log、Pass
    - `metadata`：额外信息。只是为了说明
    - `protocol`：协议。可选为"TCP"、"UDP"、"ICMP"、"ICMPv6"、"SCTP"、"UDPLite"
    - `source`：通过 label 筛选访问源
    - `destination`：筛选访问目标，这里筛选目的端口为 8080
    - `egress`：这里未做其他要求，允许所有通过 `calicoctl apply -f`，即可生效。

- 租户级别管控

    Calico 通过 `NetworkPolicy` 对象管控特定 namespace 下的 Pod，与 `GlobalNetworkPolicy` 不同的是，`NetworkPolicy` 作用于特定 namespace。
    例如：

    ```yaml
    apiVersion: projectcalico.org/v3
    kind: NetworkPolicy
    metadata:
      name: allow-tcp-8080
      namespace: production
    spec:
      selector: app == 'server'
      types:
      - Ingress
      - Egress
      ingress:
        - action: Allow
          metadata:
            annotations:
              from: frontend
              to: database
          protocol: TCP
            source:
              selector: app == 'client'
            destination:
              ports:
               - 8080
      egress:
        - action: Allow
    ```

    与上面的 `GlobalNetworkPolicy` 的不同之处在于：`metadata` 多了一个 namespace 字段，规定了这个策略作用的 namespace。

## 与 Kubernetes Policy 对比

- 支持策略优先级

- 支持 Deny 规则

- 更加灵活的匹配规则

- 支持管控更多的策略对象, Kubernetes 只支持管控 Pod

## 性能影响

Calico 的 Policy 实现依赖于 `IPtables`。
当策略增多，节点对应的 `iptables` 数量也会增多，这会影响到性能。
以下测试展示，当策略增加时，不同模式下如 `iptables`、`ipset`、`tc-bpf`、`cilium`、`calico` 的性能变化（包括 CPU 开销、吞吐量、延迟）。

!!! note

    以下测试场景旨在测试 Policy 的数量对集群内部的流量访问外部 CIDR 出口流量的影响。
    其中，Calico 使用 `GlobalNetworkSet API` 传递想要拒绝出口的 CIDR 列表，然后通过标签选择器引用 `GlobalNetworkPolicy` 中的 `GlobalNetworkSet` 资源。
    实际上，这种方式本质上使用的是 `IPset`，所以可参考 `IPtables` 模式的数据。

性能测试结果（仅供参考）:

- 当规则数增加到 1000 条以上时，`IPtables` 模式下的吞吐量大幅度增加。

![Throughput](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/throughput.svg)

- 当规则数增加到 1000 条以上时，`IPtables` 模式下的 CPU 使用量大幅度增加。

![CPU Usage](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/cpu-saturated.svg)

- 当规则数增加到 1000 条以上时，`IPtables` 模式下的延迟大幅度增加。

![Latency](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/latency-with-iptables.svg)
