---
hide:
  - toc
---

# 创建授权规则

授权规则开业根据资源的请求来源限制资源是否通过。若配置白名单，则只有请求来源位于白名单内时才可通过；若配置黑名单，则请求来源位于黑名单时不通过，其余的请求通过。

创建流控规则的方式如下：

1. 点击目标托管注册中心的名称，然后在左侧导航栏点击 __微服务列表__ ，在最右侧点击更多按钮选择 __治理__ 。

    > 注意需要治理的微服务在 __是否可以治理__ 一栏应该显示为`是`，才能进行后续步骤。

    ![微服务列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gov00.png)

2. 选择 __授权规则__ ，然后在右侧点击 __创建授权规则__ 。

    ![微服务列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gov08.png)

3. 参考下列说明填写规则配置，并在右下角点击 __确定__ 。

    - 资源名：需要控制哪个资源的流量就填写哪个资源的名称，例如当前服务下的某个 API 接口、函数、变量等。
    - 流控应用：资源的请求来源，请求来源用 `,` 分隔，如 `appA,appB`
    - 授权类型——白名单：只有请求来源位于白名单内时才允许访问该资源。
    - 授权类型——黑名单：如果请求来源位于黑名单时，不允许其访问该资源。对于不在黑名单上的请求来源，不做限制。

        ![微服务列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gov09.png)

4. 创建完成后可以在授权规则列表中查看新建的规则。在右侧点击更多按钮可以更新规则或者删除该规则。

    ![流控规则列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gov10.png)
