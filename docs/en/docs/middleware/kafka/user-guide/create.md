---
hide:
  - toc
---

# Create Kafka

In the Kafka message queue, perform the following operations to create a Kafka instance.

1. Click `New Instance` in the upper right corner.

    <!--screenshot-->

2. On the `Create Kafka Instance` page, after setting the basic information, click `Next`.

    <!--screenshot-->

3. After configuring the specifications, click `Next`.

    - Version: The version number of Kafka, currently only supports Kafka 3.1.0.
    - Number of copies: 1, 3, 5, 7 copies are supported.
    - Resource Quota: Select the rules according to the actual situation.
    - Storage Volume: Select the storage volume and the total amount of storage space for the Kafka instance.

    <!--screenshot-->

4. After setting up the service, click `Next`.

    - Access method: You can choose intra-cluster access or Nodeport access.
    - Service Settings: Set the username and password for connecting to the Kafka instance.

    <!--screenshot-->

5. Confirm that the instance configuration information is correct, and click `OK` to complete the creation.

    <!--screenshot-->

6. On the instance list page, check whether the instance is successfully created. The status of the newly created instance is `Not Ready`, and it will change to `Running` after a few minutes.

    <!--screenshot-->