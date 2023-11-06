# Manually Setting Workload Antiaffinity

The antiaffinity policy of the PostgreSQL middleware is shared across all instances within the same cluster. Therefore, we have enabled the `Preferred` antiaffinity by default. If you need to disable the antiaffinity policy or enable the `Required` antiaffinity, you will need to modify the settings of the operator.

!!! note

    Modifying the antiaffinity setting of PostgreSQL will affect all instances within the cluster. Proceed with caution.

## Steps

1. Go to `Container Management` -> `Cluster List` and select the cluster where the instance resides.

2. Click `Custom Resources` and search for the resource: `operatorconfigurations.acid.zalan.do`


3. Under that resource, select the correct `Namespace` and `CR Instance`.


4. Click `Edit YAML` and modify the following fields according to your needs:


    | Field                                          | Description                                           |
    | ---------------------------------------------- | ----------------------------------------------------- |
    | enable_pod_antiaffinity                        | true: Enable workload antiaffinity<br>false: Disable workload antiaffinity            |
    | pod_antiaffinity_preferred_during_scheduling    | true: Preferred soft antiaffinity<br>false: Required strict antiaffinity |

5. Restart the operator. The existing instances will be recreated and the new scheduling configuration will be applied.

