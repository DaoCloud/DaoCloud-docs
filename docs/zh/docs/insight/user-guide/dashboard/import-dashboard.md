# 导入自定义仪表盘

通过使用 Grafana CRD，可以将仪表板的管理和部署纳入到 Kubernetes 的生命周期管理中，实现仪表板的版本控制、自动化部署和集群级的管理。本页介绍如何通过 CRD 和 UI 界面导入自定义的仪表盘。

## 操作步骤

1. 登录 DCE 5.0 平台，进入`容器管理`，在集群列表中选择 `kpanda-global-cluster`。

2. 选择左侧导航栏的`自定义资源`，在列表中查找 `grafanadashboards.integreatly.org` 文件，进入详情。

    ![导入仪表盘](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/importboard00.png)

3. 点击 `Yaml 创建`，使用以下模板，在 `Json` 字段中替换仪表盘 JSON。

    - `namespace`：填写目标命名空间；
    - `name`：填写仪表盘的名称。
    - `label`：必填，`operator.insight.io/managed-by: insight`。

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

4. 点击`确认`后，稍等片刻即可在`仪表盘`中查看刚刚导入的仪表盘。

!!! info

    自定义设计仪表盘，请参考[添加仪表盘面板](https://grafana.com/docs/grafana/latest/dashboards/add-organize-panels/)。
