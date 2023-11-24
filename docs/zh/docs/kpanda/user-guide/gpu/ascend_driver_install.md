# 昇腾 NPU 组件安装

本章节提供 昇腾 NPU 驱动和 Device Plugin 的安装指导。

## 前提条件

1. 安装前请确认支持的 NPU 型号，详情请参考：[昇腾 GPU 矩阵](gpu_matrix.md)
2. 请确认 对应 NPU 型号所要求的内核版本是否匹配，详情请参考：[昇腾 GPU 矩阵](gpu_matrix.md)

## 安装步骤

使用 NPU 资源之前，需要完成固件安装、NPU 驱动安装、 Docker Runtime 安装以及 NPU Device Plugin 安装，详情参考如下步骤。

### 安装固件

1. 安装请请确认内核版本在“二进制安装”安装方式对应的版本范围内，则可以直接安装NPU驱动固件。
2. 固件与驱动下载请参考： [固件下载地址](https://www.hiascend.com/zh/hardware/firmware-drivers/community?product=2&model=15&cann=6.3.RC2.alpha005&driver=1.0.20.alpha)
3. 固件安装请参考：[安装NPU驱动固件](https://www.hiascend.com/document/detail/zh/quick-installation/23.0.RC2/quickinstg/800_3000/quickinstg_800_3000_0001.html)

### 安装 NPU 驱动

1. 如驱动未安装，请参考昇腾官方文档进行安装：例如 Ascend910，参考：[910 驱动安装文档](https://www.hiascend.com/document/detail/zh/Atlas%20200I%20A2/23.0.RC3/EP/installationguide/Install_87.html)。

2. 运行 `npu-smi info` 命令，并且能够正常返回 npu 信息，表示 NPU 驱动与固件已就绪。

    ![昇腾信息](./images/npu-smi-info.png)

### 安装 Docker Runtime

1. 下载 Ascend Docker Runtime

   社区版下载地址：https://www.hiascend.com/zh/software/mindx-dl/community

   ```
   $ wget -c https://mindx.obs.cn-south-1.myhuaweicloud.com/OpenSource/MindX/MindX%205.0.RC2/MindX%20DL%205.0.RC2/Ascend-docker-runtime_5.0.RC2_linux-x86_64.run
   ```

   安装到默认路径下，依次执行以下两条命令:

   ```
   $ chmod u+x Ascend-docker-runtime_5.0.RC2_linux-x86_64.run 
   $ ./Ascend-docker-runtime_5.0.RC2_linux-x86_64.run --install
   ```

   安装到指定路径下，依次执行以下两条命令，<path>参数为指定的安装路径:

   ```
   $ chmod u+x Ascend-docker-runtime_5.0.RC2_linux-x86_64.run 
   $ ./Ascend-docker-runtime_{version}_linux-{arch}.run --install --install-path=<path>
   ```

   2. 修改Containerd配置文件

   Containerd无默认配置文件时，依次执行以下3条命令，创建配置文件:

   ```
   $ mkdir /etc/containerd 
   $ containerd config default > /etc/containerd/config.toml 
   $ vim /etc/containerd/config.toml
   ```

   Containerd有配置文件时

   ```
   $ vim /etc/containerd/config.toml
   ```

   根据实际情况修改runtime的安装路径,主要修改 runtime 字段:

   ```
   ... 
   [plugins."io.containerd.monitor.v1.cgroups"]
       no_prometheus = false  
   [plugins."io.containerd.runtime.v1.linux"]
       shim = "containerd-shim"
       runtime = "/usr/local/Ascend/Ascend-Docker-Runtime/ascend-docker-runtime"
       runtime_root = ""
       no_shim = false
       shim_debug = false
     [plugins."io.containerd.runtime.v2.task"]
       platforms = ["linux/amd64"]
    ...
   ```

   执行以下命令，重启Containerd：

   ```
   $ systemctl restart containerd
   ```

### 安装 Device Plugin

1. 如驱动与 Device Plugin 未安装，请参考昇腾官方文档进行安装，参考：[昇腾 NPU Device Plugin](https://www.hiascend.com/document/detail/zh/mindx-dl/50rc3/clusterscheduling/clusterschedulingig/dlug_installation_001.html)

2. 镜像拉取可参考镜像拉取地址 : [harbor.daocloud.cn/library/ascend-k8sdeviceplugin:v5.0.RC2](http://harbor.daocloud.cn/library/ascend-k8sdeviceplugin:v5.0.RC2)
   注意：昇腾镜像仓库中拉取的MindX DL镜像与组件启动yaml中的名字不一致，需要重命名拉取的镜像后才能启动。根据以下步骤将2中获取的镜像重新命名，同时建议删除原始名字的镜像。具体操作如下。

   ```
   $ ctr -n k8s.io i tag harbor.daocloud.cn/library/ascend-k8sdeviceplugin:v5.0.RC2 ascend-k8sdeviceplugin:v5.0.RC2
   ```

3. 获取 `device-plugin-310-v5.0.RC2.yaml` 文件，请参考[下载地址]([https://mindx.obs.cn-south-1.myhuaweicloud.com/OpenSource/MindX/MindX%205.0.RC2/MindX%20DL%205.0.RC2/Ascend-mindxdl-device-plugin_5.0.RC2_linux-x86_64.zip](https://mindx.obs.cn-south-1.myhuaweicloud.com/OpenSource/MindX/MindX 5.0.RC2/MindX DL 5.0.RC2/Ascend-mindxdl-device-plugin_5.0.RC2_linux-x86_64.zip))

4. 执行 Kube Apply：

   ```
   $ kubectl apply -f device-plugin-310-v5.0.RC2.yaml 
   # 需要给 node 打上 accelerator=huawei-Ascend310 的label，才能被调度启动 pod。 
   $ kubectl label nodes {node-name} accelerator=huawei-Ascend310
   ```

   注意：`device-plugin-310-v5.0.RC2.yaml` 中的镜像地址是 `ascend-k8sdeviceplugin:v5.0.RC2`

   构建 `ascend-k8sdeviceplugin` 镜像：从下载的代码包中有 `Dockerfile`文件（详情参考：[软件包说明](https://www.hiascend.com/document/detail/zh/mindx-dl/300/dluserguide/clusterscheduling/dlug_installation_02_000035.html)），执行构建命令：

   ```
   # 310 卡构建使用Dockerfile 
   $  docker build --no-cache -t  ascend-k8sdeviceplugin:v5.0.RC2 .  
   # 310P 卡构建使用Dockerfile-310P-1usoc 
   $ docker build --no-cache -t ascend-k8sdeviceplugin:v5.0.RC2 -f Dockerfile .
   ```

   | Dockerfile            | Ascend Device Plugin 镜像构建文本文件                        |
   | --------------------- | ------------------------------------------------------------ |
   | Dockerfile-310P-1usoc | Atlas 200I Soc A1 核心版上Ascend Device Plugin镜像构建文本文件。 |

   5. NPU Device Plugin 默认安装在 `kube-system` 命名空间下。这是一个 DaemonSet 类型的工作负载，可以通过 `kubectl get pod -n kube-system | grep ascend` 命令查看，输出如下：

![昇腾 Device Plugin](./images/ascend-device-plugin.png)



