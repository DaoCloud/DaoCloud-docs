# 边车版本升级

网格的 Istio 版本升级后，将触发边车升级功能。边车升级可分为 __热升级__ 和 __重启升级__ 两种升级方式。

- 热升级：道客订制版本 Istio 下边车可在不重启用户 Pod 的情况下完成边车升级，实现业务无中断；
- 重启升级：社区原生Istio 或不满足热升级环境要求的订制版 Istio 下边车升级方式，需重启用户 Pod。

完成 Istio 版本升级后，进入 __工作负载边车管理__ 界面，具备升级条件的工作负载将出现叹号提示信息，选中期望升级的工作负载，将出现 __边车升级__ 按钮。

![边车升级](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/sidecar-update01.png)

点击 __边车升级__ 按钮将进入 __边车升级版本__ 向导，该向导分为 __环境检测__ 、 __选择目标版本__ 、 __执行升级__ 三个步骤，在“热升级”和“重启升级”两种方式下，操作会有一定差别。

## 热升级

1. **环境检测**：该步骤中将检测集群环境是否满足热升级需求，检测项包括以下三项：

	- Istio 版本：是否是定制版本（版本后缀：-mspider）
	- K8s 版本：是否符合热升级要求范围
	- EphemeralContainer：是否已启用

	以上三项满足后将在后续步骤中进入热升级流程。

    ![环境监测](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/SidecarUpdate02.png)

2. **边车升级版本**：热升级流程中，可以选择期望升级的边车版本，默认为最新版本，如果选择了其他版本，相关 Pod 重启后也会自动升级至最新版本。

    ![升级版本](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/SidecarUpdate03.png)

3. **执行升级**：升级页面中展示了所选工作负载及相关边车信息，点击 __一键升级__ 将启动升级过程。

    ![执行升级](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/SidecarUpdate04.png)

## 重启升级

1. **环境检测**：在检测阶段如果检测项不满足热升级要求，之后两个步骤将进入重启升级流程。

    ![环境监测](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/SidecarUpdate05.png)

2. **边车升级版本** 在重启升级流程中，无法选择版本，仅支持升级至最新版本。

	![升级版本](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/SidecarUpdate06.png)

3. **执行升级**：升级页面中展示了所选工作负载的基本信息及边车版本信息，点击 __一键升级__ 将立即重启 Pod，请务必谨慎操作。

	![执行升级](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/SidecarUpdate07.png)

	![执行升级](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/SidecarUpdate08.png)

!!! note

    升级过程中关闭升级向导不会中断当前升级任务。
