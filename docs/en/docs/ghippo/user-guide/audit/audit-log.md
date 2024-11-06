---
MTPE: WANG0608GitHub
Date: 2024-08-26
---

# Audit log

Audit logs help you monitor and record the activities of each user, and provide features for
collecting, storing and querying security-related records arranged in chronological order. With the
audit log service, you can continuously monitor and retain user behaviors in the Global Management
module, including but not limited to user creation, user login/logout, user authorization, and user
operations related to Kubernetes.

## Features

The audit log feature has the following characteristics:

- Out of the box: When installing and using the platform, the audit log feature will be enabled
  by default, automatically recording various user-related actions, such as creating users, authorization,
  and login/logout. By default, 365 days of user behavior can be viewed within the platform.

- Security analysis: The audit log will record user operations in detail and provide an export function.
  Through these events, you can judge whether the account is at risk.

- Real-time recording: Quickly collect operation events, and trace back in the audit log list after user operations, so that suspicious behavior can be found at any time.

- Convenient and reliable: The audit log supports manual cleaning and automatic cleaning, and the cleaning policy can be configured according to your storage size.

## View Audit Logs

1. Log in to DCE 5.0 with a user account that has the __admin__ or __Audit Owner__ role.

    ![Log in to DCE 5.0](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/lang00.png)

2. At the bottom of the left navigation bar, click __Global Management__ -> __Audit Logs__ .

    ![Audit Logs](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/audit01.png)

## User operations

On the __User operations__ tab, you can search for user operation events by time range, or by using fuzzy or exact search.

Click the __┇__ icon on the right side of an event to view its details.

![User audit logs](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/audit02.png)

The event details are shown in the following figure.

![User event details](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/audit03.png)

Click the __Export__ in the upper right corner to export the user operation logs within the selected time range in CSV or Excel format.

![Export](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/audit04.png)

## System operations

On the __System operations__ tab, you can search for system operation events by time range, or by using fuzzy or exact search.

Similarly, click the __┇__ icon on the right side of an event to view its details.

![System event details](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/audit05.png)

Click the __Export__ in the upper right corner to export the system operation logs within the selected time range in CSV or Excel format.

![Export](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/audit06.png)

## Settings

On the __Settings__ tab, you can clean up audit logs for user operations and system operations.

![Clean up](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/audit07.png)

You can manually clean up the logs, but it is recommended to export and save them before cleaning. You can also set the maximum retention time for the logs to automatically clean them up.

!!! note

    The audit logs related to Kubernetes in the auditing module are provided by the Insight module.
    To reduce the storage pressure of the audit logs, Global Management by default does not collect Kubernetes-related logs.
    If you need to record them, please refer to [Enabling K8s Audit Logs](./open-k8s-audit.md).
    Once enabled, the cleanup function is consistent with the Global Management cleanup function,
    but they do not affect each other.
