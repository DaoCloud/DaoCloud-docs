---
hide:
  - toc
---

# 创建 Elasticsearch 实例

在 Elasticsearch 实例列表中，执行以下操作创建一个新的实例。

1. 在右上角点击`新建实例`。

    ![新建实例](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/elasticsearch/images/create01.png)

2. 填写实例名称和部署位置。通过`安装环境检测`后，点击`下一步`。

    > 如未通过安装环境检测，页面会给出失败原因和操作建议。常见原因是缺少相关组件，根据页面提示安装对应的组件即可。

    ![基本信息](../images/create02.png)

3. 选择一个版本，配置实例的以下规格后，点击`下一步`。可以视情况选择启用/禁用数据节点、Kibana 节点、专用主节点和冷数据节点。

    ![规格配置](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/elasticsearch/images/create03.png)
  
    - 默认启用热数据节点，用于存放 Elasticsearch 搜索服务的日常活跃数据，默认 3 个副本，最少 1 个，最多 50 个。

        ![热数据节点](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/elasticsearch/images/create03-1.png)

    - 默认启用 Kibana 节点，用于存放 Elasticsearch 可视化数据的节点，默认为 1 个 Kibana 节点，不可增加或减少。

        ![Kibana 节点](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/elasticsearch/images/create03-2.png)

    - 可选的专用主节点。这是为了一些专用目的而设定的节点，默认 3 个专用主节点，不可增加和减少。

        ![专用主节点](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/elasticsearch/images/create03-3.png)

    - 可选的冷数据节点。这是存放一些 Elasticsearch 历史数据的节点，默认 3 个冷数据节点，最少 2 个，最多 50 个。

        ![冷数据节点](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/elasticsearch/images/create03-4.png)

4. 设置访问类型（ClusterIP 或 NodePort）、用户名和密码后，点击`下一步`。

    ![服务设置](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/elasticsearch/images/create04.png)

5. 确认上述基本信息、规格配置和服务设置无误后，点击`确认`。

    ![配置确认](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/elasticsearch/images/create05.png)

6. 屏幕提示`创建实例成功`。

    ![创建成功](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/elasticsearch/images/create06.png)
