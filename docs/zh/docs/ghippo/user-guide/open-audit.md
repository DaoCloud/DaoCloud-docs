# 开启/关闭采集k8s审计日志

## 名称解释

- k8s审计日志：k8s本身生成审计日志，开启该功能后，会在指定目录下生成k8s审计日志的日志文件
- 采集k8s审计日志：通过insight-agent采集上述‘k8s审计日志’的日志文件，’采集k8s审计日志‘ 的前提条件是集群开启了上述 ‘k8s审计日志‘

## dce5.0安装完成时状态

- 社区版安装管理集群过程中未操作k8s审计日志开关
- 商业版管理集群的k8s审计日志开关默认开启
    - 如需设置成默认关闭，可修改安装器clusterConfigt.yaml来配置（logPath 设置为空”“）
- 管理集群的采集k8s审计日志开关默认关闭
    - 默认设置不支持配置

## 管理集群采集k8s审计日志开关

### 商业版安装环境

#### 确认开启k8s审计日志

通过命令

    ls /var/log/kubernetes/audit
 
查看`/var/log/kubernetes/audit` 目录下是否有审计日志生成，若有，则表示k8s审计日志成功开启。

若未开启，请参考[文档的开启关闭k8s审计日志](#k8s)

#### 开启采集k8s审计日志流程

1. 添加chartmuseum到helm repo中

    ```shell
    helm repo add chartmuseum http://10.5.14.30:8081   # IP需要修改为火种节点的IP地址
    ```
    
2. 保存当前insight-agent helm value

    ```shell
    helm get values insight-agent -n insight-system -o yaml > insight-agent-values-bak.yaml
    ```
    
3. 获取当前版本号 ${insight_version_code}

    ```shell
    insight_version_code=`helm list -n insight-system |grep insight-agent | awk {'print $10'}` 
    ```

4. 更新helm value配置

    ```shell
    helm upgrade --install --create-namespace --version ${insight_version_code} --cleanup-on-fail insight-agent chartmuseum/insight-agent -n insight-system -f insight-agent-values-bak.yaml --set global.exporters.auditLog.kubeAudit.enabled=true
    ```

5. 重启insight-system下的所有fluentBit pod 

    ```shell
    fluent_pod=`kubectl get pod -n insight-system | grep insight-agent-fluent-bit | awk {'print $1'} | xargs`
    kubectl delete pod ${fluent_pod} -n insight-system
    ```
    
#### 关闭采集k8s审计日志

其余步骤和开启采集k8s审计日志一致，仅需修改第4步:
更新helm value配置

    ```shell
    helm upgrade --install --create-namespace --version ${insight_version_code} --cleanup-on-fail insight-agent chartmuseum/insight-agent -n insight-system -f insight-agent-values-bak.yaml --set global.exporters.auditLog.kubeAudit.enabled=false
    ```

### 社区版在线安装环境

#### 开启采集k8s审计日志流程

1. 保存当前 value

    ```shell
    helm get values insight-agent -n insight-system -o yaml > insight-agent-values-bak.yaml
    ```

2. 获取当前版本号 ${insight_version_code}，然后更新配置

    ```shell
    insight_version_code=`helm list -n insight-system |grep insight-agent | awk {'print $10'}` 
    ```

3. 更新helm value配置
    ```shell
    helm upgrade --install --create-namespace --version ${insight_version_code} --cleanup-on-fail insight-agent insight-release/insight-agent -n insight-system -f insight-agent-values-bak.yaml --set global.exporters.auditLog.kubeAudit.enabled=true 
    ```

    如果因为版本未找到而升级失败，请检查命令中使用的 helm repo 是否有这个版本。
    若没有，请尝试更新 helm repo 后重试。

    ```shell
    helm repo update insight-release
    ```

4. 重启insight-system下的所有fluentBit pod 

    ```shell
    fluent_pod=`kubectl get pod -n insight-system | grep insight-agent-fluent-bit | awk {'print $1'} | xargs`
    kubectl delete pod ${fluent_pod} -n insight-system
    ```

#### 关闭采集k8s审计日志

其余步骤和开启采集k8s审计日志一致，仅需修改第3步:
更新helm value配置

    ```shell
    helm upgrade --install --create-namespace --version ${insight_version_code} --cleanup-on-fail insight-agent insight-release/insight-agent -n insight-system -f insight-agent-values-bak.yaml --set global.exporters.auditLog.kubeAudit.enabled=false
    ```


## 工作集群开关

各工作集群开关独立，按需开启

### 创建集群时打开采集审计日志步骤

采集k8s审计日志功能默认为关闭状态，若需要开启，可以按照如下步骤：

![image](../../images/worker01.png)

![image](../../images/worker02.png)

将该按钮设置为启用状态，开启采集k8s审计日志功能

通过dce5.0创建工作集群时，确认该集群的k8s审计日志选择‘true'，这样创建出来的工作集群k8s审计日志是开启的

![image](../../images/worker03.png)

等待集群创建成功后，该工作集群的k8s审计日志将被采集

### 接入的集群和创建完成后开关步骤

#### 确认开启k8s审计日志

通过命令

    ls /var/log/kubernetes/audit

查看`/var/log/kubernetes/audit` 目录下是否有审计日志生成，若有，则表示k8s审计日志成功开启。

若未开启，请参考[文档的开启关闭k8s审计日志](#k8s)

#### 开启采集k8s审计日志

采集k8s审计日志功能默认为关闭状态，若需要开启，可以按照如下步骤

1. 选中已接入并且需要开启采集k8s审计日志功能的集群

![image](../../images/worker04.png)

2. 进入helm应用管理页面，更新insight-agent配置 （若未安装insight-agent，可以参考文档：[安装insight-agent](https://docs.daocloud.io/insight/user-guide/quickstart/install-agent/)）

![image](../../images/worker05.png)

3. 开启\关闭采集k8s审计日志按钮

![image](../../images/worker06.png)

4. 接入集群的情况下开关后仍需要重启fluent-bit pod 才能生效

![image](../../images/worker07.png)

## 开启关闭k8s审计日志

默认 Kubernetes 集群不会输出审计日志信息。通过以下配置，可以开启 Kubernetes 的审计日志功能。

1. 准备审计日志的 Policy 文件
2. 配置 API 服务器，开启审计日志
3. 重启并验证

### 准备审计日志 Policy 文件

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

### 配置 API 服务器

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

### 测试并验证

稍等一会，API 服务器会自动重启，通过命令

```shell
ls /var/log/kubernetes/audit
```

查看`/var/log/kubernetes/audit` 目录下是否有审计日志生成，若有，则表示k8s审计日志成功开启。

如果想关闭，去掉 `spec.containers.command` 中的相关命令即可。
