# Security Audit Logs

Security Audit Logs let you query gateway security policy trigger records. Platform operators can trace blocks, alerts, and content replacements, and export results based on the current filters.

Use this page together with [Security Policy Management](./security-policy.md). The capability depends on Higress integrated with the Knoway gateway (LLM Studio **v0.15.0** or later). For how to enable Higress, see [Upgrade Notes](../intro/upgrade-notes.md).

## Prerequisites

- The current user has platform administrator permissions and can access the **Admin Console**.
- Related worker clusters have Higress enabled and at least one security policy configured.
- Audit data collection is healthy. If no records appear for a long time, confirm that policies are enabled and that the gateway and logging components are ready.

## Entry Point

1. Sign in to the platform and open the **Admin Console**.
2. In the left navigation, choose **Security** → **Security Audit Logs**.

![Security audit logs](images/security-audit-logs.png)

## Filters

You can filter logs with the following conditions. The default time range is the last **24 hours**:

| Filter | Description |
| ------ | ----------- |
| Cluster | Select a worker cluster, or choose **All clusters** |
| Alert Level | **All Levels** / **High** / **Medium** / **Low** |
| Time Range | Start and end time; also required for export |
| Search | Search by **route name**, **operation**, or **policy type** |

**Operation** corresponds to the action taken after a policy match (for example, Block Request, Log, Random Replace, or Mask Replace). **Policy type** corresponds to the enabled security policy types.

## List Fields

Audit logs are shown in a table. The main fields are:

| Field | Description |
| ----- | ----------- |
| Cluster | Worker cluster where the event occurred |
| Route | Matched gateway route |
| Alert Level | High / Medium / Low |
| Operation | Action taken for this trigger |
| Reason | Why the policy was triggered |
| Policy Type | Matched policy type, such as Regex Match or Sensitive Word |
| Match Rule | The concrete rule that matched |
| Content Source | Whether the matched content came from the request, response, or another source |
| Deny Message | Related information returned when the request was blocked or denied |
| Operation Time | When the event occurred |

!!! note

    The UI shows audit records in a list and does not provide a separate detail page. Exported files may include additional fields that are not shown in the table for offline analysis.

## Export Logs

1. Set the filters first (cluster, alert level, time range, and search conditions).
2. Click **Export**.
3. Choose an export format:
    - **CSV**
    - **Excel** (`.xlsx`)

The export uses the current filter conditions.

!!! note

    - Export requires a start and end time, and the time span must not exceed **30 days**.
    - The maximum number of rows per export is limited by the deployment setting `audit_log.max_export_rows`. Use the value configured in your environment.

## Notes

- If the result set is empty, check whether the time range is too narrow, the wrong cluster is selected, the related policy is disabled, or no matches have occurred yet.
- The **Log** action does not block the call, but it writes an audit record that can be queried on this page. It is suitable for validating rules in a gray release.
- These logs focus on gateway security policy events. For platform operation audits, see the audit documentation in Global Management.
