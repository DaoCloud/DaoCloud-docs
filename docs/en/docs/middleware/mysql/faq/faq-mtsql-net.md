# Handle Network Fluctuations in MySQL Master-Slave Mode

## Background

The high availability guarantee in MySQL master-slave mode is independent of the cluster, which can lead to misjudgments. For example, consider the following cluster:

<!--Add image later-->

Suppose the master's network experiences a brief disconnection (lasting longer than the failover tolerance time set by `orch`). `Orch` will perform a failover, promoting one of the slaves to master. However, if the master's network recovers shortly after the switch, this failover operation would be redundant.

To handle such scenarios, we can disable `orch`'s automatic switch capability for the MySQL cluster.

!!! note

    This is applicable in situations where the network status of the cluster is uncontrollable. The principle is to ignore the master when `orch` detects that the master's network is unreachable.

### Steps

1. For the `common-mysql` database, use Helm to update the operator:

    ```shell
    helm -n mcamel-system get values mysql-operator > values.yaml
    ```

2. Retrieve the values set during the previous installation and upgrade the mysql-operator:

    ```shell
    helm upgrade \
      --install mysql-operator \
      --create-namespace \
      -n mcamel-system \
      --cleanup-on-fail mcamel-release/mysql-operator \
      --version 0.14.0-rc2 \
      -f values.yaml
      --set "orchestrator.config.RecoveryIgnoreHostnameFilters[0]=^mcamel-common"  # (1)!
    ```

    1. This is a regular expression that will match with the MySQL pod names.

!!! note

    Ensure that the operator restarts after execution is complete.
    Ensure that the `mysql-operator-orc` configmap includes the content set by `--set` after execution is complete.

## Verification Plan

1. Create a 3-node master-slave cluster (with `-0` as the master), ensuring the name matches the regular expression set above:

    <!--Add image later-->

2. Disconnect the master's network:

    <!--Add image later-->

3. Observe that no master switch occurs:

    <!--Add image later-->

4. Observe that the cluster has returned to normal, with `-0` still as the master:

    <!--Add image later-->

!!! note

    Additionally, verify that for clusters whose names do not match the regular expression set above, the same steps result in a normal switch.
