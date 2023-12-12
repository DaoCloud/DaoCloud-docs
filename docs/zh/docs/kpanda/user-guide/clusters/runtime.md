# 如何选择容器运行时

容器运行时是 kubernetes 中对容器和容器镜像生命周期进行管理的重要组件。
kubernetes 在 1.19 版本中将 containerd 设为默认的容器运行时，并在 1.24 版本中移除了 Dockershim 组件的支持。

因此相较于 Docker 运行时，我们更加 **推荐您使用轻量的 containerd 作为您的容器运行时**，因为这已经成为当前主流的运行时选择。

除此之外，一些操作系统发行厂商对 Docker 运行时的兼容也不够友好，不同操作系统对运行时的支持如下表：

## 不同操作系统和推荐的运行时版本对应关系

| 操作系统        | 推荐的 containerd 版本 | 推荐的 Docker 版本 |
|-------------|---------------|------------|
| CentOS      |  1.7.5  | 20.10     |
| RedHatOS    |1.7.5    | 20.10      |
| KylinOS     | 1.7.5 | 19.03（仅 ARM 架构支持 ，在 x86 架构下不支持使用 Docker 作为运行时）|

更多支持的运行时版本信息，请参考 [RedHatOS 支持的运行时版本](https://github.com/kubernetes-sigs/kubespray/blob/master/roles/container-engine/docker/vars/redhat.yml/) 和 [KylinOS 支持的运行时版本](https://github.com/kubernetes-sigs/kubespray/blob/master/roles/container-engine/docker/vars/kylin.yml)

!!! note

    在离线安装模式下，需要提前准备相关操作系统的运行时离线包。
