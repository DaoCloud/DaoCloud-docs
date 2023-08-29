# Instance log

The microservice gateway supports viewing request logs and instance logs. This page describes how to view instance logs and how to view logs.

## Viewing mode

Click the name of the target gateway to enter the gateway overview page, and then click `Check Logs` -> `Instance Logs` in the left navigation bar.

<!--![]()screenshots-->

## Related operation

- Filtering logs: support filtering instances to view only the logs of a certain pod, or refer to [KQL syntax](https://www.elastic.co/guide/en/kibana/current/kuery-query.html) to enter directly Keywords to find specific content.

- Time range: The log time range can be set to the latest 5 minutes, the latest 1 hour, the latest 12 hours, or the latest 7 days, or a user-defined time range.

- Automatic refresh: When viewing logs, enable `Auto Refresh` to view real-time logs.

<! -- Add screenshots -->

!!! info

    If you want to view more logs or download logs, you can go to [Observability Module](../../../insight/intro/index.md) through [Log Query](../../../insight/user-guide/data-query/log.md) feature to query or download logs of a specific cluster, namespace, workload, or pod.

