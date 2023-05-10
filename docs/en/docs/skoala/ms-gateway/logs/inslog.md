# instance log

The microservice gateway supports viewing request logs and instance logs. This page describes how to view instance logs and related operations when viewing logs.

## view mode

Click the name of the target gateway to enter the gateway overview page, and then click `Log View`->`Instance Log` in the left navigation bar.

<!--Update screenshot-->

## Related operations

- Filtering logs: support filtering instances to view only the logs of a certain pod, or refer to [KQL syntax](https://www.elastic.co/guide/en/kibana/current/kuery-query.html) to enter directly Keywords to find specific content.

- Limited time range: The log time range can be selected: logs of the last 5 minutes, logs of the last 1 hour, logs of the last 12 hours, logs of the last 7 days, or a custom time range.

- Auto Refresh: When viewing logs, turn on `Auto Refresh` to view real-time logs.

<!--Supplementary Screenshot-->

!!! info

    If you want to view more logs or download logs, you can go to [Observability Module](../../../insight/intro/WhatisInsight.md) through [Log Query](../../.. /insight/06UserGuide/04dataquery/logquery.md) function to query or download logs of a specific cluster, namespace, workload, or pod.