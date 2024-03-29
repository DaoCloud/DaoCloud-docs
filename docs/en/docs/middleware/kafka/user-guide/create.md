---
hide:
  - toc
---

# Create Kafka

In the Kafka message queue, follow these steps to create a Kafka instance.

1. On the Kafka message queue page, click the __Create Instance__ button in the top right corner.

    <!--add screenshot later-->

    !!! tip

        When deploying for the first time, you can click **Deploy Now**.

        <!--add screenshot later-->

2. On the __Create Kafka Instance__ page, after setting the basic information, click __Next__.

    <!--add screenshot later-->

3. After configuring the specifications, click __Next__.

    - Version: The version of Kafka, currently only supports Kafka 3.1.0.
    - Replicas: Supports 1, 3, 5, 7 replicas.
    - Resource Quota: Choose rules according to the actual situation.
    - Storage Volumes: Select the storage volume and total storage space for the Kafka instance.

    <!--add screenshot later-->

4. After service settings, click __Next__.

    - Service Settings:
        - Cluster Internal Access (ClusterIP)
        - Node Port (Nodeport)
        - Load Balancer (LoadBalancer)
    - Access Settings:
        - Access Account Configuration: Username and password to connect to the Kafka instance.
        - CMAK Resource Configuration: Replicas, CPU, and memory quotas.
        - Access Type Configuration: Node Port (Nodeport), Load Balancer (LoadBalancer)
    - Advanced Settings: Configure as needed.

    <!--add screenshot later-->

5. Confirm that the instance configuration information is correct, click __Confirm__ to complete the creation.

    <!--add screenshot later-->

6. Check the instance list page to see if the instance has been created successfully. The status of the newly created instance will be __Not Ready__, and after a few minutes, this status will change to __Running__.

    <!--add screenshot later-->

!!! note

    In addition, DCE 5.0's Kafka provides parameter templates to simplify instance creation.
    You can use these predefined [parameter templates](./template.md) to create instances.
