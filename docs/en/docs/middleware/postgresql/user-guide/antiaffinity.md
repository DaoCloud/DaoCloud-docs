# Manually Setting Workload Antiaffinity

The antiaffinity policy of the PostgreSQL middleware is shared across all instances within the same cluster. Therefore, we have enabled the __Preferred__ antiaffinity by default. If you need to disable the antiaffinity policy or enable the __Required__ antiaffinity, you will need to modify the settings of the operator.

!!! note

    Modifying the antiaffinity setting of PostgreSQL will affect all instances within the cluster. Proceed with caution.

## Steps

1. Go to __Container Management__ -> __Cluster List__ and select the cluster where the instance resides.

2. Click __Custom Resources__ and search for the resource: __operatorconfigurations.acid.zalan.do__ 


3. Under that resource, select the correct __Namespace__ and __CR Instance__ .


4. Click __Edit YAML__ and modify the following fields according to your needs:


    | Field                                          | Description                                           |
    | ---------------------------------------------- | ----------------------------------------------------- |
    | enable_pod_antiaffinity                        | true: Enable workload antiaffinity<br>false: Disable workload antiaffinity            |
    | pod_antiaffinity_preferred_during_scheduling    | true: Preferred soft antiaffinity<br>false: Required strict antiaffinity |

5. Restart the operator. The existing instances will be recreated and the new scheduling configuration will be applied.

