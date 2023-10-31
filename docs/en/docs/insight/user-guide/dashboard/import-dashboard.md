# Importing Custom Dashboards

By using Grafana CRD, you can incorporate the management and deployment of dashboards into the lifecycle management of Kubernetes. This enables version control, automated deployment, and cluster-level management of dashboards. This page describes how to import custom dashboards using CRD and the UI interface.

## Steps

1. Log in to the DCE 5.0 platform and go to `Container Management`. Select the `kpanda-global-cluster` from the cluster list.

2. Choose `Custom Resources` from the left navigation pane. Look for the `grafanadashboards.integreatly.org`
   file in the list and click on it to view the details.

3. Click on `YAML Create` and use the following template. Replace the dashboard JSON in the `Json` field.

    - `namespace`: Specify the target namespace.
    - `name`: Provide a name for the dashboard.
    - `label`: Mandatory. Set the label as `operator.insight.io/managed-by: insight`.

    ```yaml
    apiVersion: integreatly.org/v1alpha1
    kind: GrafanaDashboard
    metadata:
      labels:
        app: insight-grafana-operator
        operator.insight.io/managed-by: insight
      name: sample-dashboard
      namespace: insight-system
    spec:
      json: >
        {
          "id": null,
          "title": "Simple Dashboard",
          "tags": [],
          "style": "dark",
          "timezone": "browser",
          "editable": true,
          "hideControls": false,
          "graphTooltip": 1,
          "panels": [],
          "time": {
            "from": "now-6h",
            "to": "now"
          },
          "timepicker": {
            "time_options": [],
            "refresh_intervals": []
          },
          "templating": {
            "list": []
          },
          "annotations": {
            "list": []
          },
          "refresh": "5s",
          "schemaVersion": 17,
          "version": 0,
          "links": []
        }
    ```

4. After clicking `Confirm`, wait for a while to view the newly imported dashboard in `Dashboard`.

!!! info

    If you need to customize the dashboard, refer to
    [Add Dashboard Panel](https://grafana.com/docs/grafana/latest/dashboards/add-organize-panels/).
