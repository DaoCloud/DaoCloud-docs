# 开启/关闭审计日志

默认 Kubernetes 集群不会输出审计日志信息。通过以下配置，可以开启 Kubernetes 的审计日志功能。

1. 准备审计日志的 Policy 文件
2. 配置 API 服务器，开启审计日志
3. 重启并验证

## 准备审计日志 Policy 文件

??? note "点击查看审计日志 Policy YAML 文件"

    ```yaml  title="policy.yaml"
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

将以上审计日志文件放到 `/etc/kubernetes/audit-policy/` 文件夹下，并取名为 `apiserver-audit-policy.yaml`。

## 配置 API 服务器

打开 API 服务器的配置文件 kube-apiserver.yaml，一般会在 `/etc/kubernetes/manifests/` 文件夹下，并添加以下配置信息：

这一步操作前请备份 kube-apiserver.yaml，并且备份的文件不能放在 `/etc/kubernetes/manifests/` 下，建议放在 `/etc/kubernetes/tmp`。

1. 在 `spec.containers.command` 下添加命令：

    ```yaml
    --audit-log-maxage=30
    --audit-log-maxbackup=1
    --audit-log-maxsize=100
    --audit-log-path=/var/log/audit/kube-apiserver-audit.log
    --audit-policy-file=/etc/kubernetes/audit-policy/apiserver-audit-policy.yaml
    ```

2. 在 `spec.containers.volumeMounts` 下添加：

    ```yaml
    - mountPath: /var/log/audit
      name: audit-logs
    - mountPath: /etc/kubernetes/audit-policy
      name: audit-policy
    ```

3. 在 `spec.volumes` 下添加：

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

## 测试并验证

稍等一会，API 服务器会自动重启，在 `/var/log/kubernetes/audit` 目录下查看是否有审计日志生成。

如果想关闭，去掉 `spec.containers.command` 中的相关命令即可。

## 开启审计日志的采集

通过 FluentBit 来采集审计日志。默认 FluentBit 不会会采集 `/var/log/kubernetes/audit` 下的日志文件（Kubernetes 审计日志）。

如需开启审计日志，按以下步骤操作：

1. 保存当前 value

    ```shell
    helm get values insight-agent -n insight-system -o yaml > insight-agent-values-bak.yaml
    ```

2. 获取当前版本号 ${insight_version_code}，然后更新配置

    ```shell
    insight_version_code=`helm list -n insight-system |grep insight-agent | awk {'print $10'}` 
    ```

    ```shell
    helm upgrade --install --create-namespace --version ${insight_version_code} --cleanup-on-fail insight-agent insight-release/insight-agent -n insight-system -f insight-agent-values-bak.yaml --set global.exporters.auditLog.kubeAudit.enabled=true 
    ```

    如果因为版本未找到而升级失败，请检查命令中使用的 helm repo 是否有这个版本。
    若没有，请尝试更新 helm repo 后重试。

    ```shell
    helm repo update insight-release
    ```

3. 重启所有 Pod

    重启所有 master 节点的 FluentBit Pod，重启后的 FluentBit 将会采集 `/var/log/kubernetes/audit` 下的日志。

## 禁用审计日志的采集

如需禁用 K8s 审计日志，按以下步骤操作：

1. 保存当前 value

    ```shell
    helm get values insight-agent -n insight-system -o yaml > insight-agent-values-bak.yaml
    ```

2. 获取当前版本号 ${insight_version_code}，然后更新配置

    ```shell
    insight_version_code=`helm list -n insight-system |grep insight-agent | awk {'print $10'}` 
    ```

    与开启相比，以下这条命令只是将 true 改为了 false。

    ```shell
    helm upgrade --install --create-namespace --version ${insight_version_code} --cleanup-on-fail insight-agent insight-release/insight-agent -n insight-system -f insight-agent-values-bak.yaml --set global.exporters.auditLog.kubeAudit.enabled=false 
    ```

    如果因为版本未找到而升级失败，请检查命令中使用的 helm repo 是否有这个版本。
    若没有，请尝试更新 helm repo 后重试。

    ```shell
    helm repo update insight-release
    ```

3. 重启所有 Pod

    重启所有 master 节点的 FluentBit Pod，重启后的 FluentBit 将不再采集 `/var/log/kubernetes/audit` 下的日志。

!!! note

    此外，如果想停止全局管理的审计日志采集，可以执行 `kubectl edit cm insight-agent-fluent-bit-config -n insight-system`，删除以下 INPUT 即可：

    ```console
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
