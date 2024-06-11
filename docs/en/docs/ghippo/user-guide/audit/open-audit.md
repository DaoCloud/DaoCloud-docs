# Enable/Disable collection of audit logs

- Kubernetes Audit Logs: Kubernetes itself generates audit logs. When this feature is enabled, audit log files for
  Kubernetes will be created in the specified directory.
- Collecting Kubernetes Audit Logs: The log files mentioned above are collected using the Insight Agent. The 
  prerequisite for collecting Kubernetes audit logs are that the cluster has enabled Kubernetes audit logs,  the 
  export of audit logs has been allowed, and the collection of audit logs has been opened.

## DCE 5.0 Installation Status

- For DCE Community installations, the Kubernetes audit log switch was not operated during the management cluster
  installation process.
- For DCE 5.0 Enterprise installations, the Kubernetes audit log switch is enabled by default.
    - To set it to default off, you can modify the installer's __clusterConfig.yaml__ file 
      (set __logPath__ to empty "").
- The collection of Kubernetes audit logs switch is disabled by default for the management cluster.
    - Default settings do not support configuration.

## Management Cluster Collection of Kubernetes Audit Logs Switch

### DCE 5.0 Enterprise Installation Environment

#### Confirm Enabling Kubernetes Audit Logs

Run the following command to check if audit logs are generated under the __/var/log/kubernetes/audit__ directory. 
If they exist, it means that Kubernetes audit logs are successfully enabled.

```shell
ls /var/log/kubernetes/audit
```

If they are not enabled, please refer to the [documentation on enabling/disabling Kubernetes audit logs](open-k8s-audit.md).

#### Enable Collection of Kubernetes Audit Logs Process

1. Add ChartMuseum to the helm repo.

    ```shell
    helm repo add chartmuseum http://10.5.14.30:8081
    ```

    Modify the IP address in this command to the IP address of the Spark node.

    !!! note

        If using a self-built Harbor repository, please modify the chart repo URL in the first step to the 
        insight-agent chart URL of the self-built repository.

2. Save the current Insight Agent helm values.

    ```shell
    helm get values insight-agent -n insight-system -o yaml > insight-agent-values-bak.yaml
    ```

3. Get the current version number ${insight_version_code}.

    ```shell
    insight_version_code=`helm list -n insight-system |grep insight-agent | awk {'print $10'}`
    ```

4. Update the helm value configuration.

    ```shell
    helm upgrade --install --create-namespace --version ${insight_version_code} --cleanup-on-fail insight-agent chartmuseum/insight-agent -n insight-system -f insight-agent-values-bak.yaml --set global.exporters.auditLog.kubeAudit.enabled=true
    ```

5. Restart all fluentBit pods under the insight-system namespace.

    ```shell
    fluent_pod=`kubectl get pod -n insight-system | grep insight-agent-fluent-bit | awk {'print $1'} | xargs`
    kubectl delete pod ${fluent_pod} -n insight-system
    ```

#### Disable Collection of Kubernetes Audit Logs

The remaining steps are the same as enabling the collection of Kubernetes audit logs, with only a modification 
in the previous section's step 4: updating the helm value configuration.

```shell
helm upgrade --install --create-namespace --version ${insight_version_code} --cleanup-on-fail insight-agent chartmuseum/insight-agent -n insight-system -f insight-agent-values-bak.yaml --set global.exporters.auditLog.kubeAudit.enabled=false
```

### DCE Community Online Installation Environment

!!! note

   If installing DCE Community in a Kind cluster, perform the following steps inside the Kind container.

#### Confirm Enabling Kubernetes Audit Logs

Run the following command to check if audit logs are generated under the __/var/log/kubernetes/audit__ directory. 
If they exist, it means that Kubernetes audit logs are successfully enabled.

```shell
ls /var/log/kubernetes/audit
```

If they are not enabled, please refer to the [documentation on enabling/disabling Kubernetes audit logs](open-k8s-audit.md).

#### Enable Collection of Kubernetes Audit Logs Process

1. Save the current values.

    ```shell
    helm get values insight-agent -n insight-system -o yaml > insight-agent-values-bak.yaml
    ```

2. Get the current version number ${insight_version_code} and update the configuration.

    ```shell
    insight_version_code=`helm list -n insight-system |grep insight-agent | awk {'print $10'}`
    ```

3. Update the helm value configuration.

    ```shell
    helm upgrade --install --create-namespace --version ${insight_version_code} --cleanup-on-fail insight-agent insight-release/insight-agent -n insight-system -f insight-agent-values-bak.yaml --set global.exporters.auditLog.kubeAudit.enabled=true
    ```

    If the upgrade fails due to an unsupported version, check if the helm repo used in the command has that version.
    If not, retry after you updated the helm repo.

    ```shell
    helm repo update insight-release
    ```

4. Restart all fluentBit pods under the insight-system namespace.

    ```shell
    fluent_pod=`kubectl get pod -n insight-system | grep insight-agent-fluent-bit | awk {'print $1'} | xargs`
    kubectl delete pod ${fluent_pod} -n insight-system
    ```

#### Disable Collection of Kubernetes Audit Logs

The remaining steps are the same as enabling the collection of Kubernetes audit logs, with only a modification 
in the previous section's step 3: updating the helm value configuration.

```shell
helm upgrade --install --create-namespace --version ${insight_version_code} --cleanup-on-fail insight-agent insight-release/insight-agent -n insight-system -f insight-agent-values-bak.yaml --set global.exporters.auditLog.kubeAudit.enabled=false
```

## Work Cluster Switch

Each work cluster switch is independent and can be turned on as needed.

### Steps to Enable Audit Log Collection When Creating a Cluster

By default, the collection of K8s audit logs is turned off. If you need to enable it, you can follow these steps:

![Default Off](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/worker01.png)

![Enable Audit Logs](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/worker02.png)

Set the switch to the enabled state to enable the collection of K8s audit logs.

When creating a work cluster via DCE 5.0, ensure that the K8s audit log option for the cluster is set to 'true' so
that the created work cluster will have audit logs enabled.

![Audit Logs Enabled](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/worker03.png)

After the cluster creation is successful, the K8s audit logs for that work cluster will be collected.

### Steps to Enable/Disable After Accessing or Creating the Cluster

#### Confirm Enabling K8s Audit Logs

Run the following command to check if audit logs are generated under the __/var/log/kubernetes/audit__ directory. 
If they exist, it means that K8s audit logs are successfully enabled.

```shell
ls /var/log/kubernetes/audit
```

If they are not enabled, please refer to the [documentation on enabling/disabling K8s audit logs](open-k8s-audit.md).

#### Enable Collection of K8s Audit Logs

The collection of K8s audit logs is disabled by default. To enable it, follow these steps:

1. Select the cluster that has been accessed and needs to enable the collection of K8s audit logs.

    ![Select Cluster](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/worker04.png)

2. Go to the Helm application management page and update the insight-agent configuration (if insight-agent is not installed, 
   you can [install it](../../../insight/quickstart/install/install-agent.md)).

    ![Go to Helm Applications](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/worker05.png)

3. Enable/Disable the collection of K8s audit logs switch.

    ![Enable/Disable Switch](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/worker06.png)

4. After enabling/disabling the switch, the fluent-bit pod needs to be restarted for the changes to take effect.

    ![Restart Pods](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/worker07.png)
