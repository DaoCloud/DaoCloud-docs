---
hide:
  - toc
---

# 创建托管 Harbor

前提条件：需要先安装好 [Cert Manager](https://cert-manager.io/docs/installation/) 和 [Harbor Operator](./operator.md) 。

!!! note

    对于 Harbor 实例，除了接入管理员账号外，还可以接入机器人账号达到同样的接入效果。

1. 使用具有 Admin 角色的用户登录 DCE 5.0，从左侧导航栏点击`镜像仓库` -> `托管 Harbor`。

    ![镜像仓库](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/hosted01.png)

1. 点击右上角的`创建实例`按钮。

    ![创建实例](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/hosted02.png)

1. 填写实例名称，选择部署位置后点击`下一步`（若无部署位置可选，需先前往容器管理创建集群和命名空间）。

    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/hosted03.png)

1. 填写数据库、Redis 实例和镜像/Charts 存储信息后点击`下一步`（当前只支持接入外部数据库和 Redis 实例）。

    系统会自动检测 PostgreSQL 和 Redis，如果没有可用的数据库，可以点击创建链接进行创建。

    数据库填写提示：

    -  地址：`postgres://{host}:{port}`，例如 `postgres://acid-minimal-cluster.default.svc:5432`
    -  用户名：填写连接数据库的用户名
    -  密码：填写连接数据库的密码

    Redis 填写分为单机和哨兵模式：

    - 单机模式填写地址：`redis://{host}:{port}`，需要替换 host、port 两个参数。
    - 哨兵模式填写地址：`redis+sentinel://{host}:{port}?sentinelMasterId={master_id}`，需要替换 host、port、master_id 三个参数。
    - 密码：按需填写

    ![规格配置](../images/hosted04.png)

1. 填写域名，选择 Ingress 实例，输入管理员密码后点击`确定`（用户名/密码用于登录原生 Harbor 实例，请妥善保管密码）。

    域名填写提示: `http://{host}`，host 前面的 `http://` 必须要带上。

    ![访问与策略绑定](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/hosted05.png)

1. 返回托管 Harbor 实例列表，新创建的实例默认位于第一个，等待状态从`更新中`变为`健康`，即可正常使用。

    ![实例列表](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/hosted06.png)

1. 点击某个实例右侧的 `...`，可以选择编辑、删除或进入原生 Harbor。

    ![更多操作](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/hosted07.png)

下一步：[创建镜像空间](../integrate/registry-space.md)
