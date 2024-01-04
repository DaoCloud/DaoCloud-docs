# Create the Argo CD application

Workbench is based on open source software [Argo CD](https://argo-cd.readthedocs.io/en/stable/) for continuous deployment. This page demonstrates how to implement continuous deployment of applications.

## prerequisites

- Need to create a workspace and a user, the user needs to join the workspace and give __workspace edit__ role.
  Refer to [Creating a workspace](../../../ghippo/user-guide/workspace/workspace.md), [Users and roles](../../../ghippo/user-guide/access-control/user.md).
- Prepare a Git repository.

## Create the Argo CD application

1. On the __Workbench__ -> __Continuous Release__ page, click the __Create Application__ button.

    <!--![]()screenshots-->

1. On the __Create Application__ page, after configuring __Basic Information__ , __Deployment Location__ , __Code Warehouse Source__ and __Sync Policy__ , click __OK__ .

    - Source of code repository:
        - Code repository: Select an imported code repository or enter a public code repository address. For example: https://github.com/argoproj/argocd-example-apps.git
        - Branch/Tag: Set the branch or tag of the code repository, the default is HEAD
        - Path: Fill in the manifest file path, for example gustbook
    - Synchronization strategy:
        - Manual synchronization: Manually click whether to synchronize
        - Automatic synchronization: Automatically detect changes in the manifest file in the code repository, and immediately synchronize the application resources to the latest state once the change occurs. And supports cleaning resources and self-recovery options:
            - Clean up resources: Delete resources that are no longer defined in the code warehouse during synchronization
            - Self-recovery: ensure synchronization with the desired state in the code repository
        - Sync settings:
            - Skip Validation Specification: Skip application manifest file specification validation
            - Final Cleanup: When all resources have been synchronized and are in a healthy state, the non-existing resources will be deleted
            - Apply only unsynced: apply only unsynced resources
            - Dependency Cleanup Strategy: Select a specific cleanup strategy:
                - foreground: After deleting all dependent objects, delete the owner object
                - background: delete the owner object first, and then delete all dependent objects
                - orphan: After deleting the owner object, all dependent objects still exist
            - Replace resources: whether to replace existing resources
            - Synchronous retries: parameterize application synchronous retries, support setting the maximum number of retries, retry duration, maximum retry duration, factor

    <!--![]()screenshots-->

## View application

1. After the creation is successful, click the application name to enter the details page, where you can view the application details.

    <!--![]()screenshots-->

1. Since the synchronization method is "Manual Synchronization", we need to manually synchronize, click "Synchronization".

    <!--![]()screenshots-->

1. Please refer to [Manual Synchronization Application](./sync-manually.md) for specific parameter descriptions during the synchronization process, and click __OK__ .

    <!--![]()screenshots-->

1. After the synchronization is successful, check the synchronization result.