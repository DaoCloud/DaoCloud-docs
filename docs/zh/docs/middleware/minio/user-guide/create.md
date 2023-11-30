---
hide:
  - toc
---

# 创建 MinIO 实例

1. 从左侧导航栏选择 `Minio 存储`。

    ![选择 minio 存储](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/create01.png)

2. 可以点击列表右上角的`新建实例`按钮。

    > 如果是首次使用，需要[先选择工作空间](../../common/index.md)，然后点击`立即部署`创建 MinIO 实例。

    ![点击新建实例](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/create02.png)

3. 参考下方信息填写实例基本信息，然后点击`下一步`。

    !!! note

        - 实例名称、所在集群/命名空间在实例创建之后不可修改
        - 注意查看输入框下方的填写要求，输入符合要求的内容
        - 如未通过安装环境检测，需要根据提示安装组件之后方可进行下一步

    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/minio/images/create03.png)

4. 参考下方信息填写配置规格，然后点击`下一步`。

    - 部署模式在实例创建之后不可更改
    - 生产模式下建议采用高可用部署模式
    - 高可用模式下需要至少 4 个副本
    - 存储类：所选的存储类应有足够的可用资源，否则会因资源不足导致实例创建失败
    - 存储容量：每个磁盘具有多少容量。**实例创建之后不可调低**
    - 每副本磁盘数：为每个副本提供多少个次盘。**实例创建之后不可调低**

        ![配置规格](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/create07.png)

5. 参考下方信息填写服务设置，点击`下一步`。

    - 集群内访问：只能在同一集群内部访问服务
    - 节点端口：通过节点的 IP 和静态端口访问服务，支持从集群外部访问服务
    - 负载均衡器：使用云服务提供商的负载均衡器使得服务可以公开访问
    - 负载均衡器/外部流量策略：规定服务将外部流量路由到节点本地还是集群范围内的断点

        - Cluster：流量可以转发到集群中其他节点上的 Pod
        - Local：流量只能转发到本节点上的 Pod

    - 控制台账号：访问此新建实例时需要用到的用户名、密码
        
        ![访问模式](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/create08.png)

    ??? note "点击查看高级配置说明"

        - Bucket 名称：在此实例下新建一个存储桶，设置新建存储桶的名称
        - 调度策略/条件：设置 Pod 调度的节点亲和性，可参考 Kubernetes 官方文档[节点亲和性](https://kubernetes.io/zh-cn/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)

            - 尽量满足：先尝试调度到满足规则的节点。如果找不到匹配的节点，也会执行 Pod 调度
            - 必须满足：只有找到满足规则的节点时才执行 Pod 调度

        - 调度策略/权重：为满足每条调度策略的节点设置权重，优选使用权重高的策略。取值范围 1 到 100
        - 调度策略/选择器

            - In：节点必须包含所选的标签，并且该标签的取值必须 **属于** 某个取值集合。多个值用 `；` 隔开
            - NotIn：节点必须包含所选的标签，并且该标签的取值必须 **不属于** 某个取值集合。多个值用 `；` 隔开
            - Exists：节点包含某个标签即可，不关注标签的具体取值
            - DoesNotExists：节点不包含某个标签，不关注标签的具体取值
            - Gt：节点必须包含某个标签，并且标签的取值必须大于某个整数
            - Lt：节点必须包含某个标签，并且标签的取值必须小于某个整数

                ![访问模式](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/create09.png)

6. 确认实例配置信息无误，点击`确认`完成创建。

    ![点击确认](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/minio/images/create05.png)

7. 返回实例列表页查看实例是否创建成功。

    > 创建中的实例状态为`未就绪`，等所有相关容器成功启动之后状态变为`运行中`。

    ![状态](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/minio/images/create06.png)
