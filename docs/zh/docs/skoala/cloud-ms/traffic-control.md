# 服务治理

开始治理云原生微服务之前，首先需要将导入服务。
目前仅支持 [DCE 5.0 服务网格](../../mspider/intro/index.md)模块中网格下的服务导入。

## 导入服务

支持

1. 进入 __微服务引擎__ 模块，在左侧点击 __云原生微服务__ -> __服务治理__ ，然后在右上角点击 __手工导入__ 。

    ![手工导入](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/cloudms-import01.png)

2. 筛选目标服务所在的服务网格和命名空间，勾选该服务，然后点击 __确定__ 即可。

    ![确定](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/cloudms-import02.png)

## 查看服务

查看已经导入的所有云原生微服务，点击服务名称进一步查看服务暴露的端口和协议。

![查看](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/cloudms-import03.png)

## 移除服务

在右侧操作栏移除不需要的微服务。

![移除](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/cloudms-import04.png)

服务治理指基于 Service Mesh 对 [DCE 5.0 服务网格](../../mspider/intro/index.md)中的服务进行东西向流量治理。

将网格服务导入云原生微服务引擎之后，就可以针对服务暴露的不同端口设置不同的东西向流量策略。

1. 点击服务名称

    ![点击某个名称](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/cloudms-traffic01.png)

2. 进入治理能力页面

    ![治理能力](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/cloudms-traffic02.png)

3. 根据需要在端口上创建规则，最后点击 __确定__ 

<!--关于各个策略的具体说明，待后续补充-->
