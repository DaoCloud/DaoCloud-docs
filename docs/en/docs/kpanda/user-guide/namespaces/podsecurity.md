# Container Group Security Policies

Container group security policies in a Kubernetes cluster allow you to control the behavior of Pods in various security aspects by configuring different levels and modes for specific namespaces. Only Pods that meet certain conditions will be accepted by the system. There are three levels and three modes available, and users can choose the most suitable options based on their needs to set up restriction policies.

!!! note

    Only one security policy can be configured for each security mode. Please be cautious when configuring the `enforce` security mode for namespaces, as any violations will result in Pod creation failure.

This section will explain how to configure container group security policies for namespaces using the container management interface.

## Prerequisites

- The container management module has been integrated with a Kubernetes cluster or a Kubernetes cluster has been created. The cluster version needs to be v1.22 or above, and access to the UI interface of the cluster is required.

- A namespace has been created, and a user has been created and granted the `NS Admin` or higher permission level. For more details, refer to [Namespace Authorization](../permissions/cluster-ns-auth.md).

## Configuring Container Group Security Policies for a Namespace

1. Select the namespace for which you want to configure the container group security policies and navigate to its details page. Click `Configure Policy` on the `Container Group Security Policies` page to enter the configuration page.


2. On the configuration page, click `Add Policy` to create a new policy. You will need to specify the security level and security mode. The following table provides detailed descriptions of the security levels and security modes.

    | Security Level | Description                                                                                                                                                                     |
    | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Privileged     | Unrestricted policy that provides the widest range of permissions. This policy allows known privilege escalations.                                                               |
    | Baseline       | The least restrictive policy that disallows known privilege escalations. It allows the use of default (minimum required) Pod configurations.                                    |
    | Restricted     | A highly restrictive policy that follows best practices for protecting Pods.                                                                                                   |

    | Security Mode | Description                                                                                                             |
    | ------------- | ----------------------------------------------------------------------------------------------------------------------- |
    | Audit         | Violations of the specified policy will add new audit events in the audit log, and Pods can be created.                  |
    | Warn          | Violations of the specified policy will return visible warning messages to users, and Pods can be created.               |
    | Enforce       | Violations of the specified policy will result in the inability to create Pods.                                          |

    ![Add Policy](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/ps02.png)

3. Different security levels correspond to different checks. If you are unsure how to configure your namespace, you can click `Policy Configuration Explanation` in the upper right corner of the page to view detailed information.


4. Click `OK` to save the configuration. If successful, the configured security policy will appear on the page.


5. By clicking on `Actions`, you can edit or delete the configured security policies.

