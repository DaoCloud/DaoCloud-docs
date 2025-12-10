# Insight Grafana 持久化到数据库

Insight 使用云原生的 `GrafanaOperator` + `CRD` 的方式来使用 Grafana。我们推荐使用 GrafanaDashboard(CRD) 
来描述仪表盘的 JSON 数据，即通过 `GrafanaDashboard` 来增加、删除、修改仪表盘。

因为 Grafana 默认使用 SQLite3 作为本地数据库来存储配置信息，例如用户、仪表盘、告警等。
当用户以 管理员身份，通过 UI 创建或者导入仪表盘之后，数据将临时存储在 SQLite3 中。
当 Grafana 重启之后，将重置所有的仪表盘的数据，将只展示通过 GrafanaDashboard CR 描述的仪表盘数据，而通过 UI 创建，删除，修改也都将被全部重置。

Grafana 支持使用外部的 MySQL、PostgreSQL 等数据库替代内置的 SQLite3 作为内部存储。本文描述了如果给 Insight 提供的 Grafana 配置外置的数据库。

## 使用外部数据库

结合 Grafana（当前镜像版本 12.1.3）的官方文档。根据如下步骤配置使用外部的数据库，示例以 MySQL 为例：

1. 在外部数据库（MySQL /PostgreSQL）中创建一个数据库（DB）。
2. 配置 Grafana 使用这个数据库（MySQL 的 MGR 模式需要额外处理）。

## 操作步骤

### 方法一

1. 初始化数据库

    在数据库中创建一个新的 database 给 Grafana 使用，建议名称为 grafana

2. 修改过 Grafana CR

    在 `insight-system` 下，名为 grafana 的 Grafana 的 CR 里的配置：

    ```diff
    apiVersion: grafana.integreatly.org/v1beta1
    kind: Grafana
    metadata:
      name: grafana
      namespace: insight-system
    spec:
      config:
        # 在 config 的尾部追加
    +   database:
    +     type: mysql # 支持 mysql, postgres
    +     host: "10.6.216.101:30782" # 数据库的 Endpoint
    +     name: "grafana"  # 提前创建的 database
    +     user: "grafana"
    +     password: "grafana_password"
    ```

3. 等待 grafana operator 重新调协资源完成后 Grafana 的配置文件 `grafana-ini` 会新增 database 配置信息：

    ```toml
    [database]
      host = 10.6.216.101:30782
      name = grafana
      password = grafana_password
      type = mysql
      user = grafana
    ```

### 方式二

1. 初始化数据库

    在数据库中创建一个新的 database 给 Grafana 使用，建议名称为 grafana

2. 获取当前 insight release values

    ```shell
    helm get values insight -n insight-system -o yaml > insight.yaml
    ```

3. 指定原来配置文件并添加 grafana 数据库的连接信息

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

通过 helm 命令开启 db 后，在升级后续 insight chart 版本时会遇到 admin 用户无法登录问题，具体解决办法请查看 **注意事项 3**

## 注意事项

1. 用户是否会覆盖内置仪表盘，导致升级失败？

    回复：会。当用户编辑了 Dashbaord A（v1.1），且 Insight 也升级了 Dashboard A（v2.0），
    升级之后（升级镜像）；用户看到内容还是 v1.1，而 v2.0 是不会更新到环境里。

2. 当使用 MGR 模式 MySQL 时会存在问题，导致 grafana-deployment 无法正常启动。

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

3. 在开启 Grafana 持久化数据库后升级 insight 会导致升级后的 grafana admin 用户无法登录，dashboard 创建失败等权限问题。

    原因：在 insight 升级后 `grafana-admin-credentials` Secret 中 admin 密码被更新，但是数据库 `grafana.user` 表中 admin 用户的密码是初始化
    数据库时写入的密码，导致 admin 密码冲突，鉴权失败。

    解决方法：这个问题有两个解决方法：

    方式一：固定 grafana admin 密码

    升级 insight 前，在 insight.yaml 添加如下配置，以固定 grafana 密码：

    ```diff
     grafana-operator:
       grafana:
         config:
           security:
             admin_user: admin
    +        admin_password: F4R1an5D2oPMRg==
    ```
   
    方式二：将最新的 admin 密码更新到数据库

    在 https://go.dev/play 中根据注释运行代码并在数据库中执行生成的 SQL, 最后重启 grafana pod：

    ```go
    package main

    import (
      "fmt"

      "github.com/grafana/grafana/pkg/util"
    )

    func main() {
      sql := "UPDATE grafana.`user` SET password = '%s' WHERE login = 'admin';" // SQL update template
      salt := "JjTJT3vlVE"                                                      // Retrieve the salt via SQL query: SELECT salt FROM grafana.`user` WHERE login = 'admin';
      password := "yR1IQmNqHKjchw=="                                            // The value of GF_SECURITY_ADMIN_PASSWORD in the grafana-admin-credentials secret under the insight-system namespace
      encodeStr := util.EncodePassword(password, salt)
      fmt.Println(fmt.Sprintf(sql, encodeStr))                                  // Execute the output command in the database
      // Example output: UPDATE grafana.`user` SET password = '243c6eecaebe959d33f8f96563c6ada760efb6a2da8e46699550a8d33f28ab3a0317cb8abc3a392accea6229f6dd535173ff' WHERE login = 'admin';
    }
    ```