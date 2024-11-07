# Insight Grafana 持久化到数据库

Insight 使用云原生的 `GrafanaOperator` + `CRD` 的方式来使用 Grafana。我们推荐使用 GrafanaDashboard(CRD) 
来描述仪表盘的 JSON 数据，即通过 `GrafanaDashboard` 来增加、删除、修改仪表盘。

因为 Grafana 默认使用 SQLite3 作为本地数据库来存储配置信息，例如用户、仪表盘、告警等。
当用户以 管理员身份，通过 UI 创建或者导入仪表盘之后，数据将临时存储在 SQLite3 中。
当 Grafana 重启之后，将重置所有的仪表盘的数据，将只展示通过 GrafanaDashboard CR 描述的仪表盘数据，而通过 UI 创建，删除，修改也都将被全部重置。

Grafana 支持使用外部的 MySQL、PostgreSQL 等数据库替代内置的 SQLite3 作为内部存储。本文描述了如果给 Insight 提供的 Grafana 配置外置的数据库。

## 使用外部数据库

结合 Grafana（当前镜像版本 9.3.14）的官方文档。根据如下步骤配置使用外部的数据库，示例以 MySQL 为例：

1. 在外部数据库（MySQL /PostgreSQL）中创建一个数据库（DB）。
2. 配置 Grafana 使用这个数据库（MySQL 的 MGR 模式需要额外处理）。

## 操作步骤

1. 初始化数据库

    在数据库中创建一个新的 database 给 Grafana 使用，建议名称为 grafana

1. 配置 Grafana 使用 DB

    在 `insight-system` 下，名为 insight-grafana-operator-grafana 的 Grafana 的 CR 里的配置：

    ```yaml
    apiVersion: integreatly.org/v1alpha1
    kind: Grafana
    metadata:
      name: insight-grafana-operator-grafana
      namespace: insight-system
    spec:
      baseImage: 10.64.40.50/docker.m.daocloud.io/grafana/grafana:9.3.14
      config:
        // 在 config 的尾部追加
    +   database:
    +     type: mysql # 支持 mysql, postgres
    +     host: "10.6.216.101:30782" # 数据库的 Endpoint
    +     name: "grafana"  # 提前创建的 database
    +     user: "grafana"
    +     password: "grafana_password"
    ```

1. 如下是配置完成后在 Grafana 的配置文件 grafana-config 里的配置信息。

    ```toml
    [database]
      host = 10.6.216.101:30782
      name = grafana
      password = grafana_password
      type = mysql
      user = grafana
    ```

    1. 在 insight.yaml 添加如下配置：

        ```yaml
        grafana-operator:
          grafana:
            config:
              database:
                type: mysql
                host: "10.6.216.101:30782"
                name: "grafana"
                user: "grafana"
                password: "grafana_password"
        ```

    1. 升级 insight server，建议通过 Helm 升级。

        ```shell
        helm upgrade insight insight/insight \
          -n insight-system \
          -f ./insight.yaml \
          --version ${version}
        ```

1. 通过命令行进行升级。

    1. 获取 insight Helm 中原来的配置。

        ```shell
        helm get values insight -n insight-system -o yaml > insight.yaml
        ```

    1. 指定原来配置文件并保存 grafana 数据库的连接信息。

        ```shell
        helm upgrade --install \
            --version ${version} \
            insight insight/insight -n insight-system \
            -f ./insight.yaml \
            --set grafana-operator.grafana.config.database.type=mysql \
            --set grafana-operator.grafana.config.database.host=10.6.216.101:30782 \
            --set grafana-operator.grafana.config.database.name=grafana \
            --set grafana-operator.grafana.config.database.user=grafana \
            --set grafana-operator.grafana.config.database.password=grafana_password 
        ```

## 注意事项

1. 用户是否会覆盖内置仪表盘，导致升级失败？

    回复：会。当用户编辑了 Dashbaord A（v1.1），且 Insight 也升级了 Dashboard A（v2.0），
    升级之后（升级镜像）；用户看到内容还是 v1.1，而 v2.0 是不会更新到环境里。

1. 当使用 MGR 模式 MySQL 时会存在问题，导致 grafana-deployment 无法正常启动。

    原因：表 alert_rule_tag_v1 和 annotation_tag_v2 中没有主键，而 mysql mgr 必须有主键

    解决方法：向 alert_rule_tag_v1 和 annotation_tag_v2 临时表添加主键：

    ```SQL
    alter table alert_rule_tag_v1
        add constraint alert_rule_tag_v1_pk
            primary key (tag_id, alert_id);
        
    alter table annotation_tag_v2
        add constraint annotation_tag_v2_pk
            primary key (tag_id, annotation_id);
    ```
   
