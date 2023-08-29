# GPU Operator 创建 MIG（多实例 GPU）

NVIDIA 当前提供两种在 Kubernetes 节点上公开 MIG 设备的策略： 

- **Single 模式**，节点仅在其所有 GPU 上公开单一类型的 MIG 设备，节点上的所有 GPU 必须：
    - 属于同一个型号（例如 A100-SXM-40GB），只有同一型号 GPU 的 MIG Profile 才是一样的
    - 启用 MIG 配置，需要重启机器才能生效
    - 为在所有产品中公开“完全相同”的 MIG 设备类型，创建相同的GI 和 CI
- **Mixed 模式**，节点在其所有 GPU 上公开混合 MIG 设备类型。请求特定的 MIG 设备类型需要设备类型提供的计算切片数量和内存总量。
    - 节点上的所有 GPU 必须：属于同一产品线（例如 A100-SXM-40GB）
    - 每个 GPU 可启用或不启用 MIG，并且可以自由配置任何可用 MIG 设备类型的混合搭配。
    - 在节点上运行的 k8s-device-plugin 将：
        - 使用传统的 [nvidia.com/gpu](http://nvidia.com/gpu) 资源类型公开任何不处于 MIG 模式的 GPU
        - 使用遵循架构 nvidia.com/mig-<slice_count>g.<memory_size>gb 的资源类型公开各个 MIG 设备

注意：当前 GPU Operator 仅支持在线方式部署。

## 前提条件

- 确认集群节点上具有对应型号的 GPU 卡（[NVIDIA H100](https://www.nvidia.com/en-us/data-center/h100/)、
  [A100](https://www.nvidia.com/en-us/data-center/a100/) 和
  [A30](https://www.nvidia.com/en-us/data-center/products/a30-gpu/) Tensor Core GPU）
- 当前集群可联通网络

## 开启 GPU MIG Single 模式

1. 通过 Operator 开启 MIG  Single 模式

    ```sh
    helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
    helm repo update
    helm upgrade -i  gpu-operator -n gpu-operator -n gpu-operator --create-namespace nvidia/gpu-operator --set migStrategy=single --set node-feature-discovery.image.repository=k8s.m.daocloud.io/nfd/node-feature-discovery --set driver.version=525-5.15.0-78-generic # 通过 set 指定 MIG 模式为 Single
    ```

2. 给对应节点(已插入对应 GPU 卡节点)打上 切分规格

    ```sh
    kubectl label nodes {node} nvidia.com/mig.config="all-1g.10gb" --overwrite
    ```

3. 查看配置结果

    ```sh
    kubectl get node 10.206.0.17 -o yaml|grep nvidia.com/mig.config
    ```

## 开启 GPU MIG Mixed 模式

1. 通过 Operator 开启 MIG  Mixed 模式

    ```sh
    helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
    helm repo update
    helm install --generate-name --set migStrategy=mixed --set allowDefaultNamespace=true  nvidia/nvidia-device-plugin --set node-feature-discovery.image.repository=k8s.m.daocloud.io/nfd/node-feature-discovery # 通过 set 指定 MIG 模式为 Mixed
    ```

2. 设置`config.yaml`文件，此`config`文件中设置 MIG GI 实例切分规格。

    ```yaml
    version: v1
    mig-configs:
      all-disabled:
        - devices: all
          mig-enabled: false
      all-enabled:
        - devices: all
          mig-enabled: true
          mig-devices: {}
      all-1g.10gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            1g.5gb: 7
      all-1g.10gb.me:
        - devices: all
          mig-enabled: true
          mig-devices:
            1g.10gb+me: 1
      all-1g.20gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            1g.20gb: 4
      all-2g.20gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            2g.20gb: 3
      all-3g.40gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            3g.40gb: 2
      all-4g.40gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            4g.40gb: 1
      all-7g.80gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            7g.80gb: 1
      all-balanced:
        - device-filter: ["0x233110DE", "0x232210DE", "0x20B210DE", "0x20B510DE", "0x20F310DE", "0x20F510DE"]
          devices: all
          mig-enabled: true
          mig-devices:
            1g.10gb: 2
            2g.20gb: 1
            3g.40gb: 1
      custom-config:    # 设置后会按照设置规格切分 CI 实例
        - devices: all
          mig-enabled: true
          mig-devices:
            3g.40gb: 2
    ```

3. 在上述的`config.yaml` 中设置 `custom-config`，设置后会按照规格切分 CI 实例

    ```yaml
    custom-config:
      - devices: all
        mig-enabled: true
        mig-devices:
          1c.3g.40gb: 6
    ```

4. 按照修改后的 `config.yaml` 自定义设置：

    ```sh
    kubectl create configmap -n gpu-operator custome-mig-parted-config --from-file=config.yaml
    helm install gpu-operator -n gpu-operator --create-namespace nvidia/gpu-operator --set migManager.config.name=mig-config --set node-feature-
    discovery.image.repository=k8s.m.daocloud.io/nfd/node-feature-discovery
    ···
    
    或者
    
    ···sh
    helm upgrade -i gpu-operator nvidia/gpu-operator -n gpu-operator --set mig.strategy=mixed --set migManager.config.name=custome-mig-parted-config --set node-feature-discovery.image.repository=k8s.m.daocloud.io/nfd/node-feature-discovery
    ```

5. 设置完成后给对应的节点打上切分规格

    ```sh
    kubectl label nodes {node} nvidia.com/mig.config="custom-config" --overwrite
    ```

6. 查看配置结果

    ```sh
    kubectl get node 10.206.0.17 -o yaml|grep nvidia.com/mig.config
    ```

    设置完成后，在确认部署应用时即可使用 GPU MIG 资源。
