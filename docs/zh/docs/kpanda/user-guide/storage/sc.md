# 存储池(SC)

存储池指将许多物理磁盘组成一个大型存储资源池，本平台支持接入各类存储厂商后创建块存储池、本地存储池、自定义存储池，然后为工作负载动态配置数据卷。

## 创建存储池(SC)

目前支持通过 YAML 和表单两种方式创建存储池，这两种方式各有优劣，可以满足不同用户的使用需求。

- 通过 YAML 创建步骤更少、更高效，但门槛要求较高，需要熟悉存储池的 YAML 文件配置。

- 通过表单创建更直观更简单，根据提示填写对应的值即可，但步骤更加繁琐。

### YAML 创建

1. 在集群列表中点击目标集群的名称，然后在左侧导航栏点击 __容器存储__ -> __存储池(SC)__ -> __YAML 创建__ 。

    ![路径](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/sc01.png)

2. 在弹框中输入或粘贴事先准备好的 YAML 文件，然后在弹框底部点击 __确定__ 。

    > 支持从本地导入 YAML 文件或将填写好的文件下载保存到本地。

    ![yaml](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/sc02.png)

### 表单创建

1. 在集群列表中点击目标集群的名称，然后在左侧导航栏点击 __容器存储__ -> __存储池(SC)__ -> __创建存储池(SC)__ 。

    ![路径](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/sc03.png)

2. 填写基本信息，然后在底部点击 __确定__ 。

    **自定义存储系统**

    - 存储池名称、驱动、回收策略在创建后不可修改。
    - CSI 存储驱动：基于标准 Kubernetes 的容器存储接口插件，需遵守存储厂商规定的格式，例如 __rancher.io/local-path__ 。

        - 有关如何填写不同厂商提供的 CSI 驱动，可参考 Kubernetes 官方文档[存储类](https://kubernetes.io/zh-cn/docs/concepts/storage/storage-classes/#provisioner)。
    - 回收策略：删除数据卷时，保留数据卷中的数据或者删除其中的数据。
    - 快照/扩容：开启后，基于该存储池的数据卷/数据卷声明才能支持扩容和快照功能，但 **前提是底层使用的存储驱动支持快照和扩容功能**。

    **Hwameistor 存储系统**

    - 存储池名称、驱动、回收策略在创建后不可修改。
    - 存储系统：Hwameistor 存储系统。
    - 存储类型：支持 LVM，裸磁盘类型
      - __LVM 类型__ ：Hwameistor 推荐使用方式，可使用高可用数据卷，对应的的 CSI 存储驱动为： __lvm.hwameistor.io__ 。
      - __裸磁盘数据卷__ ： 适用于高可用场景，无高可用能力，对应的 CSI 驱动为： __hdd.hwameistor.io__ 
    - 高可用模式：使用高可用能力之前请确认 __DRDB 组件__ 已安装。开启高可用模式后，可将数据卷副本数设置为 1 和 2。 如需要可将数据卷副本从 1 Convert 成 1
    - 回收策略：删除数据卷时，保留数据卷中的数据或者删除其中的数据。
    - 快照/扩容：开启后，基于该存储池的数据卷/数据卷声明才能支持扩容和快照功能，但 **前提是底层使用的存储驱动支持快照和扩容功能**。

    !!! note

        目前 Hwameistor xfs、ext4 两种文件系统，其中默认使用的是 xfs 文件系统，如果想要替换为 ext4，可以在自定义参数添加 __csi.storage.k8s.io/fstype: ext4__ 

    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/sc04.jpg)

## 更新存储池(SC)

在存储池列表页面，找到需要更新的存储池，在右侧的操作栏下选择 __编辑__ 即可通过更新存储池。

![更新](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/sc05.png)

!!! info

    选择 __查看 YAML__ 可以查看该存储池的 YAML 文件，但不支持编辑。

## 删除存储池(SC)

在存储池列表页面，找到需要删除的存储池，在右侧的操作栏下选择 __删除__ 。

![删除](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/sc06.png)
