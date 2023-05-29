# 导入自定义仪表盘

本页介绍如何通过 CRD 和 UI 界面导入自定义的仪表盘。

## 通过 CRD 导入仪表盘

1. 登录 DCE 5.0 平台，从左侧导航栏进入`容器管理`，在集群列表中选择目标集群。

2. 选择左侧导航栏的`自定义资源`，在列表中查找 `grafanadashboards.integreatly.org` 文件，进入详情。

    ![导入仪表盘](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/importboard00.png)

3. 点击 `Yaml 创建`，使用以下模板，在 `Json` 字段中替换仪表盘 JSON。

    - `namespace`：填写目标命名空间；
    - `name`：填写仪表盘的名称。

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

## 通过 UI 导入仪表盘

本节说明如何访问原生 Grafana 构建自定义仪表盘。

1. 点击左侧导航栏 `Dashboards` > `Import`。

    ![导入仪表盘](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/importboard01.png)

2. 可选择以下方式导入：

    - 上传仪表盘 JSON 文件
    - 粘贴 [Grafana.com](https://grafana.com)仪表盘 URL
    - 粘贴仪表盘 JSON 到文本区域

    ![导入仪表盘](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/importboard02.png)

3. 点击 `Load` 后，填写以下参数：

    - name：设置仪表盘的名称
    - Floder：选择仪表盘存储的目标路径
    - Prometheus：选择数据源

    ![导入仪表盘](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/importboard03.png)

4. 点击 `Import` 即可成功导入仪表盘。

    ![导入仪表盘](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/importboard04.png)

!!! info

    如果需要自定义仪表盘，请参考[添加仪表盘面板](https://grafana.com/docs/grafana/latest/dashboards/add-organize-panels/)。

!!! warning

    目前无法为自定义的仪表盘提供持久化服务，请在升级或重启 insight 前备份您自定义的仪表盘。
