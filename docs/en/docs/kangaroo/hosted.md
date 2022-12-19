# Manage Harbor

Harbor is an open source mirror warehouse service for secure hosting and efficient distribution of OCI-compliant Artifacts such as container images and Helm Charts. It can help you manage Artifacts consistently and securely across cloud-native computing platforms (such as Kubernetes and Docker). The DaoCloud Enterprise platform provides Harbor-based fast deployment capabilities, and realizes one-stop high availability, high performance, and high Efficient deployment, management, use and other full-cycle mirror warehouse services.

## Product Features

- Support multi-copy deployment to achieve high availability
- Support importing platform users into native Harbor instances
- Provide a native Harbor instance entry, and the user's operations on the platform UI and operations in the native Harbor will take effect in real time
- Support using the platform to build a database or access an external database
- Support using the platform to build a Redis instance or access an external Redis instance
- Support specifying internal storage or using external S3 compatible object storage

## Functional advantages

- Multiple mirror warehouse instances to meet the needs of multiple mirror warehouses in various environments such as development, testing, and production.
- Break the calling barriers between modules, and support rapid image pull when deploying applications in the application workbench and container management module
- Provides a unified management control plane, allowing administrators to manage the full life cycle of multiple Harbor instances on the same interface.

## Steps

1. Log in to the web console as a user with the Admin role, and click `Mirror Warehouse` from the left navigation bar.

    ![Mirror Warehouse](images/hosted01.png)

1. Click `Managed Harbor` on the left navigation bar, and click the `Create Instance` button in the upper right corner.

    ![Create instance](images/hosted02.png)

1. Fill in the instance name, select the deployment location and click `Next` (if there is no deployment location to choose, you need to go to the container management to create a cluster and namespace).

    ![Basic Information](images/hosted03.png)

1. Fill in the database, Redis instance and image/Charts storage information and click `Next` (currently only supports access to external databases and Redis instances).

    ![Specification configuration](images/hosted04.png)

1. Fill in the domain name, select the ingress instance, enter the administrator password and click `OK` (username/password is used to log in to the native Harbor instance, please keep the password safe).

    ![Access and Policy Binding](images/hosted05.png)

1. Return to the list of managed Harbor instances. The newly created instance is the first one by default. Wait for the status to change from 'Updating' to 'Healthy' before it can be used normally.

    ![Instance list](images/hosted06.png)

1. Click `...` on the right side of an instance, and you can choose to edit, delete, or enter the original Harbor.

    ![More Actions](images/hosted07.png)