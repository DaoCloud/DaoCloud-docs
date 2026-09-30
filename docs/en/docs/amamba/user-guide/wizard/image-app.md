# Building Microservices Apps from Container Images

This article explains how to build a traditional microservices application from container image source
code, enabling features such as traffic governance, log viewing, monitoring, and tracing.

## Prerequisites

- You need to create a workspace and a user who is added to the workspace with the __workspace edit__ role.
  Refer to [Creating a Workspace](../../../ghippo/user-guide/workspace/workspace.md) and
  [Users and Roles](../../../ghippo/user-guide/access-control/user.md).
- Create a credential that can access the image repo. See [Credential Management](../pipeline/credential.md).

## Create Credentials

Following [Credential Management](../pipeline/credential.md), create the credential first:

1. On the __Credentials__ page, create a credential:

    - registry-credential: Username and password for accessing the image repo.

2. Once created, you can view the credential on the __Credential List__ page.

## Create Microservices App from Container Images

1. In the __Workbench__ -> __Wizard__ page, click __Build With Image__.

    ![Wizard](../../images/image01.png)

2. Fill in the basic information and click __Next__.

    ![Basic Information](../../images/image02.png)

    | Parameter | Description |
    |-----|---- |
    | Name | Specify the name of the resource workload |
    | Resource Type | In this demonstration, select Deployment. Currently, only Deployments are supported |
    | Deployment Location | Choose the cluster and namespace where the application will be deployed. If you want to integrate with microservices, make sure you have [created a registry](../../../skoala/trad-ms/hosted/index.md) in the current workspace. |
    | Application | Specify the name of the native application. You can select from an existing list or create a new one, which by default will have the same name as specified |
    | Replicas | Set the number of Pods for the application |

3. Fill in the container configuration and click __Next__.

    ![Container Configuration](../../images/image03.png)

    - Service Configuration: Specify how the service can be accessed within the cluster, node, or
      load balancer. Example values:

        name | protocol | port | targetPort
        ---- | -------- | ---- | ----------
        http | TCP      | 8081 | 8081
        health-http | TCP | 8999 | 8999
        service | TCP      | 9555 | 9555
        
        > For more detailed information about service configuration, refer to [Creating Services](../../../kpanda/user-guide/network/create-services.md).
        
    - Resource Limits: Specify the resource limits for the application, including CPU and memory.
    - Lifecycle: Set commands that need to be executed during container startup, after startup,
      and before shutdown. For more details, refer to
      [Container Lifecycle Configuration](../../../kpanda/user-guide/workloads/pod-config/lifecycle.md).
    - Health Checks: Define health checks to determine the health status of the container and application,
      improving availability. For more details, refer to
      [Container Health Check Configuration](../../../kpanda/user-guide/workloads/pod-config/health-check.md).
    - Environment Variables: Configure container parameters, add environment variables, or pass
      configurations to the Pod. For more details, refer to
      [Container Environment Variable Configuration](../../../kpanda/user-guide/workloads/pod-config/env-variables.md).
    - Data Storage: Configure data volume mounting and data persistence for containers.
    - Network Configuration: Configure DNS-related settings.

4. On the __Advanced Settings__ page, click __Access MicroServices__. Configure the parameters as per
   the instructions below, and click __OK__.

    ![Advanced Configuration](../../images/image04.png)

    | Parameter | Description |
    |-------|------|
    | Framework Selection | Supports **Spring Cloud** and **Dubbo**. In this case, select **Spring Cloud** |
    | Registry Instance | Currently, only hosted Nacos registry instances from the [Microservices Engine](../../../skoala/trad-ms/hosted/index.md) are supported |
    | Registry Namespace | The Nacos namespace for the microservices application |
    | Registry Service Group | The service group for the microservices application |
    | Username/Password | If the registry instance requires authentication, enter the username and password |
    | Enable Service Governance | The selected registry instance should have [Sentinel or Mesh governance plugins enabled](../../../skoala/trad-ms/hosted/plugins/plugin-center.md) |

## Viewing and Accessing Microservices Information

1. On the left navigation bar, click __Overview__, and within the __Native Applications__ tab, select the
   native application to view its details.

    ![Native Applications](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/git04.png)

2. In the details page, under the __Application Resources__ tab, select the resource with the
   __Service Mesh__ label and click its name.

    ![Navigate](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/git05.png)

3. You will be redirected to the Microservices Engine where you can view the
   [service details](../../../skoala/trad-ms/hosted/services/check-details.md).
