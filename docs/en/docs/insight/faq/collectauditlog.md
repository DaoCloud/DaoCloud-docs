# Enable collection of audit logs

The Kubernetes audit log is a detailed description of every call to the Kubernetes API Server.
Auditing provides security-related time-series operation records (including time, source, operation result, user who initiated the operation, resource of the operation, and request/response details, etc.).
The audit log data collected by the fifth-generation product mainly comes from the Kubernetes audit log and `global management` audit log.
Considering the data volume of audit logs, Insight does not collect Kubernetes audit logs by default, but only collects `global management` audit logs.

**Prerequisites**: The target cluster has `insight-agent` installed and is in `running` state.

## Enable Kubernetes audit logging

1. Configure the audit log policy file, put the following yaml in the `/etc/kubernetes/audit-policy/` folder, and name it `apiserver-audit-policy.yaml`

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
        -group: "" # core
          resources: ["endpoints", "services", "services/status"]
      - level: None
        # Ingress controller reads `configmaps/ingress-uid` through the unsecured port.
        # TODO(#46983): Change this to the ingress controller service account.
        users: ["system:unsecured"]
        namespaces: ["kube-system"]
        verbs: ["get"]
        resources:
        -group: "" # core
          resources: ["configmaps"]
      - level: None
        users: ["kubelet"] # legacy kubelet identity
        verbs: ["get"]
        resources:
        -group: "" # core
          resources: ["nodes", "nodes/status"]
      - level: None
        userGroups: ["system:nodes"]
        verbs: ["get"]
        resources:
        -group: "" # core
          resources: ["nodes", "nodes/status"]
      - level: None
        users:
        - system:kube-controller-manager
        - system:kube-scheduler
        - system:serviceaccount:kube-system:endpoint-controller
        verbs: ["get", "update"]
        namespaces: ["kube-system"]
        resources:
        -group: "" # core
          resources: ["endpoints"]
      - level: None
        users: ["system:apiserver"]
        verbs: ["get"]
        resources:
        -group: "" # core
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
        -group: "" # core
          resources: ["events"]
            
      # new start
      # Ignore all APIs that access non-authenticated ports, usually system components such as Kube-Controller, etc.
      - level: None
        users: ["system:unsecured"]

      # Ignore kube-admin audit logs
      - level: None
        users: ["kube-admin"]
      # API need add that ignores all resource status updates
      - level: None
        resources:
        -group: "" # core
        resources: ["events", "nodes/status", "pods/status", "services/status"]
        - group: "authorization.k8s.io"
        resources: ["selfsubjectrulesreviews"]
      # ignore leases need add
      - level: None
        resources:
        - group: "coordination.k8s.io"
        resources: ["leases"]
      -level: Request
        verbs: ["create", "update", "patch", "delete"]
        users: ["kube-admin"]
      #new end

      # Secrets, ConfigMaps, and TokenReviews can contain sensitive & binary data,
      # so only log at the Metadata level.
      - level: Metadata
        resources:
        -group: "" # core
          resources: ["secrets", "configmaps"]
        -group: authentication.k8s.io
          resources: ["token reviews"]
        omitStages:
        - "RequestReceived"
      # Get responses can be large; skip them.
      -level: Request
        verbs: ["get", "list", "watch"]
        resources:
        -group: "" # core
        - group: "admissionregistration.k8s.io"
        - group: "apiextensions.k8s.io"
        - group: "apiregistration.k8s.io"
        -group: "apps"
        -group: "authentication.k8s.io"
        - group: "authorization.k8s.io"
        -group: "autoscaling"
        -group: "batch"
        - group: "certificates.k8s.io"
        -group: "extensions"
        - group: "metrics.k8s.io"
        - group: "networking.k8s.io"
        -group: "policy"
        - group: "rbac.authorization.k8s.io"
        - group: "settings.k8s.io"
        -group: "storage.k8s.io"
        omitStages:
        - "RequestReceived"
      # Default level for known APIs
      - level: RequestResponse
        resources:
        -group: "" # core
        - group: "admissionregistration.k8s.io"
        - group: "apiextensions.k8s.io"
        - group: "apiregistration.k8s.io"
        -group: "apps"
        -group: "authentication.k8s.io"
        - group: "authorization.k8s.io"
        -group: "autoscaling"
        -group: "batch"
        - group: "certificates.k8s.io"
        -group: "extensions"
        - group: "metrics.k8s.io"
        - group: "networking.k8s.io"
        -group: "policy"
        - group: "rbac.authorization.k8s.io"
        - group: "settings.k8s.io"
        -group: "storage.k8s.io"
        omitStages:
        - "RequestReceived"
      # Default level for all other requests.
      - level: Metadata
        omitStages:
        - "RequestReceived"
    ```

1. Open the configuration file `kube-apiserver.yaml` of `api-server`, which is usually located in the `/etc/kubernetes/manifests/` folder, and add the following configuration information:

    - Add command under `spec.containers.command`:

        ```sh
        --audit-log-maxage=30
        --audit-log-maxbackup=1
        --audit-log-maxsize=100
        --audit-log-path=/var/log/audit/kube-apiserver-audit.log
        --audit-policy-file=/etc/kubernetes/audit-policy/apiserver-audit-policy.yaml
        ```

    - Add under `spec.containers.volumeMounts`:

        ```yaml
        - mountPath: /var/log/audit
          name: audit-logs
        - mountPath: /etc/kubernetes/audit-policy
          name: audit-policy
        ```

    - Add under `spec.volumes`:

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

1. Wait a few minutes for `api-server` to restart successfully, check whether there is an audit log generated in the `/var/log/kubernetes/audit` directory, and verify whether the Kubernetes audit log is successfully enabled.

!!! tip

    If you want to close it, just delete the relevant commands in `spec.containers.command`.

## Enable collection of audit logs

Observability collects audit logs through `FluentBit`.
By default `FluentBit` will not collect log files (Kubernetes audit logs) under `/var/log/kubernetes/audit`.
Follow the steps below to start collecting audit logs:

1. To modify the ConfigMap of `FluentBit`, execute the following command:

    ```shell
    kubectl edit cm insight-agent-fluent-bit -n insight-system
    ```

1. Add the following content under `INPUT` and save:

    ```none
        [INPUT]
            Name tail
            Tag audit_log.k8s.*
            Path /var/log/*/audit/*.log
            DB /run/flb_audit.db
            Mem_Buf_Limit 15MB
            Buffer_Chunk_Size 1MB
            Buffer_Max_Size 5MB
            #DB.Sync Normal
            Refresh_Interval 10
    ```

1. Restart the fluentbit Pod running on the Master node. After the restart, FluentBit will start collecting logs under `/var/log/kubernetes/audit`.

!!! tip

    If you need to stop collecting Kubernetes audit logs, just delete the corresponding `INPUT`.

## Close collection of audit logs

1. If you need to stop collecting `global management` audit logs, delete the following `INPUT` and save:

    ```none
        [INPUT]
            Name tail
            Tag audit_log.ghippo.*
            Parser docker
            Path /var/log/containers/*_ghippo-system_audit-log*.log
            DB /run/flb_audit.db
            Mem_Buf_Limit 15MB
            Buffer_Chunk_Size 1MB
            Buffer_Max_Size 5MB
            #DB.Sync Normal
            Refresh_Interval 10
    ```

1. Then restart the fluentbit Pod running on the Master node to stop collecting `global management` audit logs.