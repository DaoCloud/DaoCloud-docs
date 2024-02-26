# MySQL Operator

## Unspecified __storageClass__ 

When the __storageClass__ is not specified, it causes the __mysql-operator__ to be unable to retrieve the Persistent Volume Claim (PVC), resulting in a __pending__ state.

If you are using Helm to deploy, you can make the following configuration:

1. Disable PVC provisioning:

    ```console
    orchestrator.persistence.enabled=false 
    ```

2. Specify the __storageClass__ to retrieve the PVC:

    ```console
    orchestrator.persistence.storageClass={storageClassName} 
    ```

If you are using a different tool, you can modify the corresponding field in the __value.yaml__ file to achieve the same effect as deploying with Helm.
