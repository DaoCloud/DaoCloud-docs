# 如何开启采集审计日志

Kubernetes审计日志是对 Kubernetes API-Server的每个调用的详细描述。
审计提供了安全相关的时序操作记录（包括时间、来源、操作结果、发起操作的用户、操作的资源以及请求/响应的详细信息等）。
第五代产品主要采集的审计日志数据来自 Kubernetes 审计日志以及 `全局管理`的审计日志。
考虑到审计日志的数据量大小，Insight 默认不采集 Kubernetes 的审计日志，仅采集`全局管理`的审计日志。

## 前提条件

目标集群已安装 `insight-agent` 且处于`运行中`状态。

## 如何开启 Kubernetes 审计日志

1. 配置审计日志 policy 文件，将以下的 yaml 放到 `/etc/kubernetes/audit-policy/` 文件夹下，并命名为 `apiserver-audit-policy.yaml`

    ```yaml
    apiVersion: audit.k8s.io/v1
    kind: Policy
    # Don't generate audit events for all requests in RequestReceived stage.
    omitStages:
    - "ResponseStarted"
    - "RequestReceived"
    - "Panic"
    rules:
    # The following requests were manually identified as high-volume and low-risk,
    # so drop them.
    - level: None
        users: ["system:kube-proxy"]
        verbs: ["watch"]
        resources:
        - group: "" # core
            resources: ["endpoints", "services", "services/status"]
    - level: None
        # Ingress controller reads `configmaps/ingress-uid` through the unsecured port.
        # TODO(#46983): Change this to the ingress controller service account.
        users: ["system:unsecured"]
        namespaces: ["kube-system"]
        verbs: ["get"]
        resources:
        - group: "" # core
            resources: ["configmaps"]
    - level: None
        users: ["kubelet"] # legacy kubelet identity
        verbs: ["get"]
        resources:
        - group: "" # core
            resources: ["nodes", "nodes/status"]
    - level: None
        userGroups: ["system:nodes"]
        verbs: ["get"]
        resources:
        - group: "" # core
            resources: ["nodes", "nodes/status"]
    - level: None
        users:
        - system:kube-controller-manager
        - system:kube-scheduler
        - system:serviceaccount:kube-system:endpoint-controller
        verbs: ["get", "update"]
        namespaces: ["kube-system"]
        resources:
        - group: "" # core
            resources: ["endpoints"]
    - level: None
        users: ["system:apiserver"]
        verbs: ["get"]
        resources:
        - group: "" # core
            resources: ["namespaces", "namespaces/status", "namespaces/finalize"]
    # Don't log HPA fetching metrics.
    - level: None
        users:
        - system:kube-controller-manager
        verbs: ["get", "list"]
        resources:
        - group: "metrics.k8s.io"
    # Don't log these read-only URLs.
    - level: None
        nonResourceURLs:
        - /healthz*
        - /version
        - /swagger*
    # Don't log events requests.
    - level: None
        resources:
        - group: "" # core
            resources: ["events"]
            
    # new start
    # 忽略所有访问非认证端口的 API，通常是系统组件如 Kube-Controller 等。
    - level: None
        users: ["system:unsecured"]

    # 忽略 kube-admin 的审计日志
    - level: None
        users: ["kube-admin"]
    # 忽略所有资源状态更新的 API need add
    - level: None
        resources:
        - group: "" # core
        resources: ["events", "nodes/status", "pods/status", "services/status"]
        - group: "authorization.k8s.io"
        resources: ["selfsubjectrulesreviews"]
    # 忽略leases need add
    - level: None
        resources:
        - group: "coordination.k8s.io"
        resources: ["leases"]
    - level: Request
        verbs: ["create", "update", "patch", "delete"]
        users: ["kube-admin"]
    #new end

    # Secrets, ConfigMaps, and TokenReviews can contain sensitive & binary data,
    # so only log at the Metadata level.
    - level: Metadata
        resources:
        - group: "" # core
            resources: ["secrets", "configmaps"]
        - group: authentication.k8s.io
            resources: ["tokenreviews"]
        omitStages:
        - "RequestReceived"
    # Get responses can be large; skip them.
    - level: Request
        verbs: ["get", "list", "watch"]
        resources:
        - group: "" # core
        - group: "admissionregistration.k8s.io"
        - group: "apiextensions.k8s.io"
        - group: "apiregistration.k8s.io"
        - group: "apps"
        - group: "authentication.k8s.io"
        - group: "authorization.k8s.io"
        - group: "autoscaling"
        - group: "batch"
        - group: "certificates.k8s.io"
        - group: "extensions"
        - group: "metrics.k8s.io"
        - group: "networking.k8s.io"
        - group: "policy"
        - group: "rbac.authorization.k8s.io"
        - group: "settings.k8s.io"
        - group: "storage.k8s.io"
        omitStages:
        - "RequestReceived"
    # Default level for known APIs
    - level: RequestResponse
        resources:
        - group: "" # core
        - group: "admissionregistration.k8s.io"
        - group: "apiextensions.k8s.io"
        - group: "apiregistration.k8s.io"
        - group: "apps"
        - group: "authentication.k8s.io"
        - group: "authorization.k8s.io"
        - group: "autoscaling"
        - group: "batch"
        - group: "certificates.k8s.io"
        - group: "extensions"
        - group: "metrics.k8s.io"
        - group: "networking.k8s.io"
        - group: "policy"
        - group: "rbac.authorization.k8s.io"
        - group: "settings.k8s.io"
        - group: "storage.k8s.io"
        omitStages:
        - "RequestReceived"
    # Default level for all other requests.
    - level: Metadata
        omitStages:
        - "RequestReceived"
    ```

2. 打开 `api-server` 的配置文件 `kube-apiserver.yaml`，一般会在 `/etc/kubernetes/manifests/` 文件夹，并添加以下配置信息:

	- 在 `spec.containers.command` 下添加命令：

    ```yaml
    --audit-log-maxage=30
    --audit-log-maxbackup=1
    --audit-log-maxsize=100
    --audit-log-path=/var/log/audit/kube-apiserver-audit.log
    --audit-policy-file=/etc/kubernetes/audit-policy/apiserver-audit-policy.yaml
    ```

    - 在 `spec.containers.volumeMounts` 下添加:

    ```yaml
    - mountPath: /var/log/audit
        name: audit-logs
    - mountPath: /etc/kubernetes/audit-policy
        name: audit-policy
    ```

    - 在 `spec.volumes` 下添加：

    ```yaml
    - hostPath:
        path: /var/log/kubernetes/audit
        type: ""
    name: audit-logs
    - hostPath:
        path: /etc/kubernetes/audit-policy
        type: ""
    name: audit-policy
    ```

3. 等待几分钟 `api-server`重启成功后，在 `/var/log/kubernetes/audit` 目录下查看是否有审计日志生成，验证是否成功开启 Kubernetes 审计日志。

> 如果想关闭，去掉 `spec.containers.command` 中的相关命令即可。

## 开启采集审计日志

可观测性通过 `FluentBit` 采集审计日志。默认 `FluentBit` 不会采集 `/var/log/kubernetes/audit` 下的日志文件(k8s 审计日志) 。操作以下步骤开启采集审计日志：

1. 修改 `FluentBit` 的 ConfigMap ，执行以下命令

    ```
    kubectl edit cm insight-agent-fluent-bit -n insight-system
    ```

2. 在 `INPUT`下添加以下内容并保存：

    ```yaml
        [INPUT]
            Name               tail
            Tag                audit_log.k8s.*
            Path               /var/log/*/audit/*.log
            DB                 /run/flb_audit.db
            Mem_Buf_Limit      15MB
            Buffer_Chunk_Size  1MB
            Buffer_Max_Size    5MB
            #DB.Sync           Normal
            Refresh_Interval   10
    ```

2. 重启 Master 节点上运行的 fluentbit pod，重启后的 FluentBit 将开启采集 `/var/log/kubernetes/audit` 下的日志。

> 如果需要停止采集 Kubernetes 审计日志，删除对应 `INPUT` 即可。

## 关闭采集审计日志

1. 如果需要停止采集 `全局管理` 的审计日志，删除以下 `INPUT` 并保存：

    ```
        [INPUT] 
            Name               tail 
            Tag                audit_log.ghippo.* 
            Parser             docker 
            Path               /var/log/containers/*_ghippo-system_audit-log*.log 
            DB                 /run/flb_audit.db 
            Mem_Buf_Limit      15MB 
            Buffer_Chunk_Size  1MB 
            Buffer_Max_Size    5MB 
            #DB.Sync           Normal 
            Refresh_Interval   10
    ```

2. 重启 Master 节点上运行的 fluentbit pod 即可停止收集`全局管理`的审计日志。
