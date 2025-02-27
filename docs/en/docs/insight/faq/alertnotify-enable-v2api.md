# Enabling Insight Alert Notifications (v1alpha2)

Insight introduces a new templating system that adjusts the data structure used for rendering. This creates compatibility issues with the previous version (v1alpha1).  
To prevent conflicts, the new system is disabled by default, and users must enable it manually.  

⚠ **Important:** Once enabled, you must immediately migrate templates to the v1alpha2 syntax. Otherwise, alerts will fail with the error:  
*"Saved original message template cannot send alert notifications properly."*  
(**Operations Tip:** Always back up old template data before making changes.)

This document covers:

- [Enabling the new template system](#enabling-v1alpha2)
- [Migrating to the new template syntax](#template-migration)

## Enabling v1alpha2

### Method 1: (Recommended) Upgrade via Helm

1. Add the following parameter when running a Helm upgrade:

    ```shell
    --set server.alerting.notifyTemplate.version="v1alpha2"
    ```

2. Alternatively, edit the `values.yaml` file:

    ```diff
    server:
      alerting:
        notifyTemplate:
    -     version: v1alpha1
    +     version: v1alpha2
    ```

### Method 2: Temporarily Modify the ConfigMap

1. Edit the Insight server configuration file (`configmap`) named `insight-server-config`, updating the following setting:

    ```diff
    alerting:
      notifyTemplate:
    -   version: v1alpha1
    +   version: v1alpha2
    ```

2. Save the changes and restart the `insight-server`.

## Template Migration

The primary reason for migration is that the data structure has changed from `AmAlert` to `AMHookRequest`.  
The new template system provides richer information and allows for better alert rendering.

### Data Structure Comparison

#### New Structure (v1alpha2)

```go
type AMHookRequest struct {
	Version           string            `json:"version,omitempty"`
	GroupKey          string            `json:"groupKey,omitempty"`
	Status            string            `json:"status,omitempty"`
	Receiver          string            `json:"receiver,omitempty"`
	GroupLabels       map[string]string `json:"groupLabels,omitempty"`
	CommonLabels      map[string]string `json:"commonLabels,omitempty"`
	CommonAnnotations map[string]string `json:"commonAnnotations,omitempty"`
	ExternalURL       string            `json:"externalURL,omitempty"`
	Alerts            []*AmAlert        `json:"alerts,omitempty"`
	TruncatedAlerts   int64             `json:"truncatedAlerts,omitempty"`
}
```

#### Old Structure (v1alpha1)

```go
type AmAlert struct {
	Status       string            `json:"status,omitempty"`
	Labels       map[string]string `json:"labels,omitempty"`
	Annotations  map[string]string `json:"annotations,omitempty"`
	StartsAt     string            `json:"startsAt,omitempty"`
	EndsAt       string            `json:"endsAt,omitempty"`
	GeneratorURL string            `json:"generatorURL,omitempty"`
	Fingerprint  string            `json:"fingerprint,omitempty"`
}
```

The key difference is that in v1alpha2, `AmAlert` now resides inside the `Alerts` field.  
The new structure also introduces **CommonLabels** and **CommonAnnotations**, which provide more useful metadata.

## Example: Email Notification Template Migration

For an email alert template, here’s the **before-and-after** difference:

### New Template (v1alpha2)

- The new template uses `{{range .Alerts}}` to iterate over multiple alerts.
- Both the **email subject** and **body** now use the same data structure, reducing complexity.

```diff
+<b style="font-weight: bold">[{{ .Alerts | len -}}] {{.Status}}</b><br />
+{{range .Alerts}}
ruleName: {{ .Labels.alertname }} <br />
groupName: {{ .Labels.alertgroup }} <br />
severity: {{ .Labels.severity }} <br />
cluster: {{ .Labels.cluster | toClusterName }} <br />
{{if .Labels.namespace }} namespace: {{ .Labels.namespace }} <br /> {{ end }}
{{if .Labels.node }} node: {{ .Labels.node }} <br /> {{ end }}
targetType: {{ .Labels.target_type }} <br />
{{if .Labels.target }} target: {{ .Labels.target }} <br /> {{ end }}
value: {{ .Annotations.value }} <br />
startsAt: {{ .StartsAt }} <br />
{{if ne "0001-01-01T00:00:00Z" .EndsAt }} EndsAt: {{ .EndsAt }} <br /> {{ end }}
description: {{ .Annotations.description }} <br />
+<br />
+{{end}}
```

### Old Template (v1alpha1)

```
[{{ .status }}] [{{ .severity }}] alert: {{ .alertname }}
```

### Updated Syntax in v1alpha2

In the new template, severity and alert names now come from **CommonLabels**, which preserves their original values without additional processing.

```
[{{ .Status }}] [{{ .CommonLabels.severity }}] alert: {{ .CommonLabels.alertname }}
```

## More Examples

### Feishu, DingTalk, and WeChat Notification Templates

```diff
+[{{ .Alerts | len -}}] {{.Status}}
+{{range .Alerts}}
Rule Name:   {{ .Labels.alertname }}
Group Name:  {{ .Labels.alertgroup }}
Severity:    {{ .Labels.severity }}
Cluster:     {{ .Labels.cluster | toClusterName }}
{{if .Labels.namespace }}Namespace:  {{ .Labels.namespace }}
{{ end }}{{if .Labels.node }}Node:  {{ .Labels.node }}
{{ end }}Target Type: {{ .Labels.target_type }}
{{if .Labels.target }}Target:  {{ .Labels.target }} 
{{ end }}Value:       {{ .Annotations.value }}
Starts At:   {{ .StartsAt }}
{{if ne "0001-01-01T00:00:00Z" .EndsAt }}Ends At:     {{ .EndsAt }}
{{ end }}Description: {{ .Annotations.description }}
+{{end}}
```
