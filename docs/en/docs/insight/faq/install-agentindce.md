# Install insight-agent in DCE 4.0

In DCE 5.0, the previous DCE 4.0 can be connected as a subcluster.
However, since most DCE 4.0 clusters have already installed dx-insight as a monitoring system, installing insight-agent at this time will conflict with the existing prometheus operator in the cluster, resulting in failure to install smoothly.

## plan

The solution is: enable the parameters of the prometheus operator, retain the prometheus operator in dx-insight, and be compatible with the prometheus operator of insight-agent in 5.0.

The specific operation steps are as follows:

1. Log in to the console.
1. Enable the `--deny-namespaces` parameter in the two prometheus operators respectively.
1. Execute the following command (the following command is for reference only, the prometheus operator name and namespace in the command need to be replaced actually).

    ```bash
    kubectl edit deploy insight-agent-kube-prometh-operator -n insight-system
    ```

    

!!! note

    - As shown above, the dx-insight component is deployed under the dx-insight tenant, and insight-agent is deployed under the insight-system tenant.
      Add `--deny-namespaces=insight-system` to the prometheus operator in dx-insight,
      Add `--deny-namespaces=dx-insight` to prometheus operator in insight-agent.
    - Only add deny namespace, both prometheus operators can continue to scan other namespaces, and related collection resources under kube-system or customer business namespace will not be affected.
    - Please pay attention to the problem of node exporter port conflict.

## Supplementary instructions

The open source `node-exporter` enables hostnetwork by default and the default port is 9100.
If `node-exporter` has been installed in the existing monitoring system of the cluster, the installation of `insight-agent` will not work properly due to the node-exporter port conflict.

!!! note

    Insight's `node exporter` will enable some features to collect special indicators, so it is recommended to install it.

Currently, it is not supported to modify the port in the installation command, you need to manually modify the related ports of insight node-exporter daemonset and svc after `helm install insight-agent`.