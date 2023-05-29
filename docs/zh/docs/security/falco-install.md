# 安装 Falco

请确认您的集群已成功接入`容器管理`平台，然后执行以下步骤安装 Falco。

1. 从左侧导航栏点击`容器管理`—>`集群列表`，然后找到准备安装 Falco 的集群名称。

    ![falco_cluster](https://docs.daocloud.io/daocloud-docs-images/docs/security/images/falco_cluster.png)

2. 在左侧导航栏中选择 `Helm 应用` -> `Helm 模板`，找到并点击 `Falco`。

    ![falco_helm-1](https://docs.daocloud.io/daocloud-docs-images/docs/security/images/falco-install-1.png)

3. 在`版本选择`中选择希望安装的版本，点击`安装`。

    ![falco-helm-2](https://docs.daocloud.io/daocloud-docs-images/docs/security/images/falco-install-2.png)

4. 在安装界面，填写所需的安装参数。

    ![falco_helm-3](https://docs.daocloud.io/daocloud-docs-images/docs/security/images/falco-install-3.png)

    在如上界面中，填写`应用名称`、`命名空间`、`版本`等。

    ![falco_helm-4](https://docs.daocloud.io/daocloud-docs-images/docs/security/images/falco-install-4.png)

    在如上界面中，填写以下参数：

    - `Falco` -> `Image Settings` -> `Registry`：设置 Falco 镜像的仓库地址，已经默认填写可用的在线仓库。如果是私有化环境，可修改为私有仓库地址。

    - `Falco` -> `Image Settings` -> `Repository`：设置 Falco 镜像名。

    - `Falco` -> `Falco Driver` -> `Image Settings` -> `Registry`：设置 Falco Driver 镜像的仓库地址，已经默认填写可用的在线仓库。如果是私有化环境，可修改为私有仓库地址。

    - `Falco` -> `Falco Driver` -> `Image Settings` -> `Repository`：设置 Falco Driver 镜像名。

    - `Falco` -> `Falco Driver` -> `Image Settings` -> `Driver Kind`：设置 Driver Kind，提供以下两种选择：

        1. ebpf：使用 ebpf 来检测事件，这需要 Linux 内核支持 ebpf，并启用 CONFIG_BPF_JIT 和 sysctl net.core.bpf_jit_enable=1。

        2. module：使用内核模块检测，支持有限的操作系统版本，参考 module 支持[系统版本](https://download.falco.org/?prefix=driver)。

    - `Falco` -> `Falco Driver` -> `Image Settings` -> `Log Level`：要包含在日志中的最小日志级别。

        可选择值为：`emergency`, `alert`, `critical`, `error`, `warning`, `notice`, `info`, `debug`。

    - `Falco` -> `Falco Driver` -> `Image Settings` -> `Registry`：设置 Falco Driver 镜像的仓库地址，已经默认填写可用的在线仓库。如果是私有化环境，可修改为私有仓库地址。

    - `Falco` -> `Falco Driver` -> `Image Settings` -> `Repository`：设置 Falco Driver 镜像名。

    - `Falco` -> `Falco Driver` -> `Image Settings` -> `Driver Kind`：设置 Driver Kind，提供以下两种选择：

        1. ebpf：使用 ebpf 来检测事件，这需要 Linux 内核支持 ebpf，并启用 CONFIG_BPF_JIT 和 sysctl net.core.bpf_jit_enable=1。
        1. module：使用内核模块检测，支持有限的操作系统版本，参考 module 支持[系统版本](https://download.falco.org/?prefix=driver)。

    - `Falco` -> `Falco Driver` -> `Image Settings` -> `Log Level`：要包含在日志中的最小日志级别。

        可选择值为：`emergency`、`alert`、`critical`、`error`、`warning`、`notice`、`info`、`debug`。

5. 点击右下角`确定`按钮即可完成安装。
