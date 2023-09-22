# MySQL Operator

## Unspecified `storageClass`

When the `storageClass` is not specified, it causes the `mysql-operator` to be unable to retrieve the Persistent Volume Claim (PVC), resulting in a `pending` state.

If you are using Helm to deploy, you can make the following configuration:

1. Disable PVC provisioning:

    ```console
    orchestrator.persistence.enabled=false 
    ```

2. Specify the `storageClass` to retrieve the PVC:

    ```console
    orchestrator.persistence.storageClass={storageClassName} 
    ```

If you are using a different tool, you can modify the corresponding field in the `value.yaml` file to achieve the same effect as deploying with Helm.
