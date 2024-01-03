# Importing Custom Dashboards

By using Grafana CRD, you can incorporate the management and deployment of dashboards into the lifecycle management of Kubernetes. This enables version control, automated deployment, and cluster-level management of dashboards. This page describes how to import custom dashboards using CRD and the UI interface.

## Steps

1. Log in to the DCE 5.0 platform and go to __Container Management__ . Select the __kpanda-global-cluster__ from the cluster list.

2. Choose __Custom Resources__ from the left navigation pane. Look for the __grafanadashboards.integreatly.org__ 
   file in the list and click it to view the details.

3. Click __YAML Create__ and use the following template. Replace the dashboard JSON in the __Json__ field.

    - __namespace__ : Specify the target namespace.
    - __name__ : Provide a name for the dashboard.
    - __label__ : Mandatory. Set the label as __operator.insight.io/managed-by: insight__ .

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

4. After clicking __OK__ , wait for a while to view the newly imported dashboard in __Dashboard__ .

!!! info

    If you need to customize the dashboard, refer to
    [Add Dashboard Panel](https://grafana.com/docs/grafana/latest/dashboards/add-organize-panels/).
