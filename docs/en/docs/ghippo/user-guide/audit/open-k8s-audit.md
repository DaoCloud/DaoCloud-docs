# Enable/Disable the output of k8s audit logs

By default, the Kubernetes cluster does not output audit log information.
Through the following configuration, you can enable the audit log feature of Kubernetes.

!!! note

    In a public cloud environment, it may not be possible to control the output and output path of Kubernetes audit logs.

1. Prepare the Policy file for the audit log
2. Configure the API server and enable audit logs
3. Reboot and verify

## Prepare audit log policy file

??? note "Click to view Policy YAML for audit log"

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
      # Ignore all APIs accessing non-authenticated ports, usually system components such as Kube-Controller
      - level: None
        users: ["system:unsecured"]

      # Ignore audit log from kube-admin
      - level: None
        users: ["kube-admin"]
      # Ignore all APIs to update resource status
      - level: None
        resources:
        - group: "" # core
          resources: ["events", "nodes/status", "pods/status", "services/status"]
        - group: "authorization.k8s.io"
          resources: ["selfsubjectrulesreviews"]
      # Ignore leases need add
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

Put the above audit log file in `/etc/kubernetes/audit-policy/` folder, and name it `apiserver-audit-policy.yaml`.

## Configure the API server

Open the configuration file kube-apiserver.yaml of the API server, usually in the `/etc/kubernetes/manifests/` folder, and add the following configuration information:

Please back up kube-apiserver.yaml before this step, and the backup file cannot be placed under `/etc/kubernetes/manifests/`, it is recommended to put it in `/etc/kubernetes/tmp`.

1. Add the command under `spec.containers.command`:

    ```yaml
    --audit-log-maxage=30
    --audit-log-maxbackup=1
    --audit-log-maxsize=100
    --audit-log-path=/var/log/audit/kube-apiserver-audit.log
    --audit-policy-file=/etc/kubernetes/audit-policy/apiserver-audit-policy.yaml
    ```

2. Add below code under `spec.containers.volumeMounts`:

    ```yaml
    - mountPath: /var/log/audit
      name: audit-logs
    - mountPath: /etc/kubernetes/audit-policy
      name: audit-policy
    ```

3. Add below under `spec.volumes`:

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

## Test and verify

After a while, the API server will automatically restart. run the following command to check whether there is an audit log generated in the `/var/log/kubernetes/audit` directory. If so, it means that the k8s audit log is successfully enabled.

```shell
ls /var/log/kubernetes/audit
```

If you want to close it, just remove the relevant commands in `spec.containers.command`.
