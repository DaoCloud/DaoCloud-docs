---
hide:
  - toc
---

# 网格 Istio 版本升级

!!! warning "更新提示"

    更新时尽量不要进行配置等相关变更，请合理安排升级计划。

服务网格支持三种网格类型，其中托管网格与专有网格由 DaoCloud 创建并进行托管，接入网格指接入客户已有的服务网格。

## 一键升级：托管网格与专有网格

DaoCloud 托管的网格类型，支持 Istio 版本可持续升级，DaoCloud 提供了原生版本和定制版本两类升级版本。

- 原生版本：社区原生 Istio，无任何定制化修改。
- 定制版本：基于 Istio 做了部分功能定制（后缀为：-mspider），例如集成
  [Merbridge](../../community/merbridge.md) 提高网格通信性能，支持 SpringCloud、Dubbo 等传统微服务的智能识别，支持边车热升级能力等。

这两类版本升级过程相同，但不支持不同类型的混合升级；所以，在创建网格实例时务必确认所需的版本。

DaoCloud 会持续提供 Istio 新版本适配工作，当系统检测存在新的 Istio 版本时， __网格列表__ 会对可升级的网格实例进行提示（卡片会出现叹号提示图标），查看图标内容并点击 __立即升级__ 按钮即可进入升级向导。

![立即升级](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/IstioUpdate01.png)

Istio 升级向导包含 __选择目标版本__ 、 __环境检测__ 、 __执行升级__ 三步，升级完成后网格即可立即上线运行。具体步骤如下：

1. **选择目标版本**：在列表中选择期望升级的版本，升级后将无法回滚至低版本，建议谨慎选择。

    ![目标版本](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/IstioUpdate02.png)
   
    > 官方是不推荐的 Istio 对跨版本升级，建议按照阶梯升级的方式升级，例如 __1.15.x__ 应该升级到 __1.16.x__ ，
    > 不建议直接升级到大于 __1.16.x__ 的版本。

2. **环境监测**：系统将基于所选的目标版本，检测网格下各集群（k8s）版本是否符合升级要求，如果符合要求，将激活 __下一步__ 按钮，否则，需要用户处理环境问题.

    ![环境检测](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/IstioUpdate03.png)

 	- 如果集群（k8s）版本过低，可以在容器管理平台先升级集群（k8s）版本后，点击 __重新检测__ 按钮；

	- 如果集群（k8s）版本过高，建议回退至“选择目标版本”选择其他更高版本的 Istio。

    ![环境检测](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/IstioUpdate04.png)

3. **执行升级**：环境检测通过后，将进入升级阶段，该过程包含 __升级__ 和 __健康检测__ 两阶段。

	- Istio 升级：Istio 镜像拉取和控制面组件升级

	- Istio 健康检测：Istio 控制面组件运行状态检查

	![执行升级](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/IstioUpdate05.png)

升级完成后，回到网格列表页面，可以看到网格的 Istio 版本已变更。

![执行升级](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/IstioUpdate06.png)

!!! note

    - 升级过程一旦开始将无法终止，升级期间建议不要对网格执行任何设置操作。
    - 更直观的操作演示，可参阅[视频教程](../../videos/mspider.md)。

## 手工升级：接入网格

由于接入网格是由用户自行托管，其网格部署形式无法确定；所以需要用户自行进行，本文给出 Istio 官方推荐的几种升级建议，请根据实际部署方案操作。

- **金丝雀升级** 通过先运行一个金丝雀部署的新控制平面升级 Istio。
- **原地升级** 原地升级和回退。
- **使用 Helm 升级** 使用 Helm 升级 Istio 的说明。

!!! warning "注意事项"

    尚未正式测试和推行一步升级多个版本（如 1.6.x 到 1.8.x），强烈建议通过阶梯升级的方式。

更多手工升级注意事项，请参考 Istio 官方文档： <https://istio.io/latest/docs/setup/upgrade/>
