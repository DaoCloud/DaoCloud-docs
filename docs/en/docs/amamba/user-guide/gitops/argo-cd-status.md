# Argo CD application status description

This page introduces the health status and synchronization status description of the Argo CD application.

**Health status**

| Health Status | Description |
| -------- | ---------------- |
| Health | Resource Health |
| Degraded | Resource has been demoted |
| In progress | Resource is not yet healthy, but still in progress and may be healthy soon |
| Suspended | The resource is suspended and waits for some external event to resume (such as a suspended CronJob or a suspended deployment) |
| Unknown | Unable to judge current health status |
| Missing | Resource is missing |
| | |

**Sync Status**

| Sync Status | Description |
| -------- | -------------- |
| Synchronized | The resources deployed in the cluster are consistent with the expected state in the warehouse |
| not synchronized | resources deployed in the cluster are inconsistent with the expected state in the warehouse |
| Unknown | Unable to determine the current synchronization status |
