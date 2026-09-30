# Koordinator Offline Installation

Koordinator is a QoS-based Kubernetes mixed-workload scheduling system. It aims to improve the runtime efficiency and reliability of latency-sensitive workloads and batch jobs,
simplify the complexity of resource-related configuration tuning, and increase Pod deployment density to improve resource utilization.

DCE provides the Koordinator v1.5.0 offline package.

This document describes how to deploy Koordinator offline.

## Prerequisites

1. The user has installed the addon offline package of v0.20.0 or later on the platform.
2. The Kubernetes version of the target cluster is >= 1.18.
3. For the best experience, Linux kernel 4.19 or later is recommended.

## Procedure

Refer to the following steps to install the Koordinator plugin for the cluster.

1. Log in to the platform and go to __Container Management__ -> __the cluster where Koordinator is to be installed__ -> enter the cluster details.

2. On the __Helm Chart__ page, select __All Repositories__ and search for __koordinator__.

3. Select __koordinator__ and click __Install__.

    ![Click Install](../images/koordinator_helm.png)

4. On the Koordinator installation page, click __OK__ to install Koordinator with the default configuration.

    ![Use the Default Configuration](../images/koordinator_install.png)

5. Check whether the Pods in the koordinator-system namespace are running properly.

    ![Check Pods](../images/koordinator_system_pod.png)
