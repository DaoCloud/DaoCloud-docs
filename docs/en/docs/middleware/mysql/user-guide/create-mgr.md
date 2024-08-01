# Create MySQL MGR Instance

MySQL Group Replication (MGR) is a solution for achieving consistent synchronization between different nodes in a distributed database system, providing a fault-tolerant and highly available cluster environment. It uses state updates from all servers in the replication group to achieve high-speed and reliable data redundancy.

## Prerequisites

Before setting up an MGR cluster, ensure the following prerequisites are met:

- The MySQL-Operator has been deployed in the target cluster and is in a running state.

## Steps

1. In the instance list, click the dropdown button __Create MGR Instance__.

2. Fill in the basic information of the instance, and select the deployment cluster and namespace.

    The system will check the installation prerequisites for the selected deployment locations. If the check fails, please follow the system prompts to install the necessary components.

3. Choose the specifications for the deployment instance and click __Next__.

    - Version: Currently, only version 8.0.31 is supported.
    - Replica Count: The replica count range for MGR single-master mode is 3 - 9. It is recommended to use an odd number of replicas.

4. Configure the instance's access settings and click __Next__.

    - Access Type: Choose the type of access service exposed by the instance.
    - Management Tool: Enable this option to manage MySQL using the phpMyAdmin management tool.

5. After confirming that the instance configuration is correct, click Confirm to complete the creation and return to the alarm template list.
